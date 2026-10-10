[CmdletBinding()]
param(
    [string]$CanonRoot = "$env:USERPROFILE\skills-canon",
    [string[]]$ConsumerRoots = @(
        "$env:USERPROFILE\.codex\skills",
        "$env:USERPROFILE\.gemini\skills"
    )
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $CanonRoot -PathType Container)) {
    throw "No existe el canon: $CanonRoot"
}

$skills = @(
    Get-ChildItem -LiteralPath $CanonRoot -Directory -Force |
        Where-Object {
            -not $_.Name.StartsWith('.') -and
            (Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') -PathType Leaf)
        } |
        Sort-Object Name
)

if (-not $skills) {
    throw "No se encontraron skills con SKILL.md en $CanonRoot"
}

$exclusionsPath = Join-Path $CanonRoot 'sync-exclusions.json'
$exclusions = if (Test-Path -LiteralPath $exclusionsPath -PathType Leaf) {
    Get-Content -Raw -LiteralPath $exclusionsPath | ConvertFrom-Json
} else {
    [pscustomobject]@{ codex = @(); gemini = @() }
}

$created = 0
$current = 0
$conflicts = 0

foreach ($consumerRoot in $ConsumerRoots) {
    if (-not (Test-Path -LiteralPath $consumerRoot -PathType Container)) {
        New-Item -ItemType Directory -Path $consumerRoot -Force | Out-Null
    }

    $consumerName = if ($consumerRoot -match '[\\/]\.codex[\\/]') {
        'codex'
    } elseif ($consumerRoot -match '[\\/]\.gemini[\\/]') {
        'gemini'
    } else {
        throw "No se puede determinar el consumidor para $consumerRoot"
    }
    $excludedNames = @($exclusions.$consumerName)
    $eligibleSkills = @($skills | Where-Object { $_.Name -notin $excludedNames })

    foreach ($skill in $eligibleSkills) {
        $destination = Join-Path $consumerRoot $skill.Name

        if (-not (Test-Path -LiteralPath $destination)) {
            New-Item -ItemType Junction -Path $destination -Target $skill.FullName | Out-Null
            Write-Output "CREADO  $destination -> $($skill.FullName)"
            $created++
            continue
        }

        $existing = Get-Item -LiteralPath $destination -Force
        if ($existing.LinkType -notin @('Junction', 'SymbolicLink')) {
            Write-Warning "CONFLICTO: existe una carpeta física en $destination"
            $conflicts++
            continue
        }

        $target = [System.IO.Path]::GetFullPath(($existing.Target | Select-Object -First 1))
        $expected = [System.IO.Path]::GetFullPath($skill.FullName)
        if ($target -ne $expected) {
            Write-Warning "CONFLICTO: $destination apunta a $target; se esperaba $expected"
            $conflicts++
            continue
        }

        $current++
    }

    Write-Output "$consumerName`: $($eligibleSkills.Count) habilitadas; $($excludedNames.Count) excluidas por compatibilidad."
}

Write-Output "Resumen: $($skills.Count) skills; $created enlaces creados; $current correctos; $conflicts conflictos."
if ($conflicts -gt 0) {
    exit 2
}
