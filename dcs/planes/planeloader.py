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

"""Contains the implementation of the PlaneLoader class."""

# Runtime Imports
import logging
import os
from typing import Union

# Dependency Imports
from ruamel.yaml import YAML

# DCS Imports
from dcs.constants import DCSTOOLS_LOG_CHANNEL
from dcs.planes.plane import Plane
from dcs.planes.planereleasestatuses import PlaneReleaseStatuses

class PlaneLoader:
    """Utility class used to load planes from the configuration file."""

    @staticmethod
    def load(path: str) -> Union[Plane, None]:

        """Loads all planes from the config file and returns them as a
        dictionary.

        :param path: Path to the plane to load.
        :type path: str

        :return: The loaded Plane object.
        :rtype: Plane
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Loading plane {path} from disk...')

        plane = None

        if not os.path.isfile(path):
            logger.error(f'Plane configuration {path} does not exist.')
            return None

        content = None
        with open(file=path, mode='r', encoding='utf-8') as raw_plane:
            yaml = YAML()
            content = yaml.load(raw_plane.read())

        plane = Plane(
            key=content['key'],
            name=content['name'],
            status=PlaneLoader._parse_status(content),
            supported=content['supported'],
            target_name=content['targetname'])

        return plane

    @staticmethod
    def _parse_status(raw_data: dict) -> PlaneReleaseStatuses:

        """Parses the release status of the plane.

        :param raw_data: The serialized format of the plane's data.
        :type raw_data: dict

        :return: The release status of the plane.
        :rtype: PlaneReleaseStatuses
        """

        status_string = raw_data['status']
        if status_string == 'RELEASED':
            return  PlaneReleaseStatuses.RELEASED
        elif status_string == 'EARLY ACCESS':
            return  PlaneReleaseStatuses.EARLY_ACCESS

        return  PlaneReleaseStatuses.IN_DEVELOPMENT
