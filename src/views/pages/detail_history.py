# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame
from CTkTable import CTkTable
from config import app
from views.components.top_bar import TopBarComponent


class DetailHistoryPage(CTkScrollableFrame):
    """
    The home page of the application.
    """

    def __init__(self, tracking, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'History'

        self.tracking = tracking

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self).render()
        value = [
            ['No', 'Status', 'Description', 'Date'],
        ]

        for i, tracking in enumerate(self.tracking, start=1):
            value.append([
                '    ' + str(i),
                tracking[2],
                tracking[3],
                '   ' + tracking[4].strftime('%Y-%m-%d %H:%M:%S')
            ])   # type: ignore

        value.append(['No', 'Status', 'Description', 'Date'])

        table = CTkTable(
            self,
            row=len(value),
            column=4,
            values=value, justify='left', anchor='w')
        table.pack(fill='both', expand=True, padx=30, pady=30)

        return self
