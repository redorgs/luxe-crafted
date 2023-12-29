# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame, CTkFrame
from config import app
from utils.db import DB
from views.components.product import Card


class ProductsPage(CTkScrollableFrame):
    """
    The home page of the application.
    """

    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'Products'

    def __products(self):
        """
        Renders all products.
        """
        frame = CTkFrame(self)

        products = DB('products').get()

        for i in range(0, len(products), 6):
            product_chunk = products[i:i+6]
            for j, product in enumerate(product_chunk):
                Card(
                    frame,
                    product,
                ).set_size('sm').render().grid(row=i//6, column=j)

        return frame

    def render(self):
        """
        Renders the home page.
        """

        self.__products().pack()

        return self
