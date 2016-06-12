# Ubermap v1.0.0b2 [![PayPal donate button](https://img.shields.io/badge/paypal-donate-yellowgreen.svg)](https://www.paypal.me/tomduncalf/10)

## Introduction

Ubermap is a script for Ableton Live to allow Push users to create custom parameter mappings for VST and AU plugins on the Push display.

Features:

- Easy customisation of device bank and parameter names displayed on Push for devices, using simple configuration files
- Modify configurations instantly without reloading Live

## For more information, [see the main README](https://github.com/tomduncalf/ubermap/blob/master/Devices/README.md) and [the thread on the Ableton forum](https://forum.ableton.com/viewtopic.php?f=55&t=221501&sid=f8b1a012a123a51a16838c8698a28b8a)

## Disclaimer

This alpha release is intended only for advanced users who are willing to risk things breaking, and is not production ready. It hasn't been tested on any machines other than my own, so might not work at all or might do something really bad :)

This script changes your Ableton MIDI Remote configs, and could introduce instability or potentially even data corruption, so please do not use it on your main machine and ensure you have backups of all your data before using.

The author cannot be help responsible for any harm or damage resulting from the use of the software.

## Licence

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License 

## Logging

Ubermap components log to ~/Ubermap/main.log, and the log level is controlled by the settings in ~/Ubermap/global.cfg. Debug logging is turned off by default, as it is very verbose, info logging is turned on, and error logging cannot be disabled. The log file is wiped out each time the script restarts (e.g. when restarting Ableton) so shouldn't grow to be massive.

## Support

For support, please ask in the thread on the Ableton forum - I can't offer any guarantees of support but will try and help.
