# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkFrame, CTkLabel, CTkButton
from config import app

class TableComponent(CTkFrame):
    """
    A table component.
    """
    def __init__(self, master, thead, tbody, **kwargs):
        super().__init__(master, **kwargs)

        self.t_head = thead
        self.t_body = tbody

    def __thead(self, master):
        """
        Renders the table header.
        """
        frame = CTkFrame(master)

        for thead in self.t_head:
            CTkLabel(
                frame,
                text=thead[0],
                width=thead[1],
                fg_color=app.COLOR_DARK,
                bg_color=app.COLOR_DARK,
            ).pack(side='left', ipadx=30, ipady=20)

        return frame

    def __row(self, master, is_stripe, data):
        """
        Renders a row of the table.
        """
        frame = CTkFrame(
            master,
            corner_radius=0
        )

        for row in data:
            if data[-1] == row:
                button = CTkFrame(
                    frame,
                    corner_radius=0,
                    fg_color='#333' if is_stripe else 'transparent',
                    bg_color='#333' if is_stripe else 'transparent',
                )

                CTkButton(
                    button,
                    text=row[0],
                    width=row[1],
                    fg_color='#333' if is_stripe else 'transparent',
                    hover_color=row[2],
                ).pack(pady=16) # Windows: 16, Mac: 20

                button.pack(side='left', ipadx=22)
            else:
                CTkLabel(
                    frame,
                    text=row[0],
                    width=row[1],
                    fg_color='#333' if is_stripe else 'transparent',
                    bg_color='#333' if is_stripe else 'transparent',
                ).pack(side='left', ipadx=30, ipady=20)

        return frame

    def __tbody(self, master):
        """
        Renders the table body.
        """
        frame = CTkFrame(master)
        stripe = False
        for data in self.t_body:
            self.__row(frame, stripe, data).pack()
            stripe = not stripe

        return frame

    def render(self):
        """
        Renders the component.
        """
        self.__thead(self).pack()
        self.__tbody(self).pack()

        return self
