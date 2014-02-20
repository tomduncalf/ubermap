# Ubermap v0.1 alpha

## Introduction

Ubermap is a set of modifications to Ableton Live to add new functionality to Ableton, particularly aimed at Push users.

Features:

- Easy customisation of device bank and parameter names displayed on Push, for both internal and plugin devices, using simple configuration files for each device
- Modify configurations instantly without reloading Live
- More cool stuff coming soon :)

## Disclaimer

This alpha release is intended only for advanced users who are willing to risk things breaking, and is not production ready. It hasn't been tested on any machines other than my own, so might not work at all or might do something really bad :)

This script changes your Ableton MIDI Remote configs, and could introduce instability or potentially even data corruption, so please do not use it on your main machine and ensure you have backups of all your data before using.

The author cannot be help responsible for any harm or damage resulting from the use of the software.

## Licence

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License (http://creativecommons.org/licenses/by-nc/4.0/deed.en_US)

## Compatibility

Ubermap requires Ableton Live 9.1.1 and a Mac. I've tried getting it up and running on Windows briefly without luck (Ableton crashed every time I loaded it), for now it's Mac only but I do intend to support Windows at some point - although you are welcome to try and get it up and running yourself.

## Installation

I've made the installation a bit simpler as the script seems to work OK for others but please still make sure you understand what the script is doing and how to use it (and any potential risks associated with doing so), as I can't provide any technical support or be held resposible if anything goes wrong! Make sure you have a backup of anything important :)

Note that ~ refers to your user folder (/Users/username).

To install, download the ZIP file from Github (https://github.com/tomduncalf/ubermap/archive/master.zip) and unzip it somewhere. Open the unzipped folder in Finder, go in to the Devices folder, and double click "install.command". This should open up a Terminal window with some install messages, followed by "Ubermap installed - now restart Ableton Live". You can now close/quit the Terminal window.

I also recommend creating an Options.txt file for Live to set it to always auto populate plugin parameters regardless of the number, see below for further explanation - to do this, copy the included Options.txt file to ~/Library/Preferences/Ableton/Live 9.1.1/, or edit your existing file and add the line "-_PluginAutoPopulateThreshold=-1".

At this point you can (re-)start Ableton and the script should be working.

### Installation Notes

Note that my Devices.py also includes the improved default mappings by TomViolenz and other contributors on the Ableton forum - see https://forum.ableton.com/viewtopic.php?f=55&t=198946&p=1562395#p1562395.

If you want to know what the install script is doing, you can look at install.command in a text editor, or read the manual instructions below - a brief summary: This will copy the appropriate files to "/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts", creating backups of the original pyc files in case you wish to remove the script - I'd recommend taking a full backup of the MIDI Remote Scripts folder just in case, however - and creates a folder called Ubermap in your user home directory, for device configs.

## Manual (Windows) Installation 

To install the script manually (or on Windows - please note this has not been tested so use common sense and let me know of any errors!), do the following:

1. Backup your Live Remote MIDI Scripts folder
2. Create a new directory called Ubermap inside your Live Remote MIDI Scripts folder
3. Copy all the files from the unzipped Common folder (where you unzipped Ubermap) into the Ubermap folder you crated in step 2
4. Copy UbermapDevices.py from the unzipped Devices folder into the Ubermap folder you created in step 2
5. Copy Devices.py from the unzipped Devices folder to the _Generic folder in your Live Remote MIDI Scripts folder
6. Copy DeviceParameterComponent.py from the unzipped Devices folder to the Push folder in your Live Remote MIDI Scripts folder
7. Delete or rename (for backup purposes) the following files to make Live read the new Python files:
  - *.pyc inside the Ubermap folder (will only exist if you are upgrading)
  - Devices.pyc inside the _Generic folder
  - DeviceParameterComponent.pyc inside the Push folder
8. Create a folder called Ubermap in your user folder (e.g. C:\Users\Tom\Ubermap)
9. Create a folder called Devices inside this Ubermap folder (e.g. C:\Users\Tom\Ubermap\Devices)
10. Copy all the files from the unzipped Config folder into the Ubermap folder you created in step 8
11. Create an Options.txt as described above (not sure where this should live on Windows)
12. (Re)start Live

## Summary

Ubermap works by intercepting the calls from Ableton to retrieve device parameters whenever a device is selected in Push, and first looking for a suitable parameter mapping file in ~/Ubermap/Devices and sending these parameters to Push, before falling back to the default Ableton mapping (as defined in Devices.py) if no enabled custom mapping is found.

This means you can redefine what parameters and parameter banks are shown on Push for any device (internal or AU/VST), including renaming parameters or banks and inserting blank spaces, letting you create a much more intuitive layout for 3rd party plugins in particular. These mappings can be shared with other users by sharing the appropriate .cfg file with them.

To create an initial mapping, we need to know what parameters a device presents to Live - luckily, Ubermap will automatically export a new configuration file for any device it hasn't seen before, containing a list of all the parameters, split into banks of 8, making customisation much easier. 

## Configuration file details

Device configuration files are exported to and loaded from ~/Ubermap/Devices, with filenames in the format: "Device Name_HASH.cfg". See below for information about the HASH part of the filename.

Configuration files are formatted using something resembling the ini file format, and look like:

    [Banks]
    [[Bank Name 1]]
    InternalParamName1 = Display Name 1
    InternalParamName2 = Display Name 2
    [[Bank Name 2]]
    InternalParamName3 = Display Name 3
    "" = ""
    InternalParamName4 = Display Name 4
    [BestOfBank]
    [[Bank]]
    InternalParamName1 = Best of Param Name 1
    InternalParamName4 = Best of Param Name 2
    [Config]
    Cache = False
    Ignore = False 

All visible parameters will by default be exported into the [Banks] section, split into banks of 8. You can then go in and rename banks, move parameters between, rename parameters (changing the part after the "=" to set the display name for a parameter) and insert blank spaces on the display (achieved by adding a line with an empty mapping: "" = "").

The [BestOfBank] section contains a single bank, which is the "best of" bank shown on Push when you select a device but don't go "in" to view all parameters. This is populated with the first 8 parameters in the default export, but you can reference whichever parameters you want in here by copying the name from the [Banks] section, creating a more useful top level mapping.

The [Config] section is for Ubermap config - for now, the "Cache" parameter doesn't do anything (this will probably be removed, as all config files are now cached based on modified time, so any changes you make are reflected as soon as you save the file and reselect the device on Push).

The "Ignore" parameter is set to "True" by default when a new device is exported - this means that Ubermap will ignore the configuration file, and instead use Ableton's default mapping. If you are creating a custom mapping for a device, you'll want to set this to "False", or else the config will be ignored :)

