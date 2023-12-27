# pylint: disable=C0114, C0103, E0401

from customtkinter import  CTkLabel, CTkScrollableFrame, CTkEntry, CTkFrame, CTkButton
from views.product_frame import ProductFrame

class Products(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white", corner_radius=0)
        self.pack(side="right", fill="both", expand=True)

        TopBar(self)
        ProductFrame(self)

class TopBar(CTkFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#eee", corner_radius=0)
        self.pack(side="top", fill="x", ipady="20", ipadx="20")

        CTkLabel(self, text="Products").pack(side="left", padx=(20, 0))
        Search(self).pack(side="right", fill="x", padx=(0, 20))

class Search(CTkFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)

        CTkEntry(
            self,
            placeholder_text="Search product...",
            width=300,
            fg_color='white',
            text_color='#555',
            border_width=1,
            border_color="#aaa",
            corner_radius=0
        ).pack(side="left")
        CTkButton(
            self,
            text="Search",
            text_color='#555',
            hover_color='#eee',
            width=100,
            corner_radius=0,
            fg_color='white',
            border_width=1,
            border_color="#aaa"
        ).pack(side="left")
