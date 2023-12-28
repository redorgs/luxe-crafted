# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame, CTkFrame, CTkLabel, CTkButton, CTkEntry
from config import app
from views.components.top_bar import TopBarComponent

class CartPage(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'Cart'

    def __thead(self, master):
        """
        Renders the table header.
        """
        frame = CTkFrame(master)

        CTkLabel(
            frame,
            text='Product',
            width=150,
            fg_color=app.COLOR_DARK
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='Price',
            width=50,
            fg_color=app.COLOR_DARK
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='Quantity',
            width=50,
            fg_color=app.COLOR_DARK
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='Subtotal',
            width=50,
            fg_color=app.COLOR_DARK
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='',
            width=50,
            fg_color=app.COLOR_DARK
        ).pack(side='left', ipadx=30, ipady=20)

        return frame

    def __row(self, master, is_even):
        """
        Renders a row of the table.
        """
        frame = CTkFrame(
            master,
            corner_radius=0
        )

        CTkLabel(
            frame,
            text='Fancy Chair',
            width=150,
            fg_color='transparent' if is_even else app.COLOR_DARK,
            bg_color='transparent' if is_even else app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='50000',
            width=50,
            fg_color='transparent' if is_even else app.COLOR_DARK,
            bg_color='transparent' if is_even else app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='1',
            width=50,
            fg_color='transparent' if is_even else app.COLOR_DARK,
            bg_color='transparent' if is_even else app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='50000',
            width=50,
            fg_color='transparent' if is_even else app.COLOR_DARK,
            bg_color='transparent' if is_even else app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)

        button = CTkFrame(
            frame,
            corner_radius=0,
            fg_color='transparent' if is_even else app.COLOR_DARK,
            bg_color='transparent' if is_even else app.COLOR_DARK,
        )

        CTkButton(
            button,
            text='Remove',
            width=0,
            fg_color='transparent' if is_even else app.COLOR_DARK,
            hover_color=app.COLOR_DANGER,
        ).pack(pady=16)

        button.pack(side='left', ipadx=22)

        return frame

    def __tbody(self, master):
        """
        Renders the table body.
        """
        frame = CTkFrame(master)

        for i in range(10):
            self.__row(frame, i % 2 == 0).pack()

        return frame

    def __table(self, master):
        """
        Renders all products.
        """
        frame = CTkFrame(master)

        self.__thead(frame).pack()
        self.__tbody(frame).pack()

        return frame

    def __cart_total(self, master):
        """
        Renders the cart total.
        """
        frame = CTkFrame(
            master,
            fg_color=app.COLOR_SECONDARY_LIGHT,
            bg_color=app.COLOR_SECONDARY_LIGHT,
            corner_radius=0
        )

        CTkLabel(
            frame,
            text='Cart Total',
            text_color=app.COLOR_DARK,
        ).pack(side='left', padx=(20,0), pady=20)

        CTkLabel(
            frame,
            text='50000',
            text_color=app.COLOR_DARK,
        ).pack(side='right', padx=(0,20), pady=20)

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

    def __checkout(self, master):
        """
        Renders the checkout button.
        """
        frame = CTkFrame(
            master,
            fg_color=app.COLOR_SECONDARY_LIGHT,
            corner_radius=0
        )

        CTkButton(
            frame,
            text='Checkout',
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
            hover_color='#222',
            corner_radius=0
        ).pack(fill='x', ipady=20)

        return frame

    def __cart_total_frame(self, master):
        """
        Renders the cart total.
        """
        frame = CTkFrame(master)

        CTkLabel(
            frame,
            text='Cart Totals',
            fg_color=app.COLOR_DARK,
        ).pack(fill='x')

        self.__coupon_code(frame).pack(fill='x')
        self.__cart_total(frame).pack(fill='x')
        self.__checkout(frame).pack(fill='x')

        return frame

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        self.__table(self).pack(side='left', padx=(30,0), pady=(30,0))
        self.__cart_total_frame(self).pack(side='right', padx=30, pady=(30,0), fill='both', expand=True)

        return self
