
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

"""Contains the implementation of the DCSLauncherMainWindow."""

# Runtime Imports
import os
import tkinter
from tkinter import ttk
from PIL import ImageTk

# DCS Imports
from dcs.launcher.ui.window import Window

class DCSLauncherMainWindow(Window):

    """Represents the main application window."""

    def on_create(self, *args, **kwargs) -> None:

        """Initialization of the main window."""

        # Create canvas
        self._canvas = tkinter.Canvas(self,
                                      width=self.Width,
                                      height=self.Height)

        # Load Images
        self._stripe = render = ImageTk.PhotoImage(
            file=os.path.abspath(os.path.expanduser(
                './data/images/hazard_stripe.png')))

        self._logo = render2 = ImageTk.PhotoImage(
            file=os.path.abspath(os.path.expanduser(
                './data/images/logo.png')))

        self._canvas.pack()
        self.pack()

        self._canvas.create_image((0,-30), image=render, anchor='nw')
        self._canvas.create_image((0,20), image=render2, anchor='nw')
        self._canvas.create_image((0,975), image=render, anchor='nw')

        self.master.resizable(width=False, height=False)