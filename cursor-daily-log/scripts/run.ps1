# Capture today's Cursor Agent sessions into Obsidian.
# Designed for Task Scheduler (-NoProfile): do NOT rely on interactive PATH.
param(
    [string]$Date = "",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PyScript = Join-Path $ScriptDir "capture.py"
$LogDir = Join-Path $ScriptDir "logs"
$LogFile = Join-Path $LogDir ("run-{0}.log" -f (Get-Date -Format "yyyy-MM-dd"))

function Write-RunLog([string]$Message) {
    if (-not (Test-Path $LogDir)) {
        New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
    }
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    Add-Content -Path $LogFile -Value $line -Encoding UTF8
}

function Resolve-PythonExe {
    $cfgPath = Join-Path $ScriptDir "config.json"
    if (Test-Path $cfgPath) {
        $cfg = Get-Content $cfgPath -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($cfg.python_path -and (Test-Path $cfg.python_path)) {
            return $cfg.python_path
        }
    }

    $candidates = @(
        (Join-Path $env:USERPROFILE "anaconda3\python.exe"),
        (Join-Path $env:USERPROFILE "miniconda3\python.exe"),
        (Join-Path $env:LOCALAPPDATA "Programs\Python\Python313\python.exe"),
        (Join-Path $env:LOCALAPPDATA "Programs\Python\Python312\python.exe"),
        (Join-Path $env:LOCALAPPDATA "Programs\Python\Python311\python.exe")
    )
    foreach ($c in $candidates) {
        if ($c -and (Test-Path $c)) { return $c }
    }

    # Last resort: merge User+Machine PATH (Task Scheduler often omits them)
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $env:Path = @($machinePath, $userPath, $env:Path) -join ";"
    $cmd = Get-Command python.exe -ErrorAction SilentlyContinue
    if ($cmd -and $cmd.Source -and (Test-Path $cmd.Source)) {
        return $cmd.Source
    }
    return $null
}

try {
    $Python = Resolve-PythonExe
    if (-not $Python) {
        Write-RunLog "ERROR: python.exe not found. Set config.json python_path."
        Write-Error "python.exe not found. Edit config.json python_path to your Anaconda/Python install."
        exit 9009
    }

    $argsList = @($PyScript)
    if ($Date) { $argsList += @("--date", $Date) }
    if ($DryRun) { $argsList += "--dry-run" }

    Write-RunLog "START python=$Python args=$($argsList -join ' ')"
    & $Python @argsList
    $code = $LASTEXITCODE
    if ($null -eq $code) { $code = 0 }
    Write-RunLog "END exit=$code"
    exit $code
}
catch {
    Write-RunLog "ERROR: $($_.Exception.Message)"
    throw
}
