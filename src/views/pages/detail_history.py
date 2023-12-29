# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame
from CTkTable import CTkTable
from config import app
from views.components.top_bar import TopBarComponent

class DetailHistoryPage(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'History'

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        history = [
            ['1. Order #8912 placed on 12/12/2020'],
            ['2. Order #8912 processed on 12/12/2020'],
            ['3. Order #8912 shipped on 12/12/2020'],
            ['4. Order #8912 delivered on 12/12/2020'],
        ]

        value = [['Recent History']]

        for item in history:
            text = '    ' + item[0]
            value.append([text])

        value.append(['Older History'])

        table = CTkTable(self, row=len(value), column=1, values=value, justify='left', anchor='w')
        table.pack(fill='both', expand=True, padx=30, pady=(30,0))

        return self
