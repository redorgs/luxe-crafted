# pylint: disable=C0114, E0611

from PIL import ImageTk
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
        self.wm_iconbitmap()
        self.iconphoto(False, ImageTk.PhotoImage(file='assets/images/logo/lc.png'))

        # Development Only
        set_appearance_mode("dark")
