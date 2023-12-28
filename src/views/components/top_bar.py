# pylint: disable=C0114, C0103, E0401

import importlib
from functools import partial
from customtkinter import CTkFrame, CTkButton
from config import app
from utils.navigation import switch_page

class TopBar(CTkFrame):
    """
    The top bar of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            corner_radius=0,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK
        )

    def render(self):
        """
        Renders the top bar.
        """
        HomePage = importlib.import_module('views.pages.home').HomePage

        CTkButton(
            self,
            text="Back",
            width=70,
            corner_radius=0,
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
            text_color=app.COLOR_SECONDARY_DARK,
            hover_color=app.COLOR_SECONDARY_LIGHT,
            command=partial(switch_page, HomePage)
        ).pack(anchor='w', pady=15, padx=20)

        self.pack(fill='x')

        return self
