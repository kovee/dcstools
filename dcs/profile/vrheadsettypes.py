## ============================================================================
##                       ---=== DCS:World Tools ===---
##                  Copyright (C) 2021-2022, Attila Kovacs
## ============================================================================
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to
## deal in the Software without restriction, including without limitation the
## rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
## sell copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
## IN THE SOFTWARE.
##
## ============================================================================

"""Contains the implementation of the VRHeadsetTypes enum."""

# Runtime Imports
from enum import IntEnum, auto

class VRHeadsetTypes(IntEnum):

    """List of supported VR headset types."""

    VR_HEADSET_NONE = auto()
    """Default value, represents no headset in use."""

    VR_HEADSET_GENERIC = auto()
    """Represents a generic VR headset."""

    VR_HEADSET_PSVR = auto()
    """Represents the Playstation VR headset.
    Resolution (per eye): 960x1080
    Refresh rate: 90-120 Hz
    """

    VR_HEADSET_RIFT = auto()
    """Represents the Occulus Rift VR headset.
    Resolution (per eye): 1080x1200
    Refresh rate: 80 Hz
    """

    VR_HEADSET_RIFT_S = auto()
    """Represents the Occulus Rift S VR headset.
    Resolution (per eye): 1280x1440
    Refresh rate: 80 Hz
    """

    VR_HEADSET_QUEST = auto()
    """Represents the Occulus Quest VR headset.
    Resolution (per eye): 1440x1600
    Refresh rate: 72 Hz
    """

    VR_HEADSET_QUEST_2 = auto()
    """Represents the Occulus Quest 2 VR headset.
    Resolution (per eye): 1832x1920
    Refresh rate: 120 Hz
    """

    VR_HEADSET_INDEX = auto()
    """Represents the Valve Index VR headset.
    Resolution (per eye): 1600x1440
    Refresh rate: 120 Hz
    """

    VR_HEADSET_HTC_VIVE = auto()
    """Represents the HTC Vive VR headset.
    Resolution (per eye): 1080x1200
    Refresh rate: 90 Hz
    """

    VR_HEADSET_HTC_VIVE_PRO = auto()
    """Represents the HTC Vive Pro VR headset.
    Resolution (per eye): 1440x1600
    Refresh rate: 90 Hz
    """

    VR_HEADSET_ODYSSEY = auto()
    """Represents the Samsung Odyssey VR headset.
    Resolution (per eye): 1440x1600
    Refresh rate: 90 Hz
    """

    VR_HEADSET_REVERB = auto()
    """Represents the HP Reverb G1 VR headset.
    Resolution (per eye): 2160x2160
    Refresh rate: 90 Hz
    """

    VR_HEADSET_REVERB_G2 = auto()
    """Represents the HP Reverb G2 VR headset.
    Resolution (per eye): 2160x2160
    Refresh rate: 90 Hz
    """

    VR_HEADSET_PRIMAX_4K = auto()
    """Represents the Primax 4K VR headset.
    Resolution (per eye): 1920x2160
    Refresh rate: 60 Hz
    """

    VR_HEADSET_PRIMAX_5K_SUPER = auto()
    """Represents the Primax 5K Super VR headset.
    Resolution (per eye): 2560x1440
    Refresh rate: 90 Hz
    """

    VR_HEADSET_PRIMAX_5K_XR = auto()
    """Represents the Primax 5K XR VR headset.
    Resolution (per eye): 2560x1440
    Refresh rate: 90 Hz
    """

    VR_HEADSET_PRIMAX_8K = auto()
    """Represents the Primax 8K VR headset.
    Resolution (per eye): 2560x1440
    Refresh rate: 90 Hz
    """

    VR_HEADSET_PRIMAX_8K_PLUS = auto()
    """Represents the Primax 8K Plus VR headset.
    Resolution (per eye): 2560x1440
    Refresh rate: 90 Hz
    """

    VR_HEADSET_PRIMAX_8K_X = auto()
    """Represents the Primax 8K X VR headset.
    Resolution (per eye): 2560x1440
    Refresh rate: 90 Hz
    """

VR_HEADSET_MAP = \
{
    'none': VRHeadsetTypes.VR_HEADSET_NONE,
    'generic': VRHeadsetTypes.VR_HEADSET_GENERIC,
    'psvr': VRHeadsetTypes.VR_HEADSET_PSVR,
    'rift': VRHeadsetTypes.VR_HEADSET_RIFT,
    'rifts': VRHeadsetTypes.VR_HEADSET_RIFT_S,
    'quest': VRHeadsetTypes.VR_HEADSET_QUEST,
    'quest2': VRHeadsetTypes.VR_HEADSET_QUEST_2,
    'index': VRHeadsetTypes.VR_HEADSET_INDEX,
    'vive': VRHeadsetTypes.VR_HEADSET_HTC_VIVE,
    'vivepro': VRHeadsetTypes.VR_HEADSET_HTC_VIVE_PRO,
    'odyssey': VRHeadsetTypes.VR_HEADSET_ODYSSEY,
    'reverb': VRHeadsetTypes.VR_HEADSET_REVERB,
    'reverb2': VRHeadsetTypes.VR_HEADSET_REVERB_G2,
    'primax4k': VRHeadsetTypes.VR_HEADSET_PRIMAX_4K,
    'primax5ksuper': VRHeadsetTypes.VR_HEADSET_PRIMAX_5K_SUPER,
    'primax5kxr': VRHeadsetTypes.VR_HEADSET_PRIMAX_5K_XR,
    'primax8k': VRHeadsetTypes.VR_HEADSET_PRIMAX_8K,
    'primax8kplus': VRHeadsetTypes.VR_HEADSET_PRIMAX_8K_PLUS,
    'primax8kx': VRHeadsetTypes.VR_HEADSET_PRIMAX_8K_X
}
"""Helper map used when deserializing headset type data from file."""
