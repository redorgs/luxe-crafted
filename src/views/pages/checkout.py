# pylint: disable=C0114, E0401, E0611

from functools import partial
import importlib
from customtkinter import CTkScrollableFrame, CTkFrame, CTkLabel, CTkEntry
from config import app
from utils.db import DB
from utils.navigation import switch_page
from views.components.top_bar import TopBarComponent
from views.components.checkout_detail import CheckoutDetailComponent


class CheckoutPage(CTkScrollableFrame):
    """
    The home page of the application.
    """

    def __init__(self, total, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'Cart'

        self.total = total

    def __input(self, master, width):
        """
        Renders the input.
        """
        frame = CTkFrame(master, corner_radius=0, fg_color='transparent')

        CTkLabel(
            frame,
            text='Name',
        ).pack(anchor='w')

        CTkEntry(
            frame,
            placeholder_text='Enter your name',
            width=width
        ).pack()

        return frame

    def __row(self, master):
        """
        Renders the row.
        """
        frame = CTkFrame(master, corner_radius=0, fg_color='transparent')

        self.__input(frame, 300).pack(side='left', padx=(0, 30))
        self.__input(frame, 300).pack(side='right')

        return frame

    def __form(self, master):
        """
        Renders the form.
        """
        frame = CTkFrame(master, corner_radius=0)

        CTkLabel(
            frame,
            text='Billing Details',
        ).pack(anchor='w')

        self.__row(frame).pack(pady=(0, 20))
        self.__row(frame).pack(pady=(0, 20))
        self.__row(frame).pack(pady=(0, 20))
        self.__row(frame).pack(pady=(0, 20))
        self.__row(frame).pack(pady=(0, 20))
        self.__row(frame).pack()

        return frame

    def __checkout_process(self):
        """
        The checkout process.
        """
        purchase_history_id = DB('purchase_history').create({
            'user_id': app.USER_LOGIN
        })
        DB('order_tracking').create({
            'purchase_history_id': purchase_history_id,
            'status': 'Pending',
            'description': 'Your order is being processed.'
        })
        DB('product_cart').where('user_id', app.USER_LOGIN).delete()
        switch_page(
            partial(
                importlib.import_module(
                    'views.pages.detail_history').DetailHistoryPage,
                DB('order_tracking').where(
                    'purchase_history_id',
                    purchase_history_id
                ).get()
            )
        )

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        self.__form(self).pack(side='left', padx=(30, 0), pady=(30, 0))
        CheckoutDetailComponent(
            self,
            self.total,
            'Checkout',
            self.__checkout_process
        ).render().pack(
            side='right',
            padx=30,
            pady=(30, 0),
            fill='both',
            expand=True
        )

        return self
