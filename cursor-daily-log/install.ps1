param(
    [ValidateSet('cursor', 'claude-code', 'opencode', 'codex', 'all')]
    [string]$Target = '',
    [string]$VaultRoot = '',
    [switch]$InstallRuntime,
    [switch]$RegisterSchedule,
    [switch]$ForceConfig
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$home = $env:USERPROFILE

function Install-Skill {
    param([string]$Agent, [string]$Dest)
    $parent = Split-Path -Parent $Dest
    if ($parent -and -not (Test-Path $parent)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    if (Test-Path $Dest) {
        Remove-Item -Recurse -Force -LiteralPath $Dest
    }
    Copy-Item -Recurse -LiteralPath $ScriptDir -Destination $Dest -Force
    Write-Host "[ok] skill $Agent -> $Dest"
}

function Install-Runtime {
    $dest = Join-Path $home ".cursor\scripts\cursor-daily-log"
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    $scripts = Join-Path $ScriptDir "scripts"
    foreach ($f in @("capture.py", "run.ps1", "install-schedule.ps1")) {
        Copy-Item (Join-Path $scripts $f) (Join-Path $dest $f) -Force
    }
    Copy-Item (Join-Path $ScriptDir "config.example.json") (Join-Path $dest "config.example.json") -Force
    Copy-Item (Join-Path $ScriptDir "README.md") (Join-Path $dest "README.md") -Force -ErrorAction SilentlyContinue
    $cfg = Join-Path $dest "config.json"
    $example = Join-Path $dest "config.example.json"
    if ((-not (Test-Path $cfg)) -or $ForceConfig) {
        Copy-Item $example $cfg -Force
        Write-Host "[ok] wrote $cfg — edit vault_path / python_path"
    } else {
        Write-Host "[ok] kept existing $cfg"
    }
    Write-Host "[ok] runtime -> $dest"
}

if ($InstallRuntime -or $RegisterSchedule -or -not $Target) {
    if ($InstallRuntime -or -not $Target) {
        Install-Runtime
    }
}

if ($Target) {
    switch ($Target) {
        'cursor' {
            if (-not $VaultRoot) { throw "cursor requires -VaultRoot <path-to-vault>" }
            Install-Skill 'cursor (vault)' (Join-Path $VaultRoot '.cursor\skills\cursor-daily-log')
            Install-Skill 'cursor (global)' (Join-Path $home '.cursor\skills\cursor-daily-log')
        }
        'claude-code' {
            if ($VaultRoot) {
                Install-Skill 'claude-code (vault)' (Join-Path $VaultRoot '.claude\skills\cursor-daily-log')
            } else {
                Install-Skill 'claude-code (global)' (Join-Path $home '.claude\skills\cursor-daily-log')
            }
        }
        'opencode' {
            Install-Skill 'opencode' (Join-Path $home '.opencode\skills\cursor-daily-log')
        }
        'codex' {
            Install-Skill 'codex' (Join-Path $home '.codex\skills\cursor-daily-log')
        }
        'all' {
            Install-Skill 'opencode' (Join-Path $home '.opencode\skills\cursor-daily-log')
            Install-Skill 'codex' (Join-Path $home '.codex\skills\cursor-daily-log')
            Install-Skill 'claude-code (global)' (Join-Path $home '.claude\skills\cursor-daily-log')
            Install-Skill 'cursor (global)' (Join-Path $home '.cursor\skills\cursor-daily-log')
            if ($VaultRoot) {
                Install-Skill 'cursor (vault)' (Join-Path $VaultRoot '.cursor\skills\cursor-daily-log')
                Install-Skill 'claude-code (vault)' (Join-Path $VaultRoot '.claude\skills\cursor-daily-log')
            }
            Install-Runtime
        }
    }
}

if ($RegisterSchedule) {
    & (Join-Path $home ".cursor\scripts\cursor-daily-log\install-schedule.ps1")
}

Write-Host 'Done. Edit config.json under ~/.cursor/scripts/cursor-daily-log for vault/python paths.'
