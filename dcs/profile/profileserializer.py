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

"""Contains the implementation of the ProfileSerializer class."""

# Runtime Imports
import os
import logging
from typing import Union

# Dependency Imports
from ruamel.yaml import YAML

# DCS Imports
from dcs.constants import DCSTOOLS_LOG_CHANNEL
from dcs.profile import Profile
from dcs.profile.controllermodes import ControllerModes
from dcs.planes import PLANE_MANAGER
from dcs.profile.vrheadsettypes import VRHeadsetTypes, VR_HEADSET_MAP
from dcs.profile.joysticktypes import JoystickTypes, JOYSTICK_MAP
from dcs.profile.joystickgriptypes import JoystickGripTypes, JOYSTICK_GRIP_MAP
from dcs.profile.throttletypes import ThrottleTypes, THROTTLE_MAP
from dcs.profile.ruddertypes import RudderTypes, RUDDER_MAP

class ProfileSerializer:

    """Utility class to help with the saving and loading of profile files."""

    @staticmethod
    def load(path: str) -> Union[Profile, None]:

        """Loads and deserializes the given profile file from disk.

        :param path: Path to the profile to load.
        :type path: str

        :return: The loaded Profile object, or 'None' if loading failed.
        :rtype: Union[Profile, None]
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Loading profile {path} from disk...')

        profile = None

        if not os.path.isfile(path):
            logger.error(f'Profile {path} does not exist.')
            return None

        # Load and parse the YAML file
        content = None
        with open(file=path, mode='r', encoding='UTF-8') as raw:
            yaml = YAML()
            content = yaml.load(raw.read())

        # Deserialize profile name - mandatory
        try:
            name = content['name']
        except KeyError:
            logger.error(f'Profile name was not found in profile {path}.')
            return None

        # Deserialize profile description - mandatory
        try:
            description = content['description']
        except KeyError:
            logger.error(f'Profile description was not found in profile '
                         f'{path}.')
            return None

        # Deserialize controller mode - default to DCS if not found
        try:
            controller_mode = content['controllermode']
        except KeyError:
            logger.warning(f'Controller mode was not found in profile {path}, '
                           f'defaulting to DCS basic.')
            controller_mode = 'dcs'

        if controller_mode == 'target':
            controller_mode = ControllerModes.CONTROLLER_TARGET
        else:
            controller_mode = ControllerModes.CONTROLLER_DCS

        # Deserialize plane type
        try:
            plane_type = content['plane']
        except KeyError:
            logger.error(f'Plane type was not found in profile {path}.')
            return None

        plane = PLANE_MANAGER.get(plane_type=plane_type)
        if not plane:
            logger.error(f'Unsupported plane type {plane_type} found in '
                         f'profile {path}.')
            return None

        # Deserialize VR enabled
        try:
            vr_enabled = content['vrenabled']
        except KeyError:
            logger.warning(f'VR mode is not specified in profile {path}.')
            vr_enabled = False

        # Look for the rest of the VR options only if VR is enabled
        headset_type = VRHeadsetTypes.VR_HEADSET_NONE
        vr_mod_enabled = False

        if vr_enabled:
            try:
                headset_type = ProfileSerializer._load_headset_type(
                    content['headsettype'])
            except KeyError:
                logger.warning(f'VR mode is enabled, but headset type is not '
                               f'specified in profile {path}.')

            try:
                vr_mod_enabled  = content['vrmodenabled']
            except KeyError:
                logger.warning(f'VR mode is enabled, but VR mod usage is not '
                               f'specified.')

        # Deserialize keyboard layout
        try:
            keyboard_layout = content['keyboardlayout']
        except KeyError:
            logger.warning(f'Keyboard layout is not specified in profile '
                           f'{path}, using english by default.')
            keyboard_layout = 'en'

        # Deserialize joystick type
        try:
            joystick_type = ProfileSerializer._load_joystick_type(
                content['joystick'])
        except KeyError:
            logger.warning(f'Joystick type is not found in profile {path}.')
            joystick_type = JoystickTypes.JOYSTICK_NONE

        # Deserialize joystick grip if needed
        has_grip = joystick_type not in (JoystickTypes.JOYSTICK_NONE,
                                         JoystickTypes.JOYSTICK_GENERIC)
        if has_grip:
            try:
                grip_type = ProfileSerializer._load_joystick_grip_type(
                    content['grip'])
            except KeyError:
                logger.warning(f'Joystick grip type has not specified in '
                               f'profile {path}.')
                grip_type = JoystickGripTypes.JOYSTICK_GRIP_NONE

        # Deserialize throttle type
        try:
            throttle_type = ProfileSerializer._load_throttle_type(
                content['throttle'])
        except KeyError:
            logger.debug(f'Throttle type is not specified in profile {path}.')
            throttle_type = ThrottleTypes.THROTTLE_TYPE_NONE

        # Deserialize rudder type
        try:
            rudder_type = ProfileSerializer._load_rudder_type(
                content['rudder'])
        except KeyError:
            logger.warning(f'Rudder type is not specified in profile {path}.')
            rudder_type = RudderTypes.RUDDER_TYPE_NONE

        # Deserialize MFD
        try:
            mfd_enabled = content['mfdenabled']
        except KeyError:
            logger.debug(f'MFD configuration not found in profile {path}.')
            mfd_enabled = False

        if mfd_enabled:
            try:
                num_mfds = content['nummfds']
            except KeyError:
                logger.error(f'Number of MFDs not found in profile {path}. ')
                num_mfds = 0
                mfd_enabled = False

        # Create the profile object
        profile = Profile(
            name=name,
            description=description,
            controller_mode=controller_mode,
            plane=plane,
            vr_enabled=vr_enabled,
            headset_type=headset_type,
            vr_mod_enabled=vr_mod_enabled,
            keyboard_layout=keyboard_layout,
            joystick=joystick_type,
            grip=grip_type,
            throttle=throttle_type,
            rudder=rudder_type,
            mfd_enabled=mfd_enabled,
            num_mfds=num_mfds)

        logger.debug(f'Profile {profile.name} loaded successfully.')
        return profile

    @staticmethod
    def save(profile: Profile) -> None:

        """Serializes the given profile and saves it to disk.

        :param profile: The profile to save.
        :type profile: Profile
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)

        if profile is None or not isinstance(profile, Profile):
            logger.error('Attempting to save an invalid profile.')
            return

        logger.debug(f'Saving profile {profile.name} to disk.')

    @staticmethod
    def _load_headset_type(raw_data: str) -> VRHeadsetTypes:

        """Deserializes the VR headset type from its raw format.

        :param raw_data: The serialized format of the headset type.
        :type raw_data: str

        :return: The type of the VR headset.
        :rtype: VRHeadsetTypes
        """

        return VR_HEADSET_MAP.get(raw_data, VRHeadsetTypes.VR_HEADSET_NONE)

    @staticmethod
    def _load_joystick_type(raw_data: str) -> JoystickTypes:

        """Deserializes the joystick type from its raw format.

        :param raw_data: The serialized format of the joystick type.
        :type raw_data: str

        :return: The type of joystick to use.
        :rtype: JoystickTypes
        """

        return JOYSTICK_MAP.get(raw_data, JoystickTypes.JOYSTICK_NONE)

    @staticmethod
    def _load_joystick_grip_type(raw_data: str) -> JoystickGripTypes:

        """Deserializes the joystick grip type from its raw format.

        :param raw_data: The serialized format of the joystick grip type.
        :type raw_data: str

        :return: The type of joystick grip type to use.
        :rtype: JoystickGripTypes
        """

        return  JOYSTICK_GRIP_MAP.get(raw_data,
                                      JoystickGripTypes.JOYSTICK_GRIP_NONE)

    @staticmethod
    def _load_throttle_type(raw_data: str) -> ThrottleTypes:

        """Deserializes the throttle type from its raw format.

        :param raw_data: The serialized format of the throttle type.
        :type raw_data: str

        :return: The type of throttle to use.
        :rtype: ThrottleTypes
        """

        return THROTTLE_MAP.get(raw_data, ThrottleTypes.THROTTLE_TYPE_NONE)

    @staticmethod
    def _load_rudder_type(raw_data: str) -> RudderTypes:

        """Deserializes the rudder type from its raw format.

        :param raw_data: The serialized format of the rudder type.
        :type raw_data: str

        :return: The type of rudder to use.
        :rtype: RudderTypes
        """

        return RUDDER_MAP.get(raw_data, RudderTypes.RUDDER_TYPE_NONE)
