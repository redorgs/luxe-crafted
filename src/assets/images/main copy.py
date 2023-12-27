"""Import customtkinter"""
from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, set_appearance_mode, CTkImage, CTkScrollableFrame
from PIL import Image

# set_appearance_mode("dark")
set_appearance_mode("light")

class NavigationButton(CTkButton):
    """
    A custom button class that inherits from CTkButton
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color='transparent',
            text_color='#4a4a4a',
            hover=False,
            corner_radius=0,
            anchor='w'
        )
        self.pack(pady=5)

class NavigationFrame(CTkFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(pady=10)

        NavigationButton(self, text="Home")
        NavigationButton(self, text="Products")
        NavigationButton(self, text="About")


class LeftPanel(CTkFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.pack(side="left", fill="y", padx=30, pady=30)
        logo_image = CTkImage(light_image=Image.open("logo.png"), size=(110, 20))

        CTkLabel(self, image=logo_image, text="").pack()
        NavigationFrame(self)

class ProductCard(CTkFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent", corner_radius=0)
        self.grid(padx=18, pady=20)
        self.product_image = CTkImage(light_image=Image.open("product1.jpg"), size=(230, 230))

        CTkLabel(self, image=self.product_image, text="").pack()
        CTkLabel(self, text="Kursi").pack()
        CTkLabel(self, text="IDR 50.000").pack()
        CTkButton(self, text="Add to Cart", fg_color="black", hover_color="#555", corner_radius=0).pack(fill="both")

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

class WhatTheySay(CTkFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#333", corner_radius=0)
        self.pack(fill="both", expand=True)

        CTkLabel(self, text="Like what you see?", text_color="#ddd", font=('Arial', 25)).pack(pady=(40, 40))
        CTkButton(self, text="Explore", fg_color="white", text_color="#333", hover_color="#ddd", corner_radius=0).pack(pady=(0, 40))

class RightPanel(CTkScrollableFrame):
    """
    A custom frame class that inherits from CTkFrame
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white", corner_radius=0)
        self.pack(side="right", fill="both", expand=True)
        hero_image = Image.open("hero.jpg")
        image_height = hero_image.size[1]

        image = hero_image.crop((
            0,
            100,
            self.winfo_screenwidth() - 120,
            image_height - 100
        ))
        self.ctk_hero_image = CTkImage(light_image=image, size=(self.winfo_screenwidth(), 500))

        CTkLabel(self, image=self.ctk_hero_image, text="").pack()
        CTkLabel(self, text="Featured Products", font=('Arial', 25)).pack(pady=40)
        ProductFrame(self)
        WhatTheySay(self)

class App(CTk):
    """
    A custom app class that inherits from CTk
    """
    def __init__(self):
        super().__init__()
        self.title("E Commerce")
        self.geometry("1280x720")
        self.resizable(0,0)

        LeftPanel(self)
        RightPanel(self)

app = App()
app.mainloop()
