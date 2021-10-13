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

"""Contains the implementation of the ProfileEditorWindow."""

# Runtime Imports
import logging

# Dependency Imports
import tkinter
from tkinter import ttk

# DCS Imports
from dcs.constants import DCSTOOLS_LOG_CHANNEL
from dcs.tools.localizer import LOCALIZER
from dcs.launcher.ui.window import Window
from dcs.profile import PROFILE_MANAGER
from dcs.profile.controllermodes import ControllerModes
from dcs.planes import PLANE_MANAGER

class ProfileEditorWindow(Window):

    """Contains the implementation of the profile editor window of the
    application."""

    def on_create(self, *args, **kwargs) -> None:

        """Handler function called when the window is created."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Creating profile editor window...')

        # Create UI elements
        self._tab_parent = ttk.Notebook(self.master, width=1025, height=675)

        self._generic_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._dcs_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._vr_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._tools_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._keyboard_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._joystick_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._throttle_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._rudder_tab = ttk.Frame(self._tab_parent, style='TFrame')
        self._mfd_tab = ttk.Frame(self._tab_parent, style='TFrame')

        self._tab_parent.add(self._generic_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_GENERIC_TAB'))
        self._tab_parent.add(self._dcs_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_DCS_TAB'))
        self._tab_parent.add(self._vr_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_VR_TAB'))
        self._tab_parent.add(self._tools_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_TOOLS_TAB'))
        self._tab_parent.add(self._keyboard_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_KEYBOARD_TAB'))
        self._tab_parent.add(self._joystick_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_JOYSTICK_TAB'))
        self._tab_parent.add(self._throttle_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_THROTTLE_TAB'))
        self._tab_parent.add(self._rudder_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_RUDDER_TAB'))
        self._tab_parent.add(self._mfd_tab,
                             text=LOCALIZER.get('PROFILE_EDITOR_MFD_TAB'))

        self._tab_parent.grid(
            row=0, column=0, padx=0, pady=0, columnspan=3, rowspan=3)

        self._build_generic_tab()
        self._build_dcs_tab()
        self._build_vr_tab()
        self._build_tools_tab()
        self._build_keyboard_tab()
        self._build_joystick_tab()
        self._build_throttle_tab()
        self._build_rudder_tab()
        self._build_mfd_tab()

        self._save_button = ttk.Button(
            self.master,
            text=LOCALIZER.get('PROFILE_EDITOR_SAVE'),
            width=7,
            style='info.TButton')
        self._save_button.grid(row=4, column=0, padx=20, pady=10, sticky='nw')

        self._reload_button = ttk.Button(
            self.master,
            text=LOCALIZER.get('PROFILE_EDITOR_RELOAD'),
            width=7,
            style='info.TButton')
        self._reload_button.grid(row=4, column=0, padx=0, pady=10)

        profile_name = kwargs.get('profile_name', None)
        if profile_name is not None:
            logger.debug(f'Retrieving profile {profile_name} to display in '
                         f'profile editor...')
            self._profile = PROFILE_MANAGER.get_profile(profile_name)

        else:
            logger.debug('No profile to display.')
            self._profile = None

        self._load_profile_data()

        logger.debug('Profile editor window created.')

    def on_controller_mode_changed(self, eventObject: object = None) -> None:

        """Event handler triggered when the controller mode on the generic tab
        has changed."""

        if self._generic_controller_mode_combobox.get() == LOCALIZER.get(
            'PROFILE_EDITOR_GENERIC_CONTROLLER_MODE_DCS'):
            self._generic_realistic_hotas_checkbox.config(state='disabled')
        else:
            self._generic_realistic_hotas_checkbox.config(state='normal')

    def on_vr_mode_changed(self, eventObject: object = None) -> None:

        """Event handler triggered when the VR mode checkbox has changed."""

        if self._generic_vr_mode_enabled.get():
            self._vr_headset_type_box.config(state='readonly')
            self._vr_mod_enabled_checkbox.config(state='normal')
        else:
            self._vr_headset_type_box.config(state='disabled')
            self._vr_mod_enabled_checkbox.config(state='disabled')

    def _build_generic_tab(self) -> None:

        """Creates the UI elements of the Generic tab."""

        self._generic_name_label = ttk.Label(
            self._generic_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_GENERIC_PROFILE_NAME'),
            style='TLabel')
        self._generic_name_label.grid(row=0, column=0, padx=20, pady=10)

        self._generic_profile_name = tkinter.StringVar()

        self._generic_name_entry = ttk.Entry(
            self._generic_tab,
            width=80,
            textvariable=self._generic_profile_name,
            style='info.TEntry')
        self._generic_name_entry.grid(row=0, column=1, padx=5, pady=10)

        self._generic_description_label = ttk.Label(
            self._generic_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_GENERIC_PROFILE_DESCRIPTION'),
            style='TLabel')
        self._generic_description_label.grid(row=1, column=0, padx=20, pady=10)

        self._generic_description_entry = tkinter.Text(
            self._generic_tab,
            width=80,
            height=3)
        self._generic_description_entry.grid(row=1, column=1, padx=5, pady=10)

        self._generic_controller_mode_label = ttk.Label(
            self._generic_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_GENERIC_CONTROLLER_MODE'),
            style='TLabel')
        self._generic_controller_mode_label.grid(
            row=2, column=0, padx=20, pady=10)

        self._generic_controller_mode_combobox = ttk.Combobox(
            self._generic_tab,
            values=[LOCALIZER.get('PROFILE_EDITOR_GENERIC_CONTROLLER_MODE_DCS'),
                    LOCALIZER.get('PROFILE_EDITOR_GENERIC_CONTROLLER_MODE_TARGET')],
            width=79,
            state='readonly',
            style='info.TCombobox')
        self._generic_controller_mode_combobox.grid(
            row=2, column=1, padx=5, pady=10)
        self._generic_controller_mode_combobox.bind(
            '<<ComboboxSelected>>',
            self.on_controller_mode_changed)

        self._generic_realistic_hotas_state = tkinter.BooleanVar()
        self._generic_realistic_hotas_checkbox = ttk.Checkbutton(
            self._generic_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_GENERIC_REALISTIC_HOTAS'),
            style='info.TCheckbutton',
            state='disabled',
            variable=self._generic_realistic_hotas_state)
        self._generic_realistic_hotas_checkbox.grid(
            row=3, column=1, padx=20, pady=10, columnspan=2, sticky='nw')

        self._generic_vr_mode_enabled = tkinter.BooleanVar()
        self._generic_vr_mode_checkbox = ttk.Checkbutton(
            self._generic_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_GENERIC_VR_ENABLED'),
            style='info.TCheckbutton',
            variable=self._generic_vr_mode_enabled,
            command=self.on_vr_mode_changed)
        self._generic_vr_mode_checkbox.grid(
            row=4, column=0, padx=20, pady=10, columnspan=2, sticky='nw')

    def _build_dcs_tab(self) -> None:

        """Creates the UI elements of the DCS tab."""

        self._dcs_tab_scrollbar = tkinter.Scrollbar(self._dcs_tab)
        self._dcs_tab_scrollbar.grid(
            row=0, column=5, rowspan=20, columnspan=20, sticky='nse')

        self._dcs_executable_path_label = ttk.Label(
            self._dcs_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_DCS_EXECUTABLE_PATH'),
            style='TLabel')
        self._dcs_executable_path_label.grid(row=0, column=0, padx=20, pady=10)

        self._dcs_executable_path = tkinter.StringVar()
        self._dcs_executable_path_entry = ttk.Entry(
            self._dcs_tab,
            width=81,
            textvariable=self._dcs_executable_path,
            style='info.TEntry')
        self._dcs_executable_path_entry.grid(row=0, column=1, padx=5, pady=10)

        self._dcs_executable_browse_button = ttk.Button(
            self._dcs_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_DCS_EXECUTABLE_BROWSE'),
            width=7,
            style='info.TButton')
        self._dcs_executable_browse_button.grid(
            row=0, column=2, padx=20, pady=10)

        self._dcs_executable_version_label = ttk.Label(
            self._dcs_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_DCS_VERSION'),
            style='TLabel')
        self._dcs_executable_version_label.grid(
            row=1, column=0, padx=5, pady=10)

        self._dcs_executable_version = tkinter.StringVar()
        self._dcs_executable_version.set('0.0.0.0')
        self._dcs_executable_version_value = ttk.Label(
            self._dcs_tab,
            textvariable=self._dcs_executable_version,
            style='danger.TLabel')
        self._dcs_executable_version_value.grid(
            row=1, column=1, padx=5, pady=10, sticky='w')

        self._dcs_working_path_label = ttk.Label(
            self._dcs_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_DCS_WORKING_PATH'),
            style='TLabel')
        self._dcs_working_path_label.grid(row=2, column=0, padx=20, pady=10)

        self._dcs_working_path = tkinter.StringVar()
        self._dcs_working_path_entry = ttk.Entry(
            self._dcs_tab,
            width=81,
            textvariable=self._dcs_working_path,
            style='info.TEntry')
        self._dcs_working_path_entry.grid(row=2, column=1, padx=5, pady=10)

        self._dcs_working_browse_button = ttk.Button(
            self._dcs_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_DCS_WORKING_BROWSE'),
            width=7,
            style='info.TButton')
        self._dcs_working_browse_button.grid(
            row=2, column=2, padx=20, pady=10)

        self._dcs_plane_label = ttk.Label(
            self._dcs_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_DCS_PLANE_TYPE'),
            style='TLabel')
        self._dcs_plane_label.grid(row=3, column=0, padx=20, pady=10)

        self._dcs_plane_box = ttk.Combobox(
            self._dcs_tab,
            values=PLANE_MANAGER.get_plane_names(),
            width=80,
            state='readonly',
            style='info.TCombobox')
        self._dcs_plane_box.grid(row=3, column=1, padx=20, pady=10)

    def _build_vr_tab(self) -> None:

        """Creates the UI elements of the VR tab."""

        self._vr_headset_type_label = ttk.Label(
            self._vr_tab,
            text=LOCALIZER.get('PROFILE_MANAGER_VR_HEADSET_TYPE'),
            style='TLabel')
        self._vr_headset_type_label.grid(row=0, column=0, padx=20, pady=10)

        self._vr_headset_type_box = ttk.Combobox(
            self._vr_tab,
            values=self._get_headset_types(),
            width=80,
            state='disabled',
            style='info.TCombobox')
        self._vr_headset_type_box.grid(row=0, column=1, padx=20, pady=10)
        self._vr_headset_type_box.current(0)

        self._vr_mod_enabled = tkinter.BooleanVar()
        self._vr_mod_enabled_checkbox = ttk.Checkbutton(
            self._vr_tab,
            text=LOCALIZER.get('PROFILE_EDITOR_VR_MOD_ENABLED'),
            style='info.TCheckbutton',
            state='disabled',
            variable=self._vr_mod_enabled)
        self._vr_mod_enabled_checkbox.grid(
            row=1, column=0, padx=20, pady=10, columnspan=2, sticky='nw')

    def _get_headset_types(self) -> list[str]:

        """Returns the list of supported VR headset types.

        The order of headsets in this list has to be kept in sync with the
        order in the VRHeadsetTypes enum for the mapping to work correctly.
        """

        result = [
            LOCALIZER.get('VR_HEADSET_TYPE_NONE'),
            LOCALIZER.get('VR_HEADSET_TYPE_GENERIC'),
            LOCALIZER.get('VR_HEADSET_TYPE_PSVR'),
            LOCALIZER.get('VR_HEADSET_TYPE_RIFT'),
            LOCALIZER.get('VR_HEADSET_TYPE_RIFT_S'),
            LOCALIZER.get('VR_HEADSET_TYPE_QUEST'),
            LOCALIZER.get('VR_HEADSET_TYPE_QUEST_2'),
            LOCALIZER.get('VR_HEADSET_TYPE_INDEX'),
            LOCALIZER.get('VR_HEADSET_TYPE_VIVE'),
            LOCALIZER.get('VR_HEADSET_TYPE_VIVE_PRO'),
            LOCALIZER.get('VR_HEADSET_TYPE_ODYSSEY'),
            LOCALIZER.get('VR_HEADSET_TYPE_REVERB'),
            LOCALIZER.get('VR_HEADSET_TYPE_REVERB_G2'),
            LOCALIZER.get('VR_HEADSET_TYPE_PRIMAX_4K'),
            LOCALIZER.get('VR_HEADSET_TYPE_PRIMAX_5K_SUPER'),
            LOCALIZER.get('VR_HEADSET_TYPE_PRIMAX_5K_XR'),
            LOCALIZER.get('VR_HEADSET_TYPE_PRIMAX_8K'),
            LOCALIZER.get('VR_HEADSET_TYPE_PRIMAX_8K_PLUS'),
            LOCALIZER.get('VR_HEADSET_TYPE_PRIMAX_8K_X'),
        ]

        return  result


    def _build_tools_tab(self) -> None:

        """Creates the UI elements of the Tools tab."""

        pass

    def _build_keyboard_tab(self) -> None:

        """Creates the UI elements of the Keyboard tab."""

        pass

    def _build_joystick_tab(self) -> None:

        """Creates the UI elements of the Joystick tab."""

        pass

    def _build_throttle_tab(self) -> None:

        """Creates the UI elements of the Throttle tab."""

        pass

    def _build_rudder_tab(self) -> None:

        """Creates the UI elements of the Rudder tab."""

        pass

    def _build_mfd_tab(self) -> None:

        """Creates the UI elements of the MFDs tab."""

        pass

    def _load_profile_data(self) -> None:

        """Loads the profile data to the UI elements."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Loading profile data...')

        if self._profile is None:
            logger.info('No profile data to display.')
            return

        self._generic_profile_name.set(self._profile.name)
        self._generic_description_entry.insert(tkinter.END,
                                               self._profile.description)

        if self._profile.controller_mode == ControllerModes.CONTROLLER_DCS:
            self._generic_controller_mode_combobox.current(0)
        else:
            self._generic_controller_mode_combobox.current(1)
            if self._profile.realistic_hotas:
                self._generic_realistic_hotas_state.set(True)
            else:
                self._generic_realistic_hotas_state.set(False)

        self.on_controller_mode_changed(None)

        self._generic_vr_mode_enabled.set(self._profile.vr_enabled)
        self.on_vr_mode_changed(None)

        self._dcs_executable_path.set(self._profile.dcs_path)
        self._dcs_working_path.set(self._profile.dcs_working_path)
        self._dcs_plane_box.set(self._profile.plane.name)

        self._vr_headset_type_box.current(int(self._profile.headset_type)-1)
        self._vr_mod_enabled.set(self._profile.vr_mod_enabled)

        logger.debug('Profile data loaded.')

