param(
    [ValidateSet('cursor', 'claude-code', 'opencode', 'codex', 'all')]
    [string]$Target = 'all',
    [string]$VaultRoot = ''
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

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
    Write-Host "[ok] $Agent -> $Dest"
}

$home = $env:USERPROFILE

switch ($Target) {
    'cursor' {
        if (-not $VaultRoot) { throw "cursor requires -VaultRoot <path-to-vault>" }
        Install-Skill 'cursor (vault)' (Join-Path $VaultRoot '.cursor\skills\vault-daily-commit')
    }
    'claude-code' {
        if ($VaultRoot) {
            Install-Skill 'claude-code (vault)' (Join-Path $VaultRoot '.claude\skills\vault-daily-commit')
        } else {
            Install-Skill 'claude-code (global)' (Join-Path $home '.claude\skills\vault-daily-commit')
        }
    }
    'opencode' {
        Install-Skill 'opencode' (Join-Path $home '.opencode\skills\vault-daily-commit')
    }
    'codex' {
        Install-Skill 'codex' (Join-Path $home '.codex\skills\vault-daily-commit')
    }
    'all' {
        Install-Skill 'opencode' (Join-Path $home '.opencode\skills\vault-daily-commit')
        Install-Skill 'codex' (Join-Path $home '.codex\skills\vault-daily-commit')
        Install-Skill 'claude-code (global)' (Join-Path $home '.claude\skills\vault-daily-commit')
        if ($VaultRoot) {
            Install-Skill 'cursor (vault)' (Join-Path $VaultRoot '.cursor\skills\vault-daily-commit')
            Install-Skill 'claude-code (vault)' (Join-Path $VaultRoot '.claude\skills\vault-daily-commit')
        }
        Write-Host 'Tip: pass -VaultRoot to also install cursor/claude-code project skills'
    }
}

Write-Host 'Done. Edit vault-config.md in the installed copy for your paths.'
