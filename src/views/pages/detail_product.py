# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkScrollableFrame
from config import app
from views.components.top_bar import TopBar

class DetailProductPage(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, **kwargs):
        super().__init__(app.INSTANCE, **kwargs)

    def render(self):
        """
        Renders the home page.
        """

        TopBar(self).render().pack()

        return self
