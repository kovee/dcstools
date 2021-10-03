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

"""Contains the implementation of the DCSLauncherMainWindow."""

# Runtime Imports
import os
import tkinter
from tkinter import ttk
from PIL import ImageTk

# DCS Imports
from dcs.tools.localizer import LOCALIZER
from dcs.profile import PROFILE_MANAGER
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

        self._profile_picture = profile_picture = ImageTk.PhotoImage(
            file=os.path.abspath(os.path.expanduser(
                './data/images/fa18c_frame.png')))

        # Profile List
        self._profile_list = ttk.Combobox(
            self,
            values=self.read_profile_list(),
            width=70,
            state='readonly')
        self._profile_list.place(x=50, y=340)
        index = self.get_last_profile_index()
        if index >= 0:
            self._profile_list.current(index)
        else:
            self._profile_list.current(0)

        # Profile Editor Button
        self._profile_editor_button = ttk.Button(
            self,
            text=LOCALIZER.get(key='MAIN_WINDOW_EDIT_PROFILE_BUTTON'),
            style='primary.TButton',
            width=70,
            command=self.on_edit_profile)
        self._profile_editor_button.place(x=50, y=380)

        # Profile Manager Button
        self._profile_manager_button = ttk.Button(
            self,
            text=LOCALIZER.get(key='MAIN_WINDOW_PROFILE_MANAGER_BUTTON'),
            style='primary.TButton',
            width=70,
            command=self.on_profile_manager)
        self._profile_manager_button.place(x=50, y=420)

        # Launch Button
        self._launch_button = ttk.Button(
            self,
            text=LOCALIZER.get(key='MAIN_WINDOW_LAUNCH_BUTTON'),
            style='danger.TButton',
            width=70,
            command=self.on_launch)
        self._launch_button.place(x=50, y=460)

        # Donate Button
        self._donate_button = ttk.Button(
            self,
            text=LOCALIZER.get(key='MAIN_WINDOW_DONATE_BUTTON'),
            style='warning.TButton',
            width=70,
            command=self.on_donate)
        self._donate_button.place(x=50, y=500)

        # Settings Button
        self._settings_button = ttk.Button(
            self,
            text=LOCALIZER.get(key='MAIN_WINDOW_SETTINGS_BUTTON'),
            style='secondary.TButton',
            width=70,
            command=self.on_settings)
        self._settings_button.place(x=50,y=540)

        # Exit Button
        self._exit_button = ttk.Button(
            self,
            text=LOCALIZER.get(key='MAIN_WINDOW_EXIT_BUTTON'),
            style='secondary.TButton',
            width=70,
            command=self.on_exit)
        self._exit_button.place(x=50, y=580)

        self._canvas.pack()
        self.pack()

        self._canvas.create_image((0,-30), image=stripe, anchor='nw')
        self._canvas.create_image((0,37), image=logo, anchor='nw')
        self._canvas.create_image((7,150), image=profile_picture, anchor='nw')
        self._canvas.create_image((0,635), image=stripe, anchor='nw')

        self.master.resizable(width=False, height=False)

    def read_profile_list(self) -> list[str]:

        """Returns the list of the names of the currently existing profiles."""

        profile_list = PROFILE_MANAGER.get_profile_names()
        return profile_list

    def get_last_profile_index(self) -> int:

        """Returns the index of the profile that has been used the last
        time.

        :return: The index of the last used profile.
        :rtype: int
        """

        # TODO
        return  -1

    def on_edit_profile(self) -> None:

        """Handler function called when the edit profile button is pressed."""

        pass

    def on_profile_manager(self) -> None:

        """Handler function called when the profile manager button is
        pressed."""

        pass

    def on_launch(self) -> None:

        """Handler function called when the launch button is pressed."""

        pass

    def on_settings(self) -> None:

        """Handler function called when the settings button is pressed."""

        pass

    def on_exit(self) -> None:

        """Handler function called when the exit button is pressed."""

        self.master.destroy()

    def on_donate(self) -> None:

        """Handler function called when the donate button is pressed."""

        pass