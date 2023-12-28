# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkFrame
from views.components.image import ImageComponent

class RatingComponent(CTkFrame):
    """
    The rating component that is used to display ratings.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def render(self):
        """
        Renders the rating.
        """
        ImageComponent(self, 'assets/images/star.png', (15, 15)).render().pack(side="left")
        ImageComponent(self, 'assets/images/star.png', (15, 15)).render().pack(side="left", padx=(5,0))
        ImageComponent(self, 'assets/images/star.png', (15, 15)).render().pack(side="left", padx=(5,0))
        ImageComponent(self, 'assets/images/star.png', (15, 15)).render().pack(side="left", padx=(5,0))
        ImageComponent(self, 'assets/images/star.png', (15, 15)).render().pack(side="left", padx=(5,0))

        return self
