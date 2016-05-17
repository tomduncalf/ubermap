# Ubermap Devices

## Summary

The Devices component of Ubermap allows easy customisation of device bank and parameter names displayed on Push for plugin devices, using simple configuration files for each device.

<img src="http://s32.postimg.org/osqe9c2dh/Screen_Shot_2016_05_05_at_21_43_23.png"/>

## Installation

Make sure you have a backup of anything important before starting, as I can't provide any technical support or be held resposible if anything goes wrong!

Note that ~ refers to your user folder (/Users/username).

To install, download the ZIP file from Github (https://github.com/tomduncalf/ubermap/archive/master.zip) and unzip it somewhere. Open the unzipped folder in Finder, go in to the Devices folder, and double click "install.command". This should open up a Terminal window with some install messages, followed by "Ubermap installed - now restart Ableton Live". You can now close/quit the Terminal window.

I also recommend creating an Options.txt file for Live to set it to always auto populate plugin parameters regardless of the number, see below for further explanation - to do this, copy the included Options.txt file to ~/Library/Preferences/Ableton/Live 9.6.2b1/, or edit your existing file and add the line "-_PluginAutoPopulateThreshold=-1".

### Push 1 users

If you are a Push 1 user, you need to update the Ubermap config to specify that you are using Push 1. Open "<your user directory>/Ubermap/global.cfg" and change "Version = 2" under "[Push]" to "Version = 1".

At this point you can (re-)start Ableton and the script should be working.

### Installation Notes

If you want to know what the install script is doing, you can look at install.command in a text editor, or read the manual instructions below - a brief summary: This will copy the appropriate files to "/Applications/Ableton Live 9.6 Beta.app/Contents/App-Resources/MIDI Remote Scripts", creating backups of the original pyc files in case you wish to remove the script - I'd recommend taking a full backup of the MIDI Remote Scripts folder just in case, however - and creates a folder called Ubermap in your user home directory, for device configs.

## Manual (Windows) Installation

To install the script manually (or on Windows - please note this has not been tested so use common sense and let me know of any errors!), do the following:

1. Backup your Live "MIDI Remote Scripts" folder
2. Create a new directory called Ubermap inside your Live "MIDI Remote Scripts" folder
3. Copy all the files from the unzipped Common folder (where you unzipped Ubermap) into the Ubermap folder you crated in step 2
4. Copy UbermapDevices.py and UbermapDevicesPatches.py from the unzipped Devices folder into the Ubermap folder you created in step 2
5. If you are using Push 1, copy `__init__.py` from the unzipped Push folder into the Push folder inside your Live "MIDI Remote Scripts" folder
6. If you are using Push 2, copy `__init__.py` from the unzipped Push2 folder into the Push2 folder inside your Live "MIDI Remote Scripts" folder
7. Delete or rename (for backup purposes) the following files in the Live "MIDI Remote Scripts" folder to make Live read the new Python files:
  - *.pyc inside the Ubermap folder (will only exist if you are upgrading)
  - If using Push 1, `__init__.pyc` inside the Push folder
  - If using Push 2, `__init__.pyc` inside the Push2 folder
8. Create a folder called Ubermap in your user folder (e.g. `C:\Users\Tom\Ubermap`)
9. Create a folder called Devices inside this Ubermap folder (e.g. `C:\Users\Tom\Ubermap\Devices`)
10. Copy all the files from the unzipped Config folder into the Ubermap folder you created in step 8
11. Create an `Options.txt` as described above (not sure where this should live on Windows)
12. (Re)start Live

## Summary

Ubermap works by intercepting the calls from Ableton to retrieve device parameters whenever a device is selected in Push, and first looking for a suitable parameter mapping file in ~/Ubermap/Devices and sending these parameters to Push, before falling back to the default Ableton mapping (as defined in Devices.py) if no enabled custom mapping is found.

This means you can redefine what parameters and parameter banks are shown on Push for any AU/VST device, including renaming parameters or banks and inserting blank spaces, letting you create a much more intuitive layout for 3rd party plugins. These mappings can be shared with other users by sharing the appropriate .cfg file with them.

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
    _blank_0 = ""
    _blank_1 = ""
    InternalParamName4 = Display Name 4

    [ParameterValues]
    InternalParamName1 = On, Off
    InternalParamName2 = Filter
    InternalParamName3 = Filter

    [ParameterValueTypes]
    Filter = Off||0, LP||0.25, HP||0.75

    [Config]
    Cache = False
    Ignore = False

### Parameter Banks

All visible parameters will by default be exported into the [Banks] section, split into banks of 8. You can then go in and rename banks, move parameters between, rename parameters (changing the part after the "=" to set the display name for a parameter) and insert blank spaces on the display (achieved by adding a line with an empty mapping: `_blank_0 = ""` – note that the same key (left hand name) cannot occur twice in a section, so you need to use e.g. `_blank_1`, `_blank_2`, if you want multiple blank spaces within a single bank).

Note that in 9.5+, it seems that the "Best Of" bank (which used to be the bank shown on Push when you select a device but don't go "in" to view all parameters) has been done away with, and instead the first bank is shown when you select but don't go "in to" a plugin device. To replicate this functionality in 9.5, set your device configuration file up so that the first bank you define has the controllers you want quick access to without going "in" to the device (you could call this bank "Best Of" and replicate the parameters in later banks if you like).

### Parameter Values (Push 2 only)

By default, device parameters are represented by a dial with a value from 0.0 to 1.0, but in reality, many parameters are not contiuous like this, but are instead discrete - for example an effect might be "on" or "off", a filter type might be "LP" or "BP" or "HP", or an oscillator wave might be "Sine", "Saw" or "Sub". Using a discrete parameter like this with a numerical dial is difficult as you would have to either remember that, for example, 0.2 corresponds to "BP", or you have to look at your computer's screen while changing the value. Some plugins can correctly describe their values (e.g. Waves IDR), in which case you see a list of parameters on the Push 2 screen instead of a number, but many do not, so you just see a number instead.

Ubermap 1.0.0 adds the ability to represent these kinds of parameters properly on Push 2 (not supported on Push 1 currently), by describing all the possible values of a parameter (and optionally, what numerical value corresponds to which actual value, if required) in the config file. The parameter is then still controlled with a knob, but rather than displaying a dial, it will display the proper value of the control e.g. "LP".

<img src="http://s32.postimg.org/t9x4tp7ut/image1.jpg" />

#### Simple example

This is easiest to explain with an example. Take the following simple device config:

```
[Banks]
[[Main]]
1_Filter Type = Filter Type
2_Filter Cutoff Frequency = Cutoff
```

We have two parameters, one of which we have renamed to "Cutoff". Imagine that in our plugin, "cutoff" is a continuous value, so it makes sense to use a knob for it; but "filter type" actually represents a switch with four states: "Off", "LP", "BP", "HP". With this config, you would still see "filter type" as a numerical dial – but as you turn the dial, you can see that a value of 0–0.25 corresponds to "Off", 0.25–0.5 corresponds to "LP", 0.5–0.75 corresponds to "BP" and 0.75–1.0 corresponds to "HP".

We can tell Ubermap that the "filter type" parameter behaves this way like so:

```
[Banks]
[[Main]]
1_Filter Type = Filter Type
2_Filter Cutoff Frequency = Cutoff

[ParameterValues]
1_Filter Type = Off, LP, BP, HP
```

We simply add an entry in the `ParameterValues` section, with the left hand side being the original parameter name as represented by Ubermap, and the right hand side being a comma-separated list of possible values. Ubermap will then automatically distribute those possible values over the range 0.0–1.0 (i.e. 0.0–0.25 = Off, 0.25–0.5 = LP, etc.), and on Push you will see "Off/LP/BP/HP" instead of a dial.

#### Parameters without even distribution

In some cases, you might find that a parameter is not evenly distributed over the range of 0.0–1.0 – for example, imagine that filter type actually responds like so:

* 0.0 – 0.1 = Off
* 0.1 – 0.4 = LP
* 0.4 – 0.6 = BP
* 0.6 – 1.0 = BP

This seems to be quite common in some plugins, so Ubermap provides a way to optionally tell it at which numerical value a given option starts, by using `||` after each possible value to separate the starting point from the name. For this example, we would therefore do:

```
[Banks]
[[Main]]
1_Filter Type = Filter Type
2_Filter Cutoff Frequency = Cutoff

[ParameterValues]
1_Filter Type = Off||0.0, LP||0.1, BP||0.4, HP||0.6
```

You can think of the `||` as saying "this parameter starts at", so for example, "Off" starts at 0.0, "LP" starts at 0.1, "BP" starts at 0.4 etc. To determine which numerical values correspond to which actual value, it's easiest to sweep the numerical dial and make a note of the value at each point that it changes – usually these correspond to regular intervals such as 1/3, 1/4, 1/8, but it's up to the plugin developer so there might be some weird ones!

#### Parameter value types

Imagine that our plugin actually has three identical filters, so the basic config actually looks like:

```
[Banks]
[[Main]]
1_Filter 1 Type = Filter 1 Type
2_Filter 1 Cutoff Frequency = Cutoff 1
3_Filter 2 Type = Filter 2 Type
4_Filter 2 Cutoff Frequency = Cutoff 3
5_Filter 3 Type = Filter 3 Type
6_Filter 3 Cutoff Frequency = Cutoff 3
```

We could just create a `ParameterValues` entry for each filter with an identical mapping like so:

```
[ParameterValues]
1_Filter 1 Type = Off||0.0, LP||0.1, BP||0.4, HP||0.6
3_Filter 2 Type = Off||0.0, LP||0.1, BP||0.4, HP||0.6
5_Filter 3 Type = Off||0.0, LP||0.1, BP||0.4, HP||0.6
```

However, it's useful to avoid duplication in configurations where possible. Instead, Ubermap lets us define a parameter value type in the `ParameterValueTypes` section, which describes how a certain type of parameter maps to actual values, and then we just say which parameters have that type. In this way, our final configuration without the duplication looks like:

```
[Banks]
[[Main]]
1_Filter 1 Type = Filter 1 Type
2_Filter 1 Cutoff Frequency = Cutoff 1
3_Filter 2 Type = Filter 2 Type
4_Filter 2 Cutoff Frequency = Cutoff 3
5_Filter 3 Type = Filter 3 Type
6_Filter 3 Cutoff Frequency = Cutoff 3

[ParameterValues]
1_Filter 1 Type = Filter
3_Filter 2 Type = Filter
5_Filter 3 Type = Filter

[ParameterValueTypes]
Filter = Off||0.0, LP||0.1, BP||0.4, HP||0.6
```

So here, we have defined a type called "Filter", which has the mapping for a filter knob, and then we just say that each of the filter type parameters is of type "Filter".

#### Examples

There are example configurations for D16 Devastor and TAL U-No-LX 2 included with Ubermap which make use of parameter values, so you can use these as a basis for other configurations.

### Config

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
- TAL U-No-LX 2

If they don't work, you might have a different set of parameters exposed and therefore a different hash (see below) to me, in which case you can try just copying the contents of the example into your generated config file (see below again).

Note that these haven't been updated for or tested with 9.5 yet.

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

