# pylint: disable=C0114, C0103, E0401

from customtkinter import  CTkLabel, CTkScrollableFrame, CTkFrame, CTkButton, CTkImage, CTkTabview
from PIL import Image
from views.product_frame import ProductFrame

class DetailProduct(CTkScrollableFrame):
    """
    The home page of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white", corner_radius=0)
        self.pack(side="right", fill="both", expand=True)

        TopBar(self)
        Detail(self)
        Tabbale(self)

class TopBar(CTkFrame):
    """
    The top bar of the application.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(fill="x")

        CTkButton(
            self,
            text="Back",
            width=70,
            fg_color='transparent',
            text_color='#333',
            border_width=1,
            border_color='#333',
            corner_radius=0
        ).pack(side="left", padx=10, pady=10)

class Detail(CTkFrame):
    """
    The detail of the product.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(fill="both", expand=True, pady=30, padx=30)

        Images(self)
        Description(self)

class Images(CTkFrame):
    """
    The images of the product.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(side="left")

        bigger = CTkImage(light_image=Image.open("assets/images/product1.jpg"), size=(300, 300))
        image = CTkImage(light_image=Image.open("assets/images/product1.jpg"), size=(100, 100))

        CTkLabel(self, image=bigger, text="").grid(row=0, column=0, pady=10, padx=10, columnspan=3)  # Modify this line
        CTkLabel(self, image=image, text="").grid(row=1, column=0, pady=10, padx=10)
        CTkLabel(self, image=image, text="").grid(row=1, column=1, pady=10, padx=10)
        CTkLabel(self, image=image, text="").grid(row=1, column=2, pady=10, padx=10)

class Description(CTkFrame):
    """
    The description of the product.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(side="left", anchor="nw")

        CTkLabel(
            self,
            text="Originals Kaval Windbr",
            font=("Arial", 20),
            fg_color="transparent",
            text_color="black",
            corner_radius=0
        ).pack(pady=10)

        Stars(self)

        CTkLabel(
            self,
            text="IDR 120.000,00",
            font=("Arial", 20),
            fg_color="transparent",
            text_color="black",
            corner_radius=0
        ).pack(pady=10)

        CTkLabel(
            self,
            text="Lorem ipsum dolor sit amet, consectetur adipisic elit eiusm tempor incidid ut labore et dolore magna aliqua. Ut enim ad minim venialo quis nostrud exercitation ullamco",
            font=("Arial", 20),
            fg_color="transparent",
            text_color="black",
            corner_radius=0,
            wraplength=400
        ).pack(pady=10)

        AddToChart(self)

class Stars(CTkFrame):
    """
    The stars of the product.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack()

        star = CTkImage(light_image=Image.open("assets/images/star.png"), size=(20, 20))
        CTkLabel(self, image=star, text="").pack(side="left", padx=5)
        CTkLabel(self, image=star, text="").pack(side="left", padx=5)
        CTkLabel(self, image=star, text="").pack(side="left", padx=5)
        CTkLabel(self, image=star, text="").pack(side="left", padx=5)
        CTkLabel(self, image=star, text="").pack(side="left", padx=5)

class AddToChart(CTkFrame):
    """
    The add to chart button of the product.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#333", corner_radius=0)
        self.pack()

        CTkButton(
            self,
            text="+",
            width=70,
            fg_color='#333',
            text_color='white',
            border_width=1,
            border_color='#333',
            corner_radius=0
        ).pack(side="left", padx=10, pady=10)

        CTkLabel(
            self,
            text="1",
            font=("Arial", 20),
            fg_color="transparent",
            text_color="white",
            corner_radius=0
        ).pack(side="left", padx=10, pady=10)

        CTkButton(
            self,
            text="-",
            width=70,
            fg_color='#333',
            text_color='white',
            border_width=1,
            border_color='#333',
            corner_radius=0
        ).pack(side="left", padx=10, pady=10)

        CTkButton(
            self,
            text="Add to chart",
            width=70,
            fg_color='transparent',
            text_color='white',
            border_width=1,
            border_color='#333',
            corner_radius=0
        ).pack(side="right", padx=10, pady=10)

class Tabbale(CTkTabview):
    """
    The tab view of the product.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(padx=20, pady=20)

        self.add("tab 1")  # add tab at the end
        self.add("tab 2")  # add tab at the end
        self.set("tab 2")  # set currently visible tab

        button = CTkButton(master=self.tab("tab 1"))
        button.pack(padx=20, pady=20)