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

"""Contains the implementation of the Configuration class."""

# Runtime Imports
import logging
import os

# Dependency Imports
from ruamel.yaml import YAML

# DCS Imports
from dcs.constants import DCSTOOLS_LOG_CHANNEL, DEFAULT_LOG_PATH

class Configuration:

    """Utility class to manage application configuration.

    :param _configuration: The actual configuration data.
    """

    def __init__(self) -> None:

        """Creates a new Configuration instance."""

        self._configuration = {}

    def initialize(self, config_path: str) -> None:

        """Initializes the configuration."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)

        config_path = os.path.abspath(os.path.expanduser(config_path))

        logger.debug(f'Loading configuration from {config_path}.')

        if not os.path.isfile(config_path):
            logger.error(f'Configuration file {config_path} does not exist.')
            return

        with open(file=config_path, mode='r', encoding='utf-8') as raw:
            file = YAML()
            self._configuration = file.load(raw.read())

        logger.info('Configuration loaded.')

    def get_log_level(self) -> str:

        """Returns the log level for the application."""

        return self._configuration.get('loglevel', 'INFO')

    def get_log_path(self) -> str:

        """Returns the log path of the application."""

        return self._configuration.get('logpath', DEFAULT_LOG_PATH)

    def get_language(self) -> str:

        """Returns the language of the application."""

        return self._configuration.get('language', 'en')

CONFIGURATION = Configuration()
"""The global configuration instance."""