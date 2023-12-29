# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame, CTkFrame
from config import app
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

        for i in range(0, 10):
            Card(frame, 'Chairs', '50000', "assets/images/product2.jpg").set_size('sm').render().grid(row=i, column=0)
            Card(frame, 'Bean Bags', '75000', "assets/images/product1.jpg").set_size('sm').render().grid(row=i, column=1)
            Card(frame, 'Sofas', '100000', "assets/images/product1.jpg").set_size('sm').render().grid(row=i, column=2)
            Card(frame, 'Tables', '150000', "assets/images/product1.jpg").set_size('sm').render().grid(row=i, column=3)
            Card(frame, 'Chairs', '50000', "assets/images/product1.jpg").set_size('sm').render().grid(row=i, column=4)
            Card(frame, 'Bean Bags', '75000', "assets/images/product1.jpg").set_size('sm').render().grid(row=i, column=5)


        return frame

    def render(self):
        """
        Renders the home page.
        """

        self.__products().pack()

        return self
