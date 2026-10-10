#!/usr/bin/env python3
"""
update_state.py — Utilidad para actualizar el estado persistente del skill job-hunter.

Uso:
    python update_state.py --candidate <id> --action <accion> --url <url> [--metadata '<json>']

Acciones soportadas:
    mark_applied      Mover URL de reported_urls a applied_urls
    mark_expired      Mover URL a expired_urls (con razón)
    add_reported      Agregar nueva URL a reported_urls
    list              Listar estado actual del candidato
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

STATE_FILE = Path(__file__).resolve().parent.parent / "state" / "seen.json"


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"schema_version": "1.0", "candidates": {}}
    with STATE_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with STATE_FILE.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def ensure_candidate(state: dict, candidate_id: str) -> dict:
    if candidate_id not in state["candidates"]:
        state["candidates"][candidate_id] = {
            "reported_urls": [],
            "applied_urls": [],
            "expired_urls": [],
            "last_run_iso": str(date.today()),
            "total_runs": 0,
        }
    return state["candidates"][candidate_id]


def find_and_remove(url: str, lst: list) -> dict | None:
    for i, item in enumerate(lst):
        if item.get("url") == url:
            return lst.pop(i)
    return None


def mark_applied(candidate_id: str, url: str) -> None:
    state = load_state()
    cand = ensure_candidate(state, candidate_id)

    record = find_and_remove(url, cand["reported_urls"])
    if record is None:
        # If not in reported, build minimal record
        record = {"url": url}
    record["applied_iso"] = str(date.today())
    cand["applied_urls"].append(record)
    save_state(state)
    print(f"OK — Marcada como aplicada: {url}")


def mark_expired(candidate_id: str, url: str, reason: str) -> None:
    state = load_state()
    cand = ensure_candidate(state, candidate_id)

    record = find_and_remove(url, cand["reported_urls"])
    if record is None:
        record = {"url": url}
    record["verified_expired_iso"] = str(date.today())
    record["reason"] = reason or "marcada manualmente como expirada"
    cand["expired_urls"].append(record)
    save_state(state)
    print(f"OK — Marcada como expirada: {url}  ({reason})")


def add_reported(candidate_id: str, url: str, metadata: dict) -> None:
    state = load_state()
    cand = ensure_candidate(state, candidate_id)

    if any(r.get("url") == url for r in cand["reported_urls"]):
        print(f"AVISO — URL ya estaba en reported_urls: {url}")
        return

    record = {
        "url": url,
        "first_reported_iso": str(date.today()),
        "last_verified_iso": str(date.today()),
    }
    record.update(metadata or {})
    cand["reported_urls"].append(record)
    save_state(state)
    print(f"OK — Agregada a reported_urls: {url}")


def list_state(candidate_id: str) -> None:
    state = load_state()
    cand = state["candidates"].get(candidate_id)
    if cand is None:
        print(f"Candidato '{candidate_id}' no encontrado en el estado.")
        return

    print(f"\nEstado del candidato: {candidate_id}")
    print(f"  Última corrida: {cand.get('last_run_iso')}")
    print(f"  Total corridas: {cand.get('total_runs', 0)}")
    print(f"\n  Reportadas activas: {len(cand['reported_urls'])}")
    for r in cand["reported_urls"]:
        print(f"    - {r.get('company', '?')} — {r.get('title', '?')}")
        print(f"      {r['url']}")
    print(f"\n  Aplicadas: {len(cand['applied_urls'])}")
    for r in cand["applied_urls"]:
        print(f"    - {r.get('company', '?')} — {r['url']}")
    print(f"\n  Expiradas: {len(cand['expired_urls'])}")
    for r in cand["expired_urls"][-5:]:  # solo últimas 5 para no saturar
        print(f"    - {r.get('company', '?')} — razón: {r.get('reason', '?')}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Actualizar estado del skill job-hunter")
    parser.add_argument("--candidate", required=True, help="ID del candidato (ej: eddy_fresno)")
    parser.add_argument(
        "--action",
        required=True,
        choices=["mark_applied", "mark_expired", "add_reported", "list"],
        help="Acción a ejecutar",
    )
    parser.add_argument("--url", help="URL de la oferta (requerido para todas las acciones excepto 'list')")
    parser.add_argument("--reason", default="", help="Razón de expiración (para mark_expired)")
    parser.add_argument("--metadata", default="{}", help="JSON con metadata adicional (para add_reported)")

    args = parser.parse_args()

    if args.action == "list":
        list_state(args.candidate)
        return 0

    if not args.url:
        print("ERROR: --url es requerido para esta acción", file=sys.stderr)
        return 1

    if args.action == "mark_applied":
        mark_applied(args.candidate, args.url)
    elif args.action == "mark_expired":
        mark_expired(args.candidate, args.url, args.reason)
    elif args.action == "add_reported":
        try:
            metadata = json.loads(args.metadata)
        except json.JSONDecodeError as e:
            print(f"ERROR parsing --metadata: {e}", file=sys.stderr)
            return 1
        add_reported(args.candidate, args.url, metadata)

    return 0


if __name__ == "__main__":
    sys.exit(main())
