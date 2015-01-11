#!/bin/bash

cd "$(dirname "$0")"

function cp_if_ne {
    if [ ! -f "$2" ]
        then
        echo "Backing up file $1"
        cp "$1" "$2"
    fi
}

LIVE_MIDI_REMOTE_PATH="/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts"

# Backup
cp_if_ne "$LIVE_MIDI_REMOTE_PATH/Push/BrowserComponent.pyc" "$LIVE_MIDI_REMOTE_PATH/Push/BrowserComponent.pyc.ubermap-backup"

# Copy
mkdir -p "$LIVE_MIDI_REMOTE_PATH/Ubermap"
cp ../Common/__init__.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp ../Common/configobj.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp ../Common/UbermapLibs.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp UbermapBrowser.py "$LIVE_MIDI_REMOTE_PATH/Ubermap/"
cp BrowserComponent.py "$LIVE_MIDI_REMOTE_PATH/Push/"

# Copy config
mkdir -p ~/Ubermap/Devices
cp_if_ne ../Config/browser.cfg ~/Ubermap/
cp_if_ne ../Config/global.cfg ~/Ubermap/

# Remove .pyc
rm "$LIVE_MIDI_REMOTE_PATH/Ubermap/*.pyc"
rm "$LIVE_MIDI_REMOTE_PATH/Push/BrowserComponent.pyc"

echo "Ubermap installed - now restart Ableton Live."
