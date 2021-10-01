
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
        self._stripe = stripe = ImageTk.PhotoImage(
            file=os.path.abspath(os.path.expanduser(
                './data/images/hazard_stripe.png')))

        self._logo = logo = ImageTk.PhotoImage(
            file=os.path.abspath(os.path.expanduser(
                './data/images/logo.png')))

        # Profile List
        self._profile_list = ttk.Combobox(
            self,
            values=self.read_profile_list(),
            width=70,
            state='readonly')
        self._profile_list.place(x=50, y=170)

        # Profile Editor Button
        self._profile_editor_button = ttk.Button(
            self,
            text='Edit Profile',
            style='primary.TButton',
            width=70,
            command=self.on_edit_profile)
        self._profile_editor_button.place(x=50, y=210)

        # Profile Manager Button
        self._profile_manager_button = ttk.Button(
            self,
            text='Profile Manager',
            style='primary.TButton',
            width=70,
            command=self.on_profile_manager)
        self._profile_manager_button.place(x=50, y=250)

        # Launch Button
        self._launch_button = ttk.Button(
            self,
            text='Launch',
            style='danger.TButton',
            width=70,
            command=self.on_launch)
        self._launch_button.place(x=50, y=290)

        # Donate Button
        self._donate_button = ttk.Button(
            self,
            text='Donate',
            style='warning.TButton',
            width=70,
            command=self.on_donate)
        self._donate_button.place(x=50, y=330)

        # Settings Button
        self._settings_button = ttk.Button(
            self,
            text='Settings',
            style='secondary.TButton',
            width=70,
            command=self.on_settings)
        self._settings_button.place(x=50,y=370)

        # Exit Button
        self._exit_button = ttk.Button(
            self,
            text='Exit',
            style='secondary.TButton',
            width=70,
            command=self.on_exit)
        self._exit_button.place(x=50, y=410)

        self._canvas.pack()
        self.pack()

        self._canvas.create_image((0,-30), image=stripe, anchor='nw')
        self._canvas.create_image((0,37), image=logo, anchor='nw')
        self._canvas.create_image((0,465), image=stripe, anchor='nw')

        self.master.resizable(width=False, height=False)

    def on_edit_profile(self) -> None:
        pass

    def on_profile_manager(self) -> None:
        pass

    def on_launch(self) -> None:
        pass

    def on_settings(self) -> None:
        pass

    def read_profile_list(self) -> list:
        return  []

    def on_exit(self) -> None:
        self.master.destroy()

    def on_donate(self) -> None:
        pass