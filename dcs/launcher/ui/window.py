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

"""Contains the implementation of the Window class."""

# Runtime Imports
import tkinter
from tkinter import ttk
from typing import Union

# Dependency Imports
from PIL import Image, ImageTk


class Window(tkinter.Frame):

    """Utility class to hide some common window handling operations.

    :param _width: The width of the window.
    :type _width: int

    :param _height: The height of the window.
    :type _height: int
    """

    @property
    def Width(self) -> int:
        """Returns the width of the window."""
        return self._width

    @property
    def Height(self) -> int:
        """Returns the height of the window."""
        return self._height

    def __init__(self,
                 master: tkinter.Toplevel = None,
                 title: str = 'Window title',
                 favicon: str = None,
                 centered: bool = False,
                 width: int = 1024,
                 height: int = 768,
                 *args,
                 **kwargs) -> None:

        """
        Creates a new Window instance.

        :param master: The parent window to be passed to the underlying frame
            object.
        :type master: tkinter.TopLevel

        :param title: The title of the window.
        :type title: str

        :param favicon: The window icon to use.
        :type favicon: str

        :param centered: Whether or not the window should be centered on the
            active monitor.
        :type centered: bool

        :param width: The initial width of the window.
        :type width: int

        :param height: The initial height of the window.
        :type height: int
        """

        super().__init__(master)

        self._width = width
        self._height = height

        self.master.title(title)

        if favicon is not None:
            self.master.tk.call('wm',
                                'iconphoto',
                                self.master._w,
                                ImageTk.PhotoImage(Image.open(favicon)))

        self.master.minsize(width, height)

        if centered:
            self.center_window(self.master)

        self.on_create(*args, **kwargs)

    def center_window(self, window: tkinter.Frame = None) -> None:

        """Centers the window on the active monitor.

        :param window: The top level window to center.
        :type window: tkinter.Frame
        """

        if window is None:
            window = self.master

        window.update_idletasks()

        width = window.winfo_width()
        frame_width = window.winfo_rootx() - window.winfo_x()
        window_width = width + 2 * frame_width

        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        window_height = height + titlebar_height + frame_width

        x_pos = window.winfo_screenwidth() // 2 - window_width // 2
        y_pos = window.winfo_screenheight() // 2 - window_height // 2

        window.geometry(f'{width}x{height}+{x_pos}+{y_pos}')
        window.deiconify()

    @staticmethod
    def get_tab_id_for_name(
        notebook: ttk.Notebook,
        tab_name: str) -> Union[str, None]:

        """Retrieves the tab ID of a tab in the given notebook based on the
        name of the tab.

        :param notebook: The notebook to retrieve the tab ID from.
        :type notebook: ttk.Notebook

        :param tab_name: Name of the tab to retrieve.
        :type tab_name: str

        :return: The ID of the tab, or -1 if it was not found.
        :rtype: int
        """

        for i in notebook.tabs():
            if notebook.tab(i, 'text') == tab_name:
                return i

        return None

    def on_create(self, *args, **kwargs) -> None:

        """Handler function called when the window is created."""
