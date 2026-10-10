#!/usr/bin/env python3
"""
Shielding Verification Calculator — Colé S.A.
Cálculo de D_sem según NCRP 147/177/148 para verificación empírica de blindaje.

Uso:
    python shielding_calc.py --input data.json --output results.json

El archivo data.json debe contener la estructura definida abajo.
También puede importarse como módulo para uso programático.
"""

import json
import sys
import argparse
from dataclasses import dataclass, field, asdict
from typing import List, Optional
from enum import Enum


class Modalidad(str, Enum):
    RX_CONVENCIONAL = "rx_convencional"
    DENTAL_PANORAMICO = "dental_panoramico"
    DENTAL_CBCT = "dental_cbct"
    CT = "ct"
    MAMOGRAFIA = "mamografia"
    FLUOROSCOPIA = "fluoroscopia"


class TipoZona(str, Enum):
    CONTROLADA = "controlada"
    SUPERVISADA = "supervisada"


class TipoBarrera(str, Enum):
    PRIMARIA_BUCKY = "primaria_bucky"
    PRIMARIA_LATERAL = "primaria_lateral"
    SECUNDARIA = "secundaria"


# --- Parámetros NCRP 147 por defecto ---

NCRP147_W_NORM = {
    TipoBarrera.PRIMARIA_BUCKY: 0.6,       # mAmin/paciente
    TipoBarrera.PRIMARIA_LATERAL: 1.9,      # mAmin/paciente
    TipoBarrera.SECUNDARIA: 2.5,            # mAmin/paciente
}

NCRP147_U = {
    TipoBarrera.PRIMARIA_BUCKY: 1.0,
    TipoBarrera.PRIMARIA_LATERAL: 0.09,
    TipoBarrera.SECUNDARIA: 1.0,
}

NCRP147_P = {
    TipoZona.CONTROLADA: 0.1,      # mSv/sem
    TipoZona.SUPERVISADA: 0.02,    # mSv/sem
}

NCRP147_T_REFERENCE = {
    "oficina": 1.0,
    "consultorio": 1.0,
    "laboratorio": 1.0,
    "cuarto_control": 1.0,
    "recepcion": 1.0,
    "enfermeria": 1.0,
    "pasillo": 0.2,
    "bano": 0.2,
    "vestidor": 0.2,
    "puerta": 0.125,
    "escalera": 0.125,
    "exterior": 0.05,
    "estacionamiento": 0.025,
    "techo": 0.025,
}

# --- NCRP 177 Dental ---
NCRP177_W_NORM = {
    "intraoral": 0.15,
    "panoramico": 0.5,
    "cefalometrico": 0.3,
    "cbct": 1.5,
}


@dataclass
class TecnicaMedicion:
    """Parámetros de la técnica usada durante la medición."""
    kvp: float = 100.0
    mas: float = 60.0
    colimacion_cm: str = "40x40"
    dfd_m: float = 1.0
    con_maniqui: bool = False

    @property
    def mamin(self) -> float:
        """Convierte mAs a mAmin."""
        return self.mas / 60.0


@dataclass
class Barrera:
    """Datos de una barrera individual."""
    nombre: str
    tipo_barrera: str  # primaria_bucky, primaria_lateral, secundaria
    dosis_integrada_usv: float  # µSv medido en una exposición
    tipo_zona: str  # controlada, supervisada
    factor_uso_U: Optional[float] = None  # Si None, se asigna por tipo_barrera
    factor_ocupacion_T: Optional[float] = None  # Si None, se debe proporcionar
    limite_P_msv_sem: Optional[float] = None  # Si None, se asigna por tipo_zona
    area_adyacente: str = ""  # Descripción del área (pasillo, oficina, etc.)
    # Campos calculados (se llenan después)
    dosis_integrada_msv: float = 0.0
    dosis_normalizada: float = 0.0
    dosis_semanal: float = 0.0
    dosis_anual: float = 0.0
    cumple: bool = True
    mamin_max: float = 0.0
    n_pac_max: float = 0.0
    margen_pct: float = 0.0
    alerta: str = ""


