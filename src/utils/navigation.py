# pylint: disable=C0114

from importlib import import_module
from config import app

def switch_page(view):
    """Switch to a new page."""
    if app.ACTIVE_PAGE:
        app.ACTIVE_PAGE.pack_forget()

    app.ACTIVE_PAGE = view().render()
    app.ACTIVE_PAGE.pack(side="right", fill="both", expand=True)

    if app.NAV_INSTANCE:
        app.NAV_INSTANCE.pack_forget()

    app.NAV_INSTANCE = import_module("views.components.navigation").Navigation().render()
    app.NAV_INSTANCE.pack(side="left", fill="y", expand=False)
