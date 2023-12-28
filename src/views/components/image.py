# pylint: disable=C0114, E0401, E0611

from customtkinter import CTkLabel, CTkImage
from PIL import Image

class ImageComponent(CTkLabel):
    """
    The image component that is used to display images.
    """
    def __init__(self, master, img_path, size, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            image=CTkImage(
                light_image=Image.open(img_path),
                size=size
            ),
            text=""
        )

    def render(self):
        """
        Renders the images.
        """
        return self
