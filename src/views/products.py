# pylint: disable=C0114, C0103, E0401

from customtkinter import  CTkLabel, CTkScrollableFrame, CTkEntry, CTkFrame, CTkButton

class Products(CTkFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white", corner_radius=0)
        self.pack(side="right", fill="both", expand=True)

        TopBar(self)

class TopBar(CTkFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(side="top", fill="x", pady="10", padx="10")

        CTkLabel(self, text="Products").pack(side="left")
        Search(self)

class Search(CTkFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(side="right", fill="x")

        CTkEntry(self, placeholder_text="Search product...", width=300).pack(side="left")
        CTkButton(self, text="Search", width=100, corner_radius=0, fg_color='white', border_color="#333").pack(side="left")