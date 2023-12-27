# pylint: disable=C0114, C0103, E0401

from customtkinter import set_appearance_mode, CTk
from views.home import Home
from views.navigation import Navigation

class App(CTk):
    """
    The main application class.
    """
    def __init__(self):
        super().__init__()
        self.title("E Commerce")
        self.geometry("1280x720")
        self.resizable(0,0)
        set_appearance_mode("light")

        Navigation(self, app_shell=self, active_frame=Home(self))

app = App()
app.mainloop()
