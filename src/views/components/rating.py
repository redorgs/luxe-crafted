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
        for i in range(5):
            ImageComponent(
                self,
                'assets/images/icons/star.png',
                (15, 15)
            ).render().pack(side="left", padx=0 if i == 0 else (5, 0))

        return self
