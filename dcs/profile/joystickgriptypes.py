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

"""Contains the implementation of the JoystickGripTypes enum."""

# Runtime Imports
from enum import IntEnum, auto

class JoystickGripTypes(IntEnum):

    """List of supported joystick grips."""

    JOYSTICK_GRIP_NONE = auto()
    """Default value, represents no special joystick grip."""

    JOYSTICK_GRIP_A10 = auto()
    """Represents the Thrustmaster A-10 grip for the Warthog joystick."""

    JOYSTICK_GRIP_F18 = auto()
    """Represents the Thrustmaster F/A-18 grip for the Warthog joystick."""

    JOYSTICK_F16 = auto()
    """Represents the Thrustmaster F-16 grip for the Warthog joystick."""
