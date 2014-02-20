#!/bin/bash

function cp_if_ne {
    if [ ! -f "$2" ] 
        then
        echo "Backing up file $1"
        cp "$1" "$2"
    fi
}

LIVE_MIDI_REMOTE_PATH="/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts"

cd ${0%/*}

# Backup
cp_if_ne "$LIVE_MIDI_REMOTE_PATH/_Generic/Devices.pyc" "$LIVE_MIDI_REMOTE_PATH/_Generic/Devices.pyc.ubermap-backup" 
cp_if_ne "$LIVE_MIDI_REMOTE_PATH/Push/DeviceParameterComponent.pyc" "$LIVE_MIDI_REMOTE_PATH/Push/DeviceParameterComponent.pyc.ubermap-backup" 

# Copy
mkdir -p "$LIVE_MIDI_REMOTE_PATH/Ubermap"
cp ../Common/__init__.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp ../Common/configobj.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp ../Common/UbermapLibs.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp UbermapDevices.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp Devices.py "$LIVE_MIDI_REMOTE_PATH/_Generic/"
cp DeviceParameterComponent.py "$LIVE_MIDI_REMOTE_PATH/Push/"

# Copy config
mkdir -p ~/Ubermap/Devices
cp_if_ne ../Config/devices.cfg ~/Ubermap/
cp_if_ne ../Config/global.cfg ~/Ubermap/

# Remove .pyc
rm "$LIVE_MIDI_REMOTE_PATH/Ubermap/*.pyc"
rm "$LIVE_MIDI_REMOTE_PATH/_Generic/Devices.pyc"
rm "$LIVE_MIDI_REMOTE_PATH/Push/DeviceParameterComponent.pyc"

echo "Ubermap installed - now restart Ableton Live."