@dataclass
class DatosInstalacion:
    """Datos generales de la instalación."""
    institucion: str = ""
    servicio: str = "Radiología"
    direccion: str = ""
    fecha_monitoreo: str = ""
    empresa_contratante: str = ""


@dataclass
class Equipamiento:
    """Equipamiento utilizado."""
    equipo_rx_marca: str = ""
    equipo_rx_modelo: str = ""
    kv_max: float = 150.0
    mas_max: float = 800.0
    maniqui_descripcion: str = "Cilindro de agua de 50 cm de largo y 30 cm de diámetro"
    instrumento_marca: str = ""
    instrumento_modelo: str = ""
    instrumento_ns: str = ""
    sonda_ns: str = ""
    fecha_calibracion: str = ""
    vigencia_calibracion: str = "2 años"


@dataclass
class DatosVerificacion:
    """Estructura completa de datos para la verificación."""
    instalacion: DatosInstalacion = field(default_factory=DatosInstalacion)
    equipamiento: Equipamiento = field(default_factory=Equipamiento)
    tecnica_primaria: TecnicaMedicion = field(
        default_factory=lambda: TecnicaMedicion(kvp=100, mas=60, con_maniqui=False)
    )
    tecnica_secundaria: TecnicaMedicion = field(
        default_factory=lambda: TecnicaMedicion(kvp=100, mas=250, con_maniqui=True)
    )
    modalidad: str = "rx_convencional"
    n_pacientes_semana: int = 400
    barreras: List[Barrera] = field(default_factory=list)


