# pylint: disable=C0114, E0401, E0611

from PIL import Image
from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkScrollableFrame, CTkButton
from utils.db import DB
from views.components.product import Card
from config import app


class HomePage(CTkScrollableFrame):
    """
    The home page of the application.
    """

    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'Home'

    def __hero(self):
        """
        Renders the hero section of the home page.
        """
        hero_image = Image.open("assets/images/backgrounds/hero.png")
        hero_image = CTkImage(
            light_image=hero_image,
            size=(1065, 550)
        )

        return CTkLabel(
            self,
            image=hero_image,
            text=""
        )

    def __section_title(self):
        """
        Renders the section title of the home page.
        """
        return CTkLabel(
            self,
            text="Featured Products",
            font=("Verdana", 20),
        )

    def __featured_products(self):
        """
        Renders the featured products of the home page.
        """
        frame = CTkFrame(self)

        products = DB('products').get()

        for i, product in enumerate(products[:4]):
            Card(frame, product).render().grid(row=0, column=i)

        return frame

    def __banner(self):
        """
        Renders the banner of the home page.
        """
        frame = CTkFrame(
            self,
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
        )

        CTkLabel(
            frame,
            text="Discover the latest trends in fashion and lifestyle.",
            text_color=app.COLOR_SECONDARY_DARK,
            font=("Verdana", 25, "bold"),
        ).pack(pady=(40, 0))

        CTkButton(
            frame,
            text="Discover",
            fg_color=app.COLOR_SECONDARY_DARK,
            bg_color=app.COLOR_SECONDARY_DARK,
            hover_color=app.COLOR_DARK,
        ).pack(pady=(30, 50))

        return frame

    def render(self):
        """
        Renders the home page.
        """
        self.__hero().pack()
        self.__section_title().pack(pady=40)
        self.__featured_products().pack(pady=(0, 40))
        self.__banner().pack(fill='both')

        return self
