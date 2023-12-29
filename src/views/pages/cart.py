# pylint: disable=C0114, E0401, E0611

from functools import partial
import importlib
from customtkinter import CTkScrollableFrame
from config import app
from utils.db import DB
from utils.navigation import switch_page
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
        self.total = 0

        product_cart = DB('product_cart').where('user_id', 1).get()
        self.thead = [
            ['Product', 150],
            ['Price', 50],
            ['Quantity', 50],
            ['Subtotal', 50],
            ['', 50],
        ]

        self.tbody = []

        for product in product_cart:
            product_data = DB('products').where('id', product[2]).get()[0]
            subtotal = product[3] * product_data[2]  # type: ignore
            self.total += subtotal
            self.tbody.append([
                [product_data[1], 150],
                [product_data[2], 50],
                [product[3], 50],
                [subtotal, 50],
                [
                    'Remove',
                    50,
                    app.COLOR_DANGER,
                    partial(
                        self.__remove_product, product[0]
                    )
                ]
            ])

    def __remove_product(self, product_id):
        """
        Removes a product from the cart.
        """
        DB('product_cart').where('id', product_id).delete()
        switch_page(importlib.import_module('views.pages.cart').CartPage)

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        TableComponent(self, self.thead, self.tbody).render().pack(
            side='left', padx=(30, 0), pady=(30, 0), anchor='n')
        CheckoutDetailComponent(self, self.total, 'Place Order', partial(
            switch_page,
            partial(
                importlib.import_module(
                    'views.pages.checkout'
                ).CheckoutPage,
                self.total
            )
        )).render().pack(
            side='right', padx=30, pady=(30, 0), fill='both', expand=True)

        return self
