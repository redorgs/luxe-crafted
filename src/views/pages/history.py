# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame
from config import app
from views.components.top_bar import TopBarComponent
from views.components.table import TableComponent

class HistoryPage(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'History'

        self.thead = [
            ['Order', 660],
            ['Status', 150],
            ['', 50],
        ]
        self.tbody = [
            [
                ['Order #8912', 660],
                ['Processing', 150],
                ['View', 50, app.COLOR_DARK]
            ],
            [
                ['Ordeasfasdfr #8912', 660],
                ['Processing', 150],
                ['View', 50, app.COLOR_DARK]
            ],
            [
                ['Order aksjdhf lkasdfl#8912', 660],
                ['Processing', 150],
                ['View', 50, app.COLOR_DARK]
            ],
            [
                ['Order a sdf#8912', 660],
                ['Processing', 150],
                ['View', 50, app.COLOR_DARK]
            ],
        ]

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        TableComponent(self, self.thead, self.tbody).render().pack(side='left', padx=(30,0), pady=(30,0))

        return self
