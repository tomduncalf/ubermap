# Ubermap Browser Preview

## Summary

The Browser Preview component of Ubermap adds the ability to preview audio samples (WAV/AIFF) in a Drum Rack when scrolling through them in "Browse" mode on Push before loading, just like you can on Maschine. Seems crazy that this isn't part of Push already, but there you go!

This component should be considered a very alpha release at the minute, and Mac only - the way it is implemented is quite hacky, there is a risk of instability, and it's not been very well tested at all, so certainly don't install it on your main production or live rig. The worst case scenario should be that you just restore a backup of your MIDI Remote Scripts, or re-install Ableton, but as always I can accept no responsibility for any bad things that may happen when using Ubermap!

This README is quite sparse for now, more information will be added at some point in the future.

## Installation

Installation is similar to the Devices component:

Note that ~ refers to your user folder (/Users/username). Also note that you should back up your ~/Ubermap/browser.cfg file before upgrading as the installation may wipe out your config.

To install, download the ZIP file from Github (https://github.com/tomduncalf/ubermap/archive/master.zip) and unzip it somewhere. Open the unzipped folder in Finder, go in to the BrowserPreview folder, and double click "install.command". This should open up a Terminal window with some install messages, followed by "Ubermap installed - now restart Ableton Live". You can now close/quit the Terminal window.

If you are a Windows user and feeling experimental, you should be able to work out manual install instructions based on the script and the notes in the Devices README.

## Summary

The Browser Preview component works by intercepting whatever file you highlight when in browse mode on Push, and if that file looks like an audio file, it will check if the top level folder (actually the name of the folder as shown in the "Places" browser bar) of the file exists in a mapping of Places folders to disk location in the Ubermap config. If it does, then it will try and play that file using an external audio player (by default, /usr/bin/afplay, which is a very basic command line audio player installed on every Mac, which will play the sound through the default output).

This actually works quite well, but does currently require you to manually specify the disk location of each "place" in your browser.

## Configuration file details

The configuration file for this component is at ~/Ubermap/browser.cfg, and has the following top level options:

- enabled (True/False): If set to False, samples will never be previewed.
- audio_formats (List): A list of file extensions that we should try to preview
- player_bin (String): The path to the executable file to use to play the audio file - Windows users can try finding a suitable substitute for afplay and adding it here
- kill_player (True/False): Whether to kill the preview player task when previewing a new sound or not. If set to False, every sound will play to the end with no way to stop it, which can be pretty annoying with long sounds! Setting to True will prevent this, in exchange for the odd click when cutting a sound short.

The LibraryPaths section is where you must configure the mapping from "Places" in your browser to their location on disk, and contains a couple of examples that can safely be removed. Each line has the format:

Place Name = "/Path/On/Disk/"

The forward slash at the end is important, the order of places is not, and place names need to be unique - if you have two with the same name, you'll need to rename one if you want to be able to preview both.

## Usage

After configuring your library paths to match the places you have configured in your browser, you should be able to preview samples by dropping in a Drum Rack, selecting a pad with Push, selecting the pad ("EmptyPad" by default) in "Device" view, then pushing Browse. Navigate to one of your configured places (scroll all the way down to Places in column 1, then select one in column 2), and then when you scroll the end column to an audio file, you should hear a preview through your system's default audio ouptut.

If you want to change where the preview comes out of, you will need to change your system default output - on a Mac, you can Alt-Click the volume icon in the top right to get a list of available outputs.

## Troubleshooting

If you don't hear a preview, chances are the library path is set up wrong. Open up ~/Ubermap/main.log in a text editor and look at the bottom for lines like "ERROR: file /Users/Shared/Battery 4 Factory Library/Drums/Kick/Kick 606X 1.wav not found" - if you see errors like this, check that the path actually exists.

If this isn't the issue, check that "enabled" is set to true in browser.cfg, and if that still isn't the issue, try playing the audio file with afplay manually: open a terminal and type e.g.: afplay /Users/Shared/Battery 4 Factory Library/Drums/Kick/Kick 606X 1.wav - if there is no sound from this, check your audio outputs.

If it still doesn't work, give me a shout on the Ableton forum :)

## Known Issues

- I've seen Push "restart" itself a coupe of times while using this script, not sure if it is related to this script or some other one. It only interrupts for a minute but obviously not ideal! It's certainly possible that there is a bug or memory leak in it, as the Push source file that has been modified (BrowserComponent.py) did not decompile cleanly and required some manual fixing, so there could easily be a subtle bug introduced by that.

## Future Plans

- It's annoying having your places right at the bottom of the list in Browse, so I might move them to the top.
- Create a tool to automatically build up the LibraryPaths - I tried to find a way to get this via the LiveAPI but it doesn't seem to be exposed, but it should be possible to look at the Ableton Library.cfg instead.
- It would be great if the previews played through Live, rather than a separate application. I was thinking you could maybe do this by communicating with a special M4L device on a channel mapped to the cue output, but I'm hoping Ableton implement this feature properly themselves before it comes to that ;)
