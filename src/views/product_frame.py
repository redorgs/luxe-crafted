# pylint: disable=C0114, C0103, E0401

from PIL import Image
from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkButton

class ProductCard(CTkFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.grid(padx=18, pady=20)
        self.product_image = CTkImage(
            light_image=Image.open("assets/images/product1.jpg"),
            size=(230, 230)
        )

        CTkLabel(self, image=self.product_image, text="").pack()
        CTkLabel(self, text="Kursi").pack()
        CTkLabel(self, text="IDR 50.000").pack()
        CTkButton(
            self,
            text="Add to Cart",
            fg_color="black",
            hover_color="#555",
            corner_radius=0
        ).pack(fill="both")

class ProductFrame(CTkFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(fill="both", expand=True)

        ProductCard(self).grid(row=0, column=0)
        ProductCard(self).grid(row=0, column=1)
        ProductCard(self).grid(row=0, column=2)
        ProductCard(self).grid(row=0, column=3)

        ProductCard(self).grid(row=1, column=0)
        ProductCard(self).grid(row=1, column=1)
        ProductCard(self).grid(row=1, column=2)
        ProductCard(self).grid(row=1, column=3)
