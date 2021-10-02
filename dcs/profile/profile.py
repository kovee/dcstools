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

"""Contains the implementation of the Profile class."""

# Runtime Imports
from dataclasses import dataclass

# DCS Imports
from dcs.profile.controllermodes import ControllerModes
from dcs.profile.vrheadsettypes import VRHeadsetTypes
from dcs.profile.joysticktypes import JoystickTypes
from dcs.profile.joystickgriptypes import JoystickGripTypes
from dcs.profile.throttletypes import ThrottleTypes
from dcs.profile.ruddertypes import RudderTypes

@dataclass
class Profile:

    """Represents a single DCS Launcher gaming profile.

    :param name: The name of the profile.
    :type name: str

    :param description: The description of the profile.
    :type description: str

    :param controller_mode: The controller mode to use. Either to use control
        assignments specified in T.A.R.G.E.T., or use the default assignment
        method from DCS>
    :type controller_mode: ControllerModes

    :param plane: The plane to fly with the profile.
    :type plane: Plane

    :param vr_enabled: Whether or not playing in VR.
    :type vr_enabled: bool

    :param headset_type: The type of VR headset to use.
    :type headset_type: VRHeadsetTypes

    :param vr_mod_enabled: Whether or not to enable VR mod in DCS.
    :type vr_mod_enabled: bool

    :param keyboard_layout: The keyboard layout to use.
    :type keyboard_layout: str

    :param joystick: The type of joystick to use.
    :type joystick: JoystickTypes

    :param grip: The type of joystick grip to use.
    :type grip: JoystickGripTypes

    :param throttle: The type of throttle to use.
    :type throttle: ThrottleTypes

    :param rudder: The type of rudder to use.
    :type rudder: RudderTypes

    :param mfd_enabled: Whether or not external MFDs are enabled.
    :type mfd_enabled: bool

    :param num_mfds: The number of MFDs to use.
    :type num_mfds: int
    """

    name: str
    description: str
    plane: 'Plane'
    controller_mode: ControllerModes = ControllerModes.CONTROLLER_TARGET
    vr_enabled: bool = False
    headset_type: VRHeadsetTypes = VRHeadsetTypes.VR_HEADSET_NONE
    vr_mod_enabled: bool = False
    keyboard_layout: str = 'en'
    joystick: JoystickTypes = JoystickTypes.JOYSTICK_NONE
    grip: JoystickGripTypes = JoystickGripTypes.JOYSTICK_GRIP_NONE
    throttle: ThrottleTypes = ThrottleTypes.THROTTLE_TYPE_NONE
    rudder: RudderTypes = RudderTypes.RUDDER_TYPE_NONE
    mfd_enabled: bool = False
    num_mfds: int = 0
