# pylint: disable=C0114, E0401, E0611

from functools import partial
from customtkinter import CTkFrame, CTkLabel, CTkButton
from config import app
from utils.navigation import switch_page
from views.pages.home import HomePage
from views.pages.products import ProductsPage
from views.pages.cart import CartPage
from views.pages.history import HistoryPage

class Navigation(CTkFrame):
    """
    The navigation of the application.
    """
    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE ,**kwargs)

        self.configure(
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
        )

    def __logo(self):
        """
        The logo of the application.
        """
        return CTkLabel(
            self,
            text=app.NAME,
            text_color=app.COLOR_PRIMARY,
            font=("Segoe Script", 20),
        )

    def __list(self):
        """
        The links of the application.
        """
        frame = CTkFrame(self)

        self.__link(frame, HomePage)
        self.__link(frame, ProductsPage)

        return frame

    def __link(self, master, to):
        """
        The button of the link.
        """
        if app.ACTIVE_PAGE.title == to().title:
            button_color = app.COLOR_SECONDARY_DARK
        else:
            button_color = app.COLOR_DARK

        button = CTkButton(
            master,
            text=to().title,
            anchor='center',
            fg_color=button_color,
            bg_color=button_color,
            hover=False,
            width=200,
            command=partial(switch_page, to)
        )
        button.pack(ipady=5)

        return button

    def __menu(self):
        """
        The links of the application.
        """
        frame = CTkFrame(self)

        self.__link(frame, CartPage)
        self.__link(frame, HistoryPage)

        return frame

    def render(self):
        """
        Render the navigation.
        """
        self.__logo().pack(pady=20)
        self.__list().pack()
        self.__menu().pack(side="bottom")

        return self
