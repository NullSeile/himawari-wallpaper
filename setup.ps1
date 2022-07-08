$action = New-ScheduledTaskAction -Execute "$PSScriptRoot/invoke.vbs"

$RepetitionPattern = Get-CimClass `
    -Namespace Root/Microsoft/Windows/TaskScheduler `
    -ClassName MSFT_TaskRepetitionPattern

$R = New-CimInstance `
    -CimClass $RepetitionPattern `
    -Property @{Interval = 'PT5M'} `
    -ClientOnly

$trigger = New-ScheduledTaskTrigger -AtLogOn
$trigger.Repetition = $R

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -ExecutionTimeLimit (New-TimeSpan -Seconds 0)

Register-ScheduledTask -Force -TaskName  "HimawariWallpaper" -Trigger $trigger -Action $action -Settings $settings