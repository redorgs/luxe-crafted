# pylint: disable=C0114, E0401, E0611

from importlib import import_module
from functools import partial
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkEntry
from utils.navigation import switch_page
from config import app


class CheckoutDetailComponent(CTkFrame):
    """
    Checkout detail component.
    """

    def __init__(self, master, total, button_text, command, **kwargs):
        super().__init__(master, **kwargs)

        self.total = total
        self.button_text = button_text
        self.command = command

    def __cart_total(self, master):
        """
        Renders the cart total.
        """
        frame = CTkFrame(
            master,
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
            corner_radius=0
        )

        CTkLabel(
            frame,
            text='Cart Total',
            text_color=app.COLOR_DARK,
        ).pack(side='left', padx=(20, 0), pady=20)

        CTkLabel(
            frame,
            text=self.total,
            text_color=app.COLOR_DARK,
        ).pack(side='right', padx=(0, 20), pady=20)

        return frame

    def __coupon_code(self, master):
        """
        Renders the coupon code.
        """
        frame = CTkFrame(master, corner_radius=0)

        CTkLabel(
            frame,
            text='Coupon Code',
        ).pack(side='left', padx=20, pady=20)

        CTkEntry(
            frame,
            placeholder_text='Enter coupon code',
        ).pack(side='right', fill='x', expand=True, padx=20, pady=20)

        return frame

    def __payment_method(self, master):
        """
        Renders the coupon code.
        """
        frame = CTkFrame(master, corner_radius=0)

        CTkLabel(
            frame,
            text='Payment',
        ).pack(side='left', padx=20, pady=20)

        CTkLabel(
            frame,
            text='Cash On Delivery',
        ).pack(side='right', padx=20, pady=20)

        return frame

    def __checkout(self, master):
        """
        Renders the checkout button.
        """
        frame = CTkFrame(
            master,
            corner_radius=0
        )

        CTkButton(
            frame,
            text=self.button_text,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
            hover_color='#222',
            corner_radius=0,
            command=self.command
        ).pack(fill='x', ipady=20)

        return frame

    def render(self):
        """
        Renders the cart total.
        """
        CTkLabel(
            self,
            text='Cart Totals',
            fg_color=app.COLOR_DARK,
        ).pack(fill='x')

        if self.button_text == 'Place Order':
            self.__coupon_code(self).pack(fill='x')
        else:
            self.__payment_method(self).pack(fill='x')

        self.__cart_total(self).pack(fill='x')
        self.__checkout(self).pack(fill='x')

        return self
