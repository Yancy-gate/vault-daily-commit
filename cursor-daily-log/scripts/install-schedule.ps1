# Install / refresh Windows scheduled task for evening capture (default 21:00).
$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Cfg = Get-Content (Join-Path $ScriptDir "config.json") -Raw -Encoding UTF8 | ConvertFrom-Json
$Hour = [int]$Cfg.evening_hour
$Minute = [int]$Cfg.evening_minute
$RunPs1 = Join-Path $ScriptDir "run.ps1"
$TaskName = "CursorDailyLogToObsidian"

$Time = "{0:D2}:{1:D2}" -f $Hour, $Minute
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$RunPs1`""
$Trigger = New-ScheduledTaskTrigger -Daily -At $Time
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Principal $Principal -Force | Out-Null

Write-Host "Scheduled task '$TaskName' set for daily $Time"
Get-ScheduledTask -TaskName $TaskName | Format-List TaskName, State
