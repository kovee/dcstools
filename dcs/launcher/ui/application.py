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

"""Contains the implementation of the DCSLauncherGUIApplication class."""

# Runtime Imports
import os
import tkinter
from ttkbootstrap import Style

# DCS Imports
from dcs.launcher.ui.mainwindow import DCSLauncherMainWindow

class DCSLauncherGUIApplication(tkinter.Tk):

    """Wrapper class for the main Tkinter application.

    :param _mainwindow: The main application window.
    :type _mainwindow: DCSLauncherMainWindow
    """

    def __init__(self) -> None:

        """Creates a new DCSLauncherGUIApplication instance."""

        super().__init__()

        self._style = Style(theme='darkly')

        favicon_path = os.path.abspath(os.path.expanduser(
            './data/images/favicon.ico'))

        self._mainwindow = DCSLauncherMainWindow(
            master=self,
            title='DCS Launcher',
            favicon=favicon_path,
            centered=True,
            width=800   ,
            height=1000)