## Example usage

Here's a quick example of how you would use Ubermap to map a new device:

1. Add the device to your Live set and select it so its default mapping is displayed on Push - this will cause Ubermap to export the default mapping configuration file for the device.
2. Go to the ~/Ubermap/Devices directory, locate the configuration file for the device in question (e.g. LuSH-101_<hash>.cfg) and open it in a text editor (I recommend Sublime Text).
3. Modify the parameters in the [Banks] section, splitting them into appropriately named banks and moving, renaming and deleting parameters as desired.
4. Modify the parameters in the [BestOfBank] section, selecting up to 8 parameters you want to display in the "best of" bank.
5. Change "Ignore = True" to "Ignore = False" in the [Config] section.
6. Save your changes to the config file.
7. Select a different device and then select the device you are mapping again - the config will be reloaded and you should see your new mapping. If you're not happy with it, you can continue editing, saving and reselecting the device until you get it right.

## Example device configurations

Example configurations for a few devices are included in the Example Configs directory to give an idea of what can be done - if you want to use any of these, copy them to ~/Ubermap/Devices. If you have the plugin auto populate threshold set correctly in Options.txt and the same plugin version as I do, they should be picked up, although I've not been able to test this with anyone :) 

Included example device mappings are:

- D16 Devastor
- D16 Drumazon
- D16 LuSH-101 (requires loading my parameter mapping, included in the "Plugin Parameter Mappings" directory)
- D16 Toraverb
- FabFilter Timeless 2
- FXpansion Cypher
- FXpansion Strobe
- Maradona Labs Aalto (unfinished mapping)
- ML-185 step sequencer (Max MIDI Effect_86742a9aa7c78617f94e80f3ce65d488.cfg)
- NI Monark (Reaktor5_9c1425c4d9e6878ca148439e91cd63a6.cfg)

If they don't work, you might have a different set of parameters exposed and therefore a different hash (see below) to me, in which case you can try just copying the contents of the example into your generated config file (see below again).

## FAQs

### Why is there a hash in the filename?

The hash is an md5 hash of all the parameter names the device presents to Live, in the order they are presented. What this means in real terms is that there can be multiple mappings present for the same device, if the device has been loaded with a different set (or order) of parameters exposed (in the "Configure" section of the device) each time. 

The primary reason for adding this hash was so that different Reaktor and Max devices can be individually mapped - as they all run inside the same host device/plguin, the device name is always seen as "Reaktor" or e.g. "Max MIDI Effect", but each device presents a different set of automatable parameters and so can be uniquely identified this way. 

### Why do I need to change the plugin auto populate threshold?

It is recommended to set Ableton's plugin parameter auto population threshold as high as possible for several reasons:

- This ensures the exported intial mapping file contains all available device parameters (parameters can be removed from the mapping file if you do not wish to see them on Push)
- This should help ensure that different users create the same hash for the same plugin, enabling easier sharing of configs
- This helps with unique identification of things like Reaktor devices
- Finally, at the minute if you change the configured plugin parameters, Ubermap will create a new config file for every change you make and you'll end up with hundreds of generated config files to clean up ;) (this will be fixed in future)

### How do I determine a device's configuration filename?

Normally, it should be easy to figure out which configuration file relates to a device, as the device name is at the start of the filename. However, in the case of Reaktor/Max devices, there might be multiple devices with the same name but different hashes, it might be a bit harder to work out which one corresponds to what.

In this case, you can either open each of the files up and look at the parameters to work out which one looks like the device you are interested in, or you can look in the Ubermap log file, which is located in ~/Ubermap/main.log - if you select the device you are interested in, then look at the log file, it should be the at the bottom of the file, in a line like:

    INFO load config name: Scale_c0888f8a7d74998b5867d2a2fff78034, path: /Users/xxx/Ubermap/Devices/Scale_c0888f8a7d74998b5867d2a2fff78034.cfg, subdir: Devices


### My device mapping isn't being loaded!

Have you changed "Ignore = True" to "Ignore = False" in the config file? If so, maybe you have an error in your configuration. Take a look at ~/Ubermap/main.log if you're feeling brave, or post in the thread on the Ableton forum.

## Support

For support, please ask in the thread on the Ableton forum - I can't offer any guarantees of support but will try and help.
