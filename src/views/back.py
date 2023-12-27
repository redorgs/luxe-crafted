# pylint: disable=C0114, C0103, E0401

from customtkinter import  CTkFrame, CTkButton

class TopBar(CTkFrame):
    """
    The top bar of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(fill="x")

        CTkButton(
            self,
            text="Back",
            width=70,
            fg_color='transparent',
            text_color='#333',
            border_width=1,
            border_color='#333',
            corner_radius=0
        ).pack(side="left", padx=10, pady=10)
