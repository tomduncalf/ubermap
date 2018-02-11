# WARNING : for live 10 version

Need to pach file MIDI Remote Scripts\Push2\model\repr.pyc for method DeviceParameterAdapter._get_image_filenames line 173 :

                except (AttributeError, RuntimeError):
=> shoud be :

                except (AttributeError, RuntimeError, ArgumentError):

This should be done adding a new method in apply_ubermap_patches()

# Ubermap v0.1 alpha

## Introduction

Ubermap is a set of modifications to Ableton Live to add new functionality to Ableton, particularly aimed at Push users.

Features:

- Easy customisation of device bank and parameter names displayed on Push, for both internal and plugin devices, using simple configuration files for each device
- Modify configurations instantly without reloading Live

For information on installing and using each feature, please read the README.md in the relevant directory (BrowserPreview or Devices) - each component can be installed separately.

## Disclaimer

This alpha release is intended only for advanced users who are willing to risk things breaking, and is not production ready. It hasn't been tested on any machines other than my own, so might not work at all or might do something really bad :)

This script changes your Ableton MIDI Remote configs, and could introduce instability or potentially even data corruption, so please do not use it on your main machine and ensure you have backups of all your data before using.

The author cannot be help responsible for any harm or damage resulting from the use of the software.

## Licence

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License (http://creativecommons.org/licenses/by-nc/4.0/deed.en_US)

## Compatibility

Ubermap requires Ableton Live 9.5.1beta4 and a Mac. I've tried getting it up and running on Windows briefly without luck (Ableton crashed every time I loaded it), for now it's Mac only but I do intend to support Windows at some point - although you are welcome to try and get it up and running yourself.

## Installation

Installation notes are contained in the individual README.md files, but one thing to note is that as the core Ubermap libs are shared, if you upgrade (i.e. reinstall over the top of the old version) one component to a new release of Ubermap, you should also upgrade the others, as the shared libraries may have changed, making the old component incompatible.

I'll consider fixing this in a better way (e.g. have the libs contained in each component) in future if there is demand.

## Logging

Ubermap components log to ~/Ubermap/main.log, and the log level is controlled by the settings in ~/Ubermap/global.cfg. Debug logging is turned off by default, as it is very verbose, info logging is turned on, and error logging cannot be disabled. The log file is wiped out each time the script restarts (e.g. when restarting Ableton) so shouldn't grow to be massive.

## Support

For support, please ask in the thread on the Ableton forum - I can't offer any guarantees of support but will try and help.
