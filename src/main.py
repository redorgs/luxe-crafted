# pylint: disable=C0114, E0401, E0611

from app import App
from views.pages.home import HomePage
from config import app
from utils.navigation import switch_page

if __name__ == "__main__":
    app.APP_INSTANCE = App()

    switch_page(HomePage)

    app.APP_INSTANCE.mainloop()
