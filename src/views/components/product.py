# pylint: disable=C0114, E0401, E0611

from functools import partial
from customtkinter import CTkFrame, CTkLabel, CTkButton
from config import app
from utils.navigation import switch_page
from views.pages.detail_product import DetailProductPage
from views.components.image import ImageComponent

class Card(CTkFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, title, price, img_path, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
        )
        self.grid(padx=18, pady=20)
        self.title = title
        self.price = price
        self.img_path = img_path
        self.__size = 'md'

    def set_size(self, size):
        """
        Sets the size of the card.
        """
        self.__size = size

        return self

    def render(self):
        """
        Renders the product card.
        """
        if self.__size == 'md':
            ImageComponent(self, self.img_path, (220, 220)).render().pack()
        elif self.__size == 'sm':
            ImageComponent(self, self.img_path, (100, 100)).render().pack()

        CTkLabel(
            self,
            text=self.title,
            text_color=app.COLOR_DARK,
            font=("Verdana", 14),
        ).pack()

        CTkLabel(
            self,
            text=self.price,
            text_color=app.COLOR_SECONDARY_DARK,
            font=("Verdana", 12),
        ).pack()

        CTkButton(
            self,
            text="View",
            font=("Verdana", 12),
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
            hover_color=app.COLOR_SECONDARY_DARK,
            corner_radius=0,
            command=partial(switch_page, DetailProductPage)
        ).pack(fill="both", ipady=10, pady=(10, 0))

        return self
