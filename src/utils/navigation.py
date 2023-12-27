# pylint: disable=C0114

from config import app

def switch_page(view):
    """Switch to a new page."""
    if app.ACTIVE_PAGE:
        app.ACTIVE_PAGE.pack_forget()

    app.ACTIVE_PAGE = view().render()
    app.ACTIVE_PAGE.pack(side="right", fill="both", expand=True)
