##############################################################################################
# Windows 10 / WIndows 11 PowerShell install script                                          #
# Paths may differ from the defaults used in this script and may be adjusted                 #
##############################################################################################
$LIVE_MIDI_REMOTE_PATH = "C:\ProgramData\Ableton\Live 11 Suite\Resources\MIDI Remote Scripts"

# Backup Existing Midi Remote Folder
# Copy-Item $LIVE_MIDI_REMOTE_PATH -Destination $LIVE_MIDI_REMOTE_PATH" ORIG" -Recurse

# Copy
$UBERMAP_MIDI_REMOTE_PATH = $LIVE_MIDI_REMOTE_PATH + '/Ubermap'
New-Item -Path $UBERMAP_MIDI_REMOTE_PATH -ItemType "directory" -Force
Copy-Item ../Common/__init__.py -Destination $UBERMAP_MIDI_REMOTE_PATH -Force
Copy-Item ../Common/configobj.py -Destination $UBERMAP_MIDI_REMOTE_PATH -Force
Copy-Item ../Common/UbermapLibs.py -Destination $UBERMAP_MIDI_REMOTE_PATH -Force
Copy-Item UbermapDevices.py -Destination $UBERMAP_MIDI_REMOTE_PATH -Force
Copy-Item UbermapDevicesPatches.py -Destination $UBERMAP_MIDI_REMOTE_PATH -Force

# Copy config
$UBERMAP_USER = $HOME + '/Ubermap'
New-Item -Path $UBERMAP_USER -ItemType "directory" -Force
New-Item -Path $UBERMAP_USER"/Devices" -ItemType "directory" -Force
Copy-Item ..\Config\devices.cfg -Destination $UBERMAP_USER -Force
Copy-Item ..\Config\global.cfg -Destination $UBERMAP_USER -Force
Copy-Item ..\Config\browser.cfg -Destination $UBERMAP_USER -Force

# PluginAutoPopulateThreshold Setting
$SETTINGS_FOLDER_SEARCH = $HOME + '\AppData\Roaming\Ableton'
$LIVE_VERSION_FOLDER_NAME = (Get-ChildItem $SETTINGS_FOLDER_SEARCH | Where-Object {$_.name -match "Live .[0-9.]"} | Sort-Object | Select-Object -Last 1).Name
$OPTIONS_FILE = $HOME + '\AppData\Roaming\Ableton\' + $LIVE_VERSION_FOLDER_NAME + '\Preferences\Options.txt'

$SETTING = "-_PluginAutoPopulateThreshold=-1"
if(!(Test-path $OPTIONS_FILE))
{
    $SETTING | Out-File $OPTIONS_FILE
} else {
    $contains = Select-String -Path $OPTIONS_FILE "-_PluginAutoPopulateThreshold"

    if ($null -eq $contains)
    {
        Add-Content $OPTIONS_FILE $SETTING
    }
}

# Remove .pyc
Get-ChildItem -Path $LIVE_MIDI_REMOTE_PATH"/Ubermap" *.pyc | ForEach-Object { Remove-Item -Path $_.FullName }

Write-Output 'Ubermap installed - now restart Ableton Live.'
Read-Host 'Press ENTER to close...'