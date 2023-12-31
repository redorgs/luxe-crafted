# pylint: disable=C0114, E0401, E0611

from functools import partial
from customtkinter import CTkScrollableFrame
from config import app
from utils.db import DB
from views.components.top_bar import TopBarComponent
from views.components.table import TableComponent
from views.pages.detail_history import DetailHistoryPage
from utils.navigation import switch_page


class HistoryPage(CTkScrollableFrame):
    """
    The home page of the application.
    """

    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'History'

        self.thead = [
            ['Order', 630],
            ['Status', 150],
            ['', 50],
        ]
        self.tbody = []

        for history in DB('purchase_history').get():
            tracking = DB('order_tracking').where(
                'purchase_history_id', history[0]
            ).orderBy('id', 'DESC').get()

            self.tbody.append([
                [f'Order #{history[0]}', 630],
                [tracking[0][2], 150],
                ['View', 50, app.COLOR_DARK, partial(
                    switch_page, partial(
                        DetailHistoryPage,
                        tracking
                    )
                )]
            ])

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        TableComponent(self, self.thead, self.tbody).render().pack(
            side='left', padx=(30, 0), pady=(30, 0)
        )

        return self
