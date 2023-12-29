# pylint: disable=C0114, E0401, E0611

from functools import partial
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

        self.thead = [
            ['Product', 150],
            ['Price', 50],
            ['Quantity', 50],
            ['Subtotal', 50],
            ['', 50],
        ]
        self.tbody = [
            [
                ['Fancy Chair', 150],
                ['50000', 50],
                ['1', 50],
                ['50000', 50],
                ['Remove', 50, app.COLOR_DANGER, partial(print, 'hello')]
            ],
            [
                ['Fancy Chair', 150],
                ['50000', 50],
                ['1', 50],
                ['50000', 50],
                ['Remove', 50, app.COLOR_DANGER, partial(print, 'hello')]
            ],
            [
                ['Fancy Chair', 150],
                ['50000', 50],
                ['1', 50],
                ['50000', 50],
                ['Remove', 50, app.COLOR_DANGER, partial(print, 'hello')]
            ],
        ]

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        TableComponent(self, self.thead, self.tbody).render().pack(side='left', padx=(30,0), pady=(30,0), anchor='n')
        CheckoutDetailComponent(self).render().pack(side='right', padx=30, pady=(30,0), fill='both', expand=True)

        return self
