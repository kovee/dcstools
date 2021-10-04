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

"""Contains the implementation of the AppFinder class."""

# Runtime Imports
import os
import logging

if os.name == 'nt':
    import winreg

from typing import Union

# DCS Imports
from dcs.constants import (
    DCSTOOLS_LOG_CHANNEL,
    DCS_STEAM_PATH,
    DCS_ED_PATH,
    DCS_WORKING_DIRECTORY,
    TARGET_PATH,
    TARGET_EXECUTABLE,
    PSVR_INSTALL_DIRECTORY,
    PSMOVESERVICE_INSTALL_DIRECTORY,
    PSMOVESERVICE_EXECUTABLE,
    FREEPIE_INSTALL_DIRECTORY,
    FREEPIE_EXECUTABLE
)

class AppFinder:

    """Utility class to help find the location of various tools on the host
    system."""

    @staticmethod
    def find_dcs_install_directory() -> Union[str, None]:

        """
        Finds the installation directory of DCS:World.

        This function doesn't take into account the possibility of having
        multiple DCS installations on the host system, it will only find the
        first occurrence of the possible installations in the following order:

        1. DCS:World - Steam Edition
        2. DCS:World - Eagle Dynamics Edition
        3. DCS World Open Beta - Eagle Dynamics Edition
        4. DCS World Open Alpha - Eagle Dynamics Edition

        :return: The path to the install directory, or 'None' if it was not
            found.
        :rtype: Union[str, None]
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Attempting to find DCS installation directory...')

        # Typically when DCS is installed from Steam it will be installed in
        # the steamapps directory, so start there.
        if os.path.isdir(DCS_STEAM_PATH):
            logger.info(
                f'DCS install directory identified as {DCS_STEAM_PATH}.')
            return DCS_STEAM_PATH

        # If it was not found there, it might be possible that Steam is
        # installed in a non-default directory, so attempt to find it from
        # the Windows registry
        try:
            root = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(root, 'SOFTWARE\\Valve\\Steam')
            value, value_type = winreg.QueryValueEx(key, 'SteamPath')
            dcs_path = os.path.abspath(f'{value}/steamapps/common/DCSWorld')
            logger.info(
                f'DCS install directory identified as {dcs_path}.')
            return dcs_path
        except OSError:
            pass

        # Looks like Steam is not installed, try alternative install location.
        if os.path.isdir(DCS_ED_PATH):
            return DCS_ED_PATH

        # As a last resort, try to check the registry for the various ED
        # install locations.
        try:
            root = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(root, 'SOFTWARE\\Eagle Dynamics\\DCS World')
            value, value_type = winreg.QueryValueEx(key, 'path')
            logger.info(
                f'DCS install directory identified as {value}.')
            return value
        except OSError:
            pass

        try:
            root = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(
                root,
                'SOFTWARE\\Eagle Dynamics\\DCS World Open Beta')
            value, value_type = winreg.QueryValueEx(key, 'path')
            logger.info(
                f'DCS install directory identified as {value}.')
            return value
        except OSError:
            pass

        try:
            root = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(
                root,
                'SOFTWARE\\Eagle Dynamics\\DCS World Open Alpha')
            value, value_type = winreg.QueryValueEx(key, 'path')
            logger.info(
                f'DCS install directory identified as {value}.')
            return value
        except OSError:
            pass

        # Still not found the install path, just give up
        logger.warning('Failed to identify the DCS installation directory, it '
                       'has to be set manually.')
        return None

    @staticmethod
    def find_dcs_working_directory() -> Union[str, None]:

        """Locates the working directory of DCS.

        :return: The path to the working directory, or 'None' if it was not
            found.
        :rtype: Union[str, None]
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Attempting to find DCS working directory...')

        # DCS by default will use the Saved Games folder to store files, so
        # start there
        dcs_path = os.path.abspath(os.path.expanduser(DCS_WORKING_DIRECTORY))
        if os.path.isdir(dcs_path):
            logger.info(f'DCS working directory identified as {dcs_path}.')
            return dcs_path

        # Give up
        logger.warning('Failed to identify the DCS working directory, it has '
                       'to be set manually.')
        return None

    @staticmethod
    def find_target_directory() -> Union[str, None]:

        """Locates the path where T.A.R.G.E.T. is installed.

        :return: The path to the T.A.R.G.E.T. installation directory, or
            'None', if it was not found.

        :rtype: Union[str, None]
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Attempting to find T.A.R.G.E.T. installation '
                     'directory...')

        # Start with the default installation directory
        target_path = os.path.abspath(os.path.expanduser(TARGET_PATH))
        target_executable = os.path.abspath(os.path.expanduser(
            f'{TARGET_PATH}/{TARGET_EXECUTABLE}'))
        if os.path.isdir(target_path) and os.path.isfile(target_executable):
            logger.info(f'T.A.R.G.E.T. installation is identified '
                        f'as {target_path}.')
            return target_path

        # Give up
        logger.warning('Failed to identify the T.A.R.G.E.T. installation '
                       'directory, it has to be set manually.')
        return None


    @staticmethod
    def find_psvr_path() -> Union[str, None]:

        """Locates the directory where Trinus PSVR is installed.

        :return: The path to the Trinus PSVR installation directory, or 'None',
            if it was not found.
        :rtype: Union[str, None]
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Attempting to find Trinus PSVR installation '
                     'directory...')

        psvr_directory = os.path.abspath(os.path.expanduser(
            PSVR_INSTALL_DIRECTORY))
        if os.path.isdir(psvr_directory):
            logger.info(f'Trinus PSVR installation directory is identified '
                        f'as {psvr_directory}.')
            return  psvr_directory

        logger.warning('Failed to identify the Trinus PSVR installation '
                       'directory, it has to be set manually.')
        return  None

    @staticmethod
    def find_psmoveservice_path() -> Union[str, None]:

        """Locates the installation directory of PSMoveService.

        :return: The path to the PSMoveService installation directory, or
            'None', if it was not found.
        :rtype: Union[str, None]
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Attempting to find the PSMoveService installation '
                     'directory...')

        psmoveservice_directory = os.path.abspath(os.path.expanduser(
            PSMOVESERVICE_INSTALL_DIRECTORY))
        psmoveservice_executable = os.path.abspath(os.path.expanduser(
            f'{psmoveservice_directory}/{PSMOVESERVICE_EXECUTABLE}'))

        if os.path.isdir(psmoveservice_directory) \
            and os.path.isfile(psmoveservice_executable):

            logger.info(f'PSMoveService installation directory is identified '
                        f'as {psmoveservice_directory}.')
            return psmoveservice_directory

        logger.warning('Failed to identify the PSMoveService installation '
                       'directory, it has to be set manually.')
        return  None

    @staticmethod
    def find_freepie_path() -> Union[str, None]:

        """Locates the installation directory of FreePIE.

        :return: The path to the FreePIE installation directory, or 'None' if
            it was not found.

        :rtype: Union[str, None]
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Attempting to find the FreePIE installation '
                     'directory...')

        freepie_directory = os.path.abspath(os.path.expanduser(
            FREEPIE_INSTALL_DIRECTORY))
        freepie_executable = os.path.abspath(os.path.expanduser(
            f'{freepie_directory}/{FREEPIE_EXECUTABLE}'))

        if os.path.isdir(freepie_directory) \
            and os.path.isfile(freepie_executable):

            logger.info(f'FreePIE installation directory is identified '
                        f'as {freepie_directory}.')
            return freepie_directory

        logger.warning('Failed to identify the FreePIE installation '
                       'directory, it has to be set manually.')
        return None