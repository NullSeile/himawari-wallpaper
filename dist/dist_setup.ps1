$action = New-ScheduledTaskAction -Execute "$PSScriptRoot\dist_invoke.vbs"

$RepetitionPattern = Get-CimClass `
    -Namespace Root/Microsoft/Windows/TaskScheduler `
    -ClassName MSFT_TaskRepetitionPattern

$R = New-CimInstance `
    -CimClass $RepetitionPattern `
    -Property @{Interval = 'PT10M' } `
    -ClientOnly

$trigger = New-ScheduledTaskTrigger -AtLogOn
$trigger.Repetition = $R

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -ExecutionTimeLimit (New-TimeSpan -Seconds 0)

Register-ScheduledTask -Force -TaskName  "HimawariWallpaperDist" -Trigger $trigger -Action $action -Settings $settings