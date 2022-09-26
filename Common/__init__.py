# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/__init__.py
from __future__ import absolute_import, print_function

from . import UbermapDevicesPatches

def create_instance(c_instance):
    UbermapDevicesPatches.apply_ubermap_patches()