def calcular_barrera(
    barrera: Barrera,
    tecnica: TecnicaMedicion,
    n_pacientes: int = 400,
    modalidad: str = "rx_convencional",
) -> Barrera:
    """
    Calcula D_sem y verifica cumplimiento para una barrera individual.

    Fórmula: D_sem = (D_med / mAmin_med) × W × U × T
    """
    tipo = barrera.tipo_barrera

    # 1. Convertir µSv → mSv
    barrera.dosis_integrada_msv = barrera.dosis_integrada_usv / 1000.0

    # 2. mAmin de la medición
    mamin_med = tecnica.mamin

    # 3. Dosis normalizada (mSv/mAmin)
    if mamin_med > 0:
        barrera.dosis_normalizada = barrera.dosis_integrada_msv / mamin_med
    else:
        barrera.dosis_normalizada = 0.0
        barrera.alerta = "ERROR: mAmin_med = 0"
        return barrera

    # 4. W_norm y W según tipo de barrera
    if modalidad == "rx_convencional":
        w_norm_map = {
            "primaria_bucky": NCRP147_W_NORM[TipoBarrera.PRIMARIA_BUCKY],
            "primaria_lateral": NCRP147_W_NORM[TipoBarrera.PRIMARIA_LATERAL],
            "secundaria": NCRP147_W_NORM[TipoBarrera.SECUNDARIA],
        }
    else:
        # Para otras modalidades, usar secundarias como default
        w_norm_map = {
            "primaria_bucky": 0.6,
            "primaria_lateral": 1.9,
            "secundaria": 2.5,
        }

    w_norm = w_norm_map.get(tipo, 2.5)
    W = n_pacientes * w_norm

    # 5. Factor de uso (U)
    if barrera.factor_uso_U is not None:
        U = barrera.factor_uso_U
    else:
        u_map = {
            "primaria_bucky": NCRP147_U[TipoBarrera.PRIMARIA_BUCKY],
            "primaria_lateral": NCRP147_U[TipoBarrera.PRIMARIA_LATERAL],
            "secundaria": NCRP147_U[TipoBarrera.SECUNDARIA],
        }
        U = u_map.get(tipo, 1.0)
        barrera.factor_uso_U = U

    # 6. Factor de ocupación (T)
    T = barrera.factor_ocupacion_T if barrera.factor_ocupacion_T is not None else 1.0

    # 7. Límite P
    if barrera.limite_P_msv_sem is not None:
        P = barrera.limite_P_msv_sem
    else:
        p_map = {
            "controlada": NCRP147_P[TipoZona.CONTROLADA],
            "supervisada": NCRP147_P[TipoZona.SUPERVISADA],
        }
        P = p_map.get(barrera.tipo_zona, 0.02)
        barrera.limite_P_msv_sem = P

    # 8. D_sem = D_norm × W × U × T
    barrera.dosis_semanal = barrera.dosis_normalizada * W * U * T

    # 9. D_anual = D_sem × 50
    barrera.dosis_anual = barrera.dosis_semanal * 50.0

    # 10. Cumplimiento
    barrera.cumple = barrera.dosis_semanal <= P

    # 11. Capacidad máxima
    if barrera.dosis_normalizada > 0 and U > 0 and T > 0:
        barrera.mamin_max = P / (barrera.dosis_normalizada * U * T)
        barrera.n_pac_max = barrera.mamin_max / w_norm
    else:
        barrera.mamin_max = float('inf')
        barrera.n_pac_max = float('inf')

    # 12. Margen
    if P > 0:
        barrera.margen_pct = ((P - barrera.dosis_semanal) / P) * 100.0

    # 13. Alertas
    alertas = []
    if not barrera.cumple:
        alertas.append("NO CUMPLE — D_sem > P")
    elif barrera.margen_pct < 50:
        alertas.append(f"Margen reducido ({barrera.margen_pct:.1f}%)")
    if barrera.n_pac_max < 400 and barrera.n_pac_max != float('inf'):
        alertas.append(f"Capacidad limitada: {barrera.n_pac_max:.0f} pac/sem")
    if barrera.dosis_integrada_usv > 10 and tipo == "secundaria":
        alertas.append("Dosis atípicamente alta para barrera secundaria")
    if barrera.dosis_integrada_usv == 0:
        alertas.append("Dosis = 0 — verificar dato de campo")

    barrera.alerta = "; ".join(alertas) if alertas else "OK"

    return barrera


def calcular_verificacion(datos: DatosVerificacion) -> dict:
    """
    Ejecuta el cálculo completo de verificación de blindaje.

    Returns:
        dict con resultados, resumen y alertas
    """
    resultados = []

    for barrera in datos.barreras:
        # Seleccionar técnica según tipo de barrera
        if barrera.tipo_barrera in ("primaria_bucky", "primaria_lateral"):
            tecnica = datos.tecnica_primaria
        else:
            tecnica = datos.tecnica_secundaria

        barrera_calc = calcular_barrera(
            barrera=barrera,
            tecnica=tecnica,
            n_pacientes=datos.n_pacientes_semana,
            modalidad=datos.modalidad,
        )
        resultados.append(barrera_calc)

    # Resumen
    total_barreras = len(resultados)
    barreras_cumplen = sum(1 for b in resultados if b.cumple)
    barreras_no_cumplen = [b.nombre for b in resultados if not b.cumple]
    barreras_margen_reducido = [
        b.nombre for b in resultados
        if b.cumple and b.margen_pct < 50
    ]

    todas_cumplen = barreras_cumplen == total_barreras

    resumen = {
        "total_barreras": total_barreras,
        "barreras_cumplen": barreras_cumplen,
        "barreras_no_cumplen": barreras_no_cumplen,
        "barreras_margen_reducido": barreras_margen_reducido,
        "todas_cumplen": todas_cumplen,
        "modalidad": datos.modalidad,
        "n_pacientes": datos.n_pacientes_semana,
    }

    # Parámetros usados
    parametros = {
        "tecnica_primaria": {
            "kvp": datos.tecnica_primaria.kvp,
            "mas": datos.tecnica_primaria.mas,
            "mamin": datos.tecnica_primaria.mamin,
        },
        "tecnica_secundaria": {
            "kvp": datos.tecnica_secundaria.kvp,
            "mas": datos.tecnica_secundaria.mas,
            "mamin": datos.tecnica_secundaria.mamin,
        },
        "W_bucky": datos.n_pacientes_semana * NCRP147_W_NORM[TipoBarrera.PRIMARIA_BUCKY],
        "W_lateral": datos.n_pacientes_semana * NCRP147_W_NORM[TipoBarrera.PRIMARIA_LATERAL],
        "W_secundarias": datos.n_pacientes_semana * NCRP147_W_NORM[TipoBarrera.SECUNDARIA],
    }

    return {
        "barreras": [asdict(b) for b in resultados],
        "resumen": resumen,
        "parametros": parametros,
    }


