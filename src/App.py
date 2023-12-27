# pylint: disable=C0114, E0611

from customtkinter import set_appearance_mode, CTk
from config import app

class App(CTk):
    """
    The main application class.
    """
    def __init__(self):
        super().__init__()

        self.title(app.NAME)
        self.geometry(app.RESOLUTION)
        self.resizable(0,0)

        # Development Only
        set_appearance_mode("dark")
