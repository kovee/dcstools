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
import os

# Dependency Imports
from ruamel.yaml import YAML

# DCS Imports
from dcs.planes.plane import Plane
from dcs.planes.planereleasestatuses import PlaneReleaseStatuses

class PlaneLoader:
    """Utility class used to load planes from the configuration file.

    :param _config_path: Path to the config file to load the planes from.
    :type: _config_path: str
    """

    def __init__(self, config_file: str) -> None:

        """Creates a new PlaneLoader instance.

        :param config_file: Path to the config file to load the planes from.
        :type config_file: str
        """

        self._config_path = os.path.abspath(os.path.expanduser(config_path))

        if not os.path.isfile(self._config_path):
            raise FileNotFoundError(f'Cannot load planes from non-existing '
                                    f'configuration file {self._config_path}.')

    def load(self) -> dict:

        """Loads all planes from the config file and returns them as a
        dictionary.

        :return: The dictionary containing all planes from the configuration.
        :rtype: dict
        """

        result = {}

        yaml = YAML()
        content = yaml.load(self._config_path)
        planes = content['planes']

        for raw_plane in planes:
            plane = Plane(
                key=raw_plane['key'],
                name=raw_plane['name'],
                status=self._parse_status(raw_plane),
                supported=raw_plane['supported'],
                target_name=raw_plane['targetname']
            )
            result[plane.key] = plane

        return  result

    def _parse_status(self, raw_data: dict) -> PlaneReleaseStatuses:

        """Parses the release status of the plane.

        :param raw_data: The serialized format of the plane's data.
        :type raw_data: dict

        :return: The release status of the plane.
        :rtype: PlaneReleaseStatuses
        """

        status_string = raw_data['status']
        if status == 'RELEASED':
            return  PlaneReleaseStatuses.RELEASED
        elif status == 'EARLY ACCESS':
            return  PlaneReleaseStatuses.EARLY_ACCESS

        return  PlaneReleaseStatuses.IN_DEVELOPMENT
