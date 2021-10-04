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

"""Contains the implementation of the ProfileManager class."""

# Runtime Imports
import os
import glob
import logging
from typing import Union

# DCS Imports
from dcs.constants import DEFAULT_PROFILES_PATH, DCSTOOLS_LOG_CHANNEL
from dcs.profile.profile import Profile
from dcs.profile.profileserializer import ProfileSerializer

class ProfileManager:

    """Manager class for user profiles."""

    def __init__(self) -> None:

        """Creates a new ProfileManager instance."""

        self._profiles = {}
        self._load_profiles()

    def get_profile(self, profile_name: str) -> Union[Profile, None]:

        """Returns a profile with the given name.

        :param profile_name: Name of the profile to retrieve.
        :type profile_name: str

        :return: The requested profile object, or 'None' if it was not found.
        :rtype: Union[Profile, None]
        """

        return  self._profiles.get(profile_name, None)

    def get_profile_names(self) -> list[str]:

        """Returns the list of existing profile names.

        :return: The list of existing profile names.
        :rtype: list[str]
        """

        return self._profiles.keys()

    def _load_profiles(self) -> None:

        """Loads existing user profiles from disk."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Loading user profiles...')

        profiles_path = os.path.abspath(os.path.expanduser(
            DEFAULT_PROFILES_PATH))
        if not os.path.isdir(profiles_path):
            logger.error(f'Profiles directory {profiles_path} does not exist.')
            return

        file_list = glob.glob(f'{profiles_path}/*.yaml')
        for file in file_list:
            self._load_single_profile(file)

    def _load_single_profile(self, path: str) -> None:

        """Loads a single profile from disk.

        :param path: Path to the file to load.
        :type path: str
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Attempting to load {path}...')

        profile = ProfileSerializer.load(path)

        if profile is None:
            logger.error(f'Failed to load a valid profile from {path}.')
            return

        self._profiles[profile.name] = profile
        logger.debug(f'Profile {profile.name} is registered in the profile '
                     f'manager.')

PROFILE_MANAGER = ProfileManager()
"""The global profile manager instance."""
