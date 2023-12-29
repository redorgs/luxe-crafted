# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame
from config import app
from views.components.top_bar import TopBarComponent
from views.components.checkout_detail import CheckoutDetailComponent
from views.components.table import TableComponent

class CartPage(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'Cart'

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        TableComponent(self).render().pack(side='left', padx=(30,0), pady=(30,0))
        CheckoutDetailComponent(self).render().pack(side='right', padx=30, pady=(30,0), fill='both', expand=True)

        return self
