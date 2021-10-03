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

"""Contains the implementation of the PlaneManager class."""

# Runtime Imports Imports
import os
import glob
import logging
from typing import Union

# DCS Imports
from dcs.constants import DCSTOOLS_LOG_CHANNEL, DEFAULT_PLANES_PATH
from dcs.planes.plane import Plane
from dcs.planes.planeloader import PlaneLoader

class PlaneManager:

    """Manager class for plane types."""

    def __init__(self) -> None:

        """Creates a new PlaneManager instance."""

        self._planes = {}
        self._load_planes()

    def get(self, plane_type: str) -> Union[Plane, None]:

        """Returns the Plane object associated with the given plane type.

        :param plane_type: The type of the plane to retrieve.
        :type plane_type: str

        :return: The Plane object associated with the given type, or 'None' if
            it was not found.
        :rtype: Union[Plane, None]
        """

        return self._planes.get(plane_type, None)

    def _load_planes(self) -> None:

        """Loads the plane data from the configuration."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Loading plane configurations...')

        planes_path = os.path.abspath(os.path.expanduser(DEFAULT_PLANES_PATH))
        if not os.path.isdir(planes_path):
            logger.error(f'Plane configuration directory {planes_path} does '
                         f'not exist.')
            return

        file_list = glob.glob(f'{planes_path}/*.yaml')
        for file in file_list:
            plane = PlaneLoader.load(file)
            if plane is not None:
                self._planes[plane.key] = plane

        logger.debug('Planes has been loaded.')

PLANE_MANAGER = PlaneManager()
