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

"""Contains the implementation of the TARGETGenerator class."""

# Runtime Imports
import os
from string import Template

class TARGETGenerator:

    """Utility class that generates a T.A.R.G.E.T. configuration for the
    Thrustmaster devices configured in the selected profile."""

    @staticmethod
    def generate() -> None:

        """Generates the T.A.R.G.E.T. configuration script.

        :raises FileNotFoundError: Raised when the T.A.R.G.E.T. script template
            was not found on the host machine.
        """

        # Create a map of all configuration values to be read from the profile
        # or from common configuration
        substitution_map = \
        {

        }

        # Load the template
        template_file = os.path.abspath(os.path.expanduser(
            '~/Documents/dcstools/templates/profile.tmc'))

        if not os.path.isfile(template_file):
            raise FileNotFoundError(
                f'The required template file ({template_file}) was not found.')

        template = None
        with open(file=template_file, mode='r', encoding='UTF-8') as file:
            template = file.read()

        # Substitute template variables based on the configuration
        script = None
        try:
            script = Template(template).substitute(substitution_map)
        except (ValueError, KeyError) as error:
            raise RuntimeError(
                'Failed to substitute script parameters.') from error

        # Write the script
        script_file = os.path.abspath(os.path.expanduser(
            '~/Documents/dcstools/generated/profile.tmc'))
        with open(file=script_file, mode='w', encoding='UTF-8') as file:
            file.write(script)