def from_json(filepath: str) -> DatosVerificacion:
    """Carga datos desde un archivo JSON."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    inst = data.get("instalacion", {})
    equip = data.get("equipamiento", {})
    tp = data.get("tecnica_primaria", {})
    ts = data.get("tecnica_secundaria", {})

    datos = DatosVerificacion(
        instalacion=DatosInstalacion(**inst) if inst else DatosInstalacion(),
        equipamiento=Equipamiento(**equip) if equip else Equipamiento(),
        tecnica_primaria=TecnicaMedicion(**tp) if tp else TecnicaMedicion(kvp=100, mas=60),
        tecnica_secundaria=TecnicaMedicion(**ts) if ts else TecnicaMedicion(kvp=100, mas=250, con_maniqui=True),
        modalidad=data.get("modalidad", "rx_convencional"),
        n_pacientes_semana=data.get("n_pacientes_semana", 400),
    )

    for b_data in data.get("barreras", []):
        datos.barreras.append(Barrera(
            nombre=b_data["nombre"],
            tipo_barrera=b_data.get("tipo_barrera", "secundaria"),
            dosis_integrada_usv=b_data["dosis_integrada_usv"],
            tipo_zona=b_data.get("tipo_zona", "supervisada"),
            factor_uso_U=b_data.get("factor_uso_U"),
            factor_ocupacion_T=b_data.get("factor_ocupacion_T"),
            limite_P_msv_sem=b_data.get("limite_P_msv_sem"),
            area_adyacente=b_data.get("area_adyacente", ""),
        ))

    return datos


def main():
    parser = argparse.ArgumentParser(description="Shielding Verification Calculator — Colé S.A.")
    parser.add_argument("--input", "-i", required=True, help="JSON con datos de medición")
    parser.add_argument("--output", "-o", default="results.json", help="JSON de resultados")
    args = parser.parse_args()

    datos = from_json(args.input)
    resultados = calcular_verificacion(datos)

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)

    # Resumen en consola
    res = resultados["resumen"]
    print(f"\n{'='*60}")
    print(f"VERIFICACIÓN DE BLINDAJE — {datos.instalacion.institucion}")
    print(f"{'='*60}")
    print(f"Modalidad: {res['modalidad']}")
    print(f"Pacientes/semana: {res['n_pacientes']}")
    print(f"Total barreras: {res['total_barreras']}")
    print(f"Cumplen: {res['barreras_cumplen']}")

    if res['barreras_no_cumplen']:
        print(f"\n⚠ NO CUMPLEN: {', '.join(res['barreras_no_cumplen'])}")
    if res['barreras_margen_reducido']:
        print(f"\n⚡ Margen reducido: {', '.join(res['barreras_margen_reducido'])}")

    if res['todas_cumplen']:
        print(f"\n✓ TODAS LAS BARRERAS CUMPLEN")
    else:
        print(f"\n✗ HAY BARRERAS QUE NO CUMPLEN")

    print(f"\nResultados guardados en: {args.output}")


if __name__ == "__main__":
    main()
