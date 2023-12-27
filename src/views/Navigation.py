# pylint: disable=C0114, C0103, E0401

from functools import partial
from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkButton
from PIL import Image
from views.home import Home
from views.products import Products
from views.detail_product import DetailProduct

class Navigation(CTkFrame):
    """
    The navigation of the application.
    """
    def __init__(self, master, app_shell, active_frame, **kwargs):
        super().__init__(master ,**kwargs)

        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(side="left", fill="y", padx=30, pady=30)

        logo_image = CTkImage(light_image=Image.open("assets/images/logo.png"), size=(110, 20))

        CTkLabel(self, image=logo_image, text="").pack()
        NavigationFrame(self, app_shell=app_shell, active_frame=active_frame)

class NavigationFrame(CTkFrame):
    """
    The navigation frame of the application.
    """
    def __init__(self, master, app_shell, active_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(pady=10)
        self.app_shell = app_shell
        self.active_frame = active_frame

        NavigationButton(self, command=partial(self.changeView, Home), text="Home")
        NavigationButton(self, command=partial(self.changeView, Products), text="Products")
        NavigationButton(self, command=partial(self.changeView, DetailProduct), text="Detail Product")

    def changeView(self, view):
        """
        The onclick event of the navigation button.
        """
        self.active_frame.pack_forget()
        self.active_frame = view(self.app_shell)

class NavigationButton(CTkButton):
    """
    The navigation button of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color='transparent',
            text_color='#4a4a4a',
            hover=False,
            corner_radius=0,
            anchor='w'
        )
        self.pack(pady=5)
