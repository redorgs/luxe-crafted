# pylint: disable=C0114, C0103, E0401

from customtkinter import  CTkLabel, CTkScrollableFrame, CTkFrame, CTkButton, CTkImage, CTkTabview
from PIL import Image
from views.back import TopBar

class Cart(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white", corner_radius=0)
        self.pack(side="right", fill="both", expand=True)

        TopBar(self)
        Table(self)

class Table(CTkFrame):
    """
    The table of the cart.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(fill="both", expand=True)

        CTkLabel(self, text="Image", fg_color='gray', width=100).grid(row=0, column=0, ipady=20, ipadx=20)
        CTkLabel(self, text="Product Name", fg_color='gray').grid(row=0, column=1, ipady=20, ipadx=20)
        CTkLabel(self, text="Unit Price", fg_color='gray').grid(row=0, column=2, ipady=20, ipadx=20)
        CTkLabel(self, text="QTY", fg_color='gray').grid(row=0, column=3, ipady=20, ipadx=20)
        CTkLabel(self, text="Subtotal", fg_color='gray').grid(row=0, column=4, ipady=20, ipadx=20)
        CTkLabel(self, text="Action", fg_color='gray').grid(row=0, column=5, ipady=20, ipadx=20)

        image = CTkImage(light_image=Image.open("assets/images/product1.jpg"), size=(132, 132))
        CTkLabel(self, image=image, text="").grid(row=1, column=0)

        CTkLabel(self, text="Originals Kaval Windbr").grid(row=1, column=1)

        CTkLabel(self, text="Rp. 1.000.000").grid(row=1, column=2)

        CTkLabel(self, text="1").grid(row=1, column=3)

        CTkLabel(self, text="Rp. 1.000.000").grid(row=1, column=4)

        CTkButton(self, text="Remove", fg_color='transparent', text_color='#333', border_width=1, border_color='#333', corner_radius=0).grid(row=1, column=5)