# pylint: disable=C0114, C0103, E0401

from PIL import Image
from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkScrollableFrame, CTkButton
from views.product_frame import ProductFrame

class Home(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white", corner_radius=0)
        self.pack(side="right", fill="both", expand=True)

        hero_image = Image.open("assets/images/hero.jpg")
        image_height = hero_image.size[1]
        hero_image = hero_image.crop((
            0,
            100,
            self.winfo_screenwidth() - 120,
            image_height - 100
        ))
        hero_image = CTkImage(light_image=hero_image, size=(self.winfo_screenwidth(), 500))
        explore_frame = CTkFrame(self, fg_color="#333", corner_radius=0)

        CTkLabel(
            self,
            image=hero_image,
            text=""
        ).pack()

        CTkLabel(
            self,
            text="Featured Products",
            font=('Arial', 25)
        ).pack(pady=40)

        ProductFrame(self)

        explore_frame.pack(fill="both", expand=True)

        CTkLabel(
            explore_frame,
            text="Like what you see?",
            text_color="#ddd",
            font=('Arial', 25)
        ).pack(pady=(40, 40))

        CTkButton(
            explore_frame,
            text="Explore",
            fg_color="white",
            text_color="#333",
            hover_color="#ddd",
            corner_radius=0
        ).pack(pady=(0, 40))
