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

"""Contains the entry point of the DCS Launcher."""

# Runtime Imports
import logging
import argparse

# DCS Imports
from dcs.constants import DCSTOOLS_LOG_CHANNEL
from dcs.tools.localizer import LOCALIZER
from dcs.launcher.ui.application import DCSLauncherGUIApplication

def configure_logging() -> None:

    """Initializes the logging configuration of the launcher."""
    logging.basicConfig(filename='dcstools.log',
                        encoding='utf-8',
                        level=logging.INFO)

def process_command_line() -> argparse.Namespace:

    """Processes the command line arguments.

    :return: The argparse Namespace object containing the processed command
        line arguments.
    :rtype: argparse.Namespace
    """

    parser = argparse.ArgumentParser(
        description=LOCALIZER.get('CLI_DESCRIPTION'),
        epilog=LOCALIZER.get('CLI_EPILOG'))

    parser.add_argument('-d', '--debug',
                        dest='debug_mode',
                        action='store_true',
                        help=LOCALIZER.get('CLI_OPTION_DEBUG_DESCRIPTION'))

    parser.add_argument('-r', '--run',
                        dest='run',
                        action='store',
                        default=None,
                        help=LOCALIZER.get('CLI_OPTION_RUN_DESCRIPTION'))

    return parser.parse_args()

def execute(arguments: argparse.Namespace) -> int:

    """Contains the main execution logic of the application.

    :return: The return code of the application.
    :type: int
    """

    # Enable debug mode if requested
    if arguments.debug_mode:

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.setLevel(logging.DEBUG)

    if arguments.run is not None:
        # Just start DCS based on the specified profile without displaying the
        # GUI
        pass
    else:
        # Normal startup, start the GUI
        application = DCSLauncherGUIApplication()
        application.mainloop()

    return  0

def main() -> int:

    """Implements the entry point of the DCS Launcher application.

    :return: The overall return value of the application.
    :rtype: int
    """

    configure_logging()

    try:
        return execute(process_command_line())
    except Exception:
        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.error('Unhandled exception.', exc_info=True)
        return -1

if __name__ == "__main__":
    main()
