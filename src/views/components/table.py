# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkFrame, CTkLabel, CTkButton
from config import app

class TableComponent(CTkFrame):
    """
    A table component.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def __thead(self, master):
        """
        Renders the table header.
        """
        frame = CTkFrame(master)

        CTkLabel(
            frame,
            text='Product',
            width=150,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='Price',
            width=50,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='Quantity',
            width=50,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='Subtotal',
            width=50,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='',
            width=50,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
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
            fg_color='transparent' if is_even else '#333',
            bg_color='transparent' if is_even else '#333',
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='50000',
            width=50,
            fg_color='transparent' if is_even else '#333',
            bg_color='transparent' if is_even else '#333',
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='1',
            width=50,
            fg_color='transparent' if is_even else '#333',
            bg_color='transparent' if is_even else '#333',
        ).pack(side='left', ipadx=30, ipady=20)
        CTkLabel(
            frame,
            text='50000',
            width=50,
            fg_color='transparent' if is_even else '#333',
            bg_color='transparent' if is_even else '#333',
        ).pack(side='left', ipadx=30, ipady=20)

        button = CTkFrame(
            frame,
            corner_radius=0,
            fg_color='transparent' if is_even else '#333',
            bg_color='transparent' if is_even else '#333',
        )

        CTkButton(
            button,
            text='Remove',
            width=0,
            fg_color='transparent' if is_even else '#333',
            hover_color=app.COLOR_DANGER,
        ).pack(pady=16) # Windows: 16, Mac: 20

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

    def render(self):
        """
        Renders the component.
        """
        self.__thead(self).pack()
        self.__tbody(self).pack()

        return self
