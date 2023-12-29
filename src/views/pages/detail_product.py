# pylint: disable=C0114, E0401, E0611

import importlib
from tkinter import Canvas
from customtkinter import CTkScrollableFrame, CTkFrame, CTkLabel, CTkButton, CTkTabview
from CTkTable import CTkTable
from config import app
from views.components.top_bar import TopBarComponent
from views.components.image import ImageComponent
from views.components.rating import RatingComponent


class DetailProductPage(CTkScrollableFrame):
    """
    The detail product page of the application.
    """

    def __init__(self, product, **kwargs):
        super().__init__(app.APP_INSTANCE, **kwargs)

        self.configure(corner_radius=0)
        self.title = 'Products'

        self.product = product

    def __product_name(self, master):
        """
        Renders the name section.
        """
        return CTkLabel(
            master,
            text=self.product[1],
            font=("Verdana", 20),
        )

    def __product_price(self, master):
        """
        Renders the price section.
        """
        return CTkLabel(
            master,
            text=self.product[2],
            font=("Verdana", 20, 'bold'),
        )

    def __product_rating(self, master):
        """
        Renders the rating section.
        """
        frame = CTkFrame(master)

        RatingComponent(
            frame,
            fg_color='transparent',
            bg_color='transparent'
        ).render().pack()

        CTkLabel(
            frame,
            text="(23 Reviews)",
            font=("Verdana", 11),
        ).pack(side="left", padx=(10, 0))

        return frame

    def __product_description(self, master):
        """
        Renders the description section.
        """
        return CTkLabel(
            master,
            text=self.product[3],
            font=("Verdana", 14),
            wraplength=420,
            justify="left"
        )

    def __add_product_to_cart(self, master):
        """
        Renders the add product to cart section.
        """
        frame = CTkFrame(master)

        CTkButton(
            frame,
            text="-",
            width=30,
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
            text_color=app.COLOR_SECONDARY_DARK,
            hover=False
        ).pack(side="left")

        CTkLabel(
            frame,
            text="1",
            font=("Verdana", 14),
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
            text_color=app.COLOR_SECONDARY_DARK,
        ).pack(side="left")

        CTkButton(
            frame,
            text="+",
            width=30,
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
            text_color=app.COLOR_SECONDARY_DARK,
            hover=False
        ).pack(side="left")

        CTkButton(
            frame,
            text="Add To Cart",
            width=30,
            fg_color=app.COLOR_LIGHT,
            bg_color=app.COLOR_LIGHT,
            text_color=app.COLOR_SECONDARY_DARK,
            hover=False
        ).pack(side="left", padx=(20, 0), ipadx=20)

        return frame

    def __product_description_section(self, master):
        """
        Renders the description section.
        """
        frame = CTkFrame(
            master,
            fg_color='transparent',
            bg_color='transparent',
        )
        canvas = Canvas(
            frame,
            height=1,
            bg=app.COLOR_SECONDARY_LIGHT,
            highlightthickness=0
        )

        self.__product_name(frame).pack(anchor="w")
        self.__product_price(frame).pack(anchor="w", pady=(10, 0))
        self.__product_rating(frame).pack(anchor="w", pady=(10, 0))
        self.__product_description(frame).pack(anchor="w", pady=(10, 0))

        canvas.pack(anchor="w", fill='x', pady=30)
        canvas.create_line(0, 0, 0, 0)

        self.__add_product_to_cart(frame).pack(anchor="w")

        return frame

    def __image_option(self, master):
        """
        Renders the image option section.
        """
        frame = CTkFrame(master)

        ImageComponent(
            frame,
            'assets/images/products/' + str(self.product[9]),
            (100, 100)
        ).render().pack(pady=(0, 10))
        ImageComponent(
            frame,
            'assets/images/products/' + str(self.product[9]),
            (100, 100)
        ).render().pack(pady=(0, 10))
        ImageComponent(
            frame,
            'assets/images/products/' + str(self.product[9]),
            (100, 100)
        ).render().pack(pady=(0, 10))
        ImageComponent(
            frame,
            'assets/images/products/' + str(self.product[9]),
            (100, 100)
        ).render().pack()

        return frame

    def __detail_section(self):
        """
        Renders the detail section.
        """
        frame = CTkFrame(self)

        self.__image_option(frame).pack(side="left")
        ImageComponent(
            frame,
            'assets/images/products/' + str(self.product[9]),
            (430, 430)
        ).render().pack(side="left", padx=(10, 0))
        self.__product_description_section(frame).pack(padx=(20, 0))

        return frame

    def __tab_additional_information(self, tab):
        """
        Renders the tab section.
        """
        value = [
            ['Color', self.product[4]],
            ['Size', self.product[5]],
            ['Material', self.product[6]],
            ['Weight', self.product[7]],
            ['Dimension', self.product[8]],
        ]

        table = CTkTable(tab, row=len(value), column=2, values=value)
        table.pack(pady=(20, 0))

    def __comment_description(self, master):
        """
        Renders the comment description section.
        """
        frame = CTkFrame(
            master,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK
        )

        RatingComponent(
            frame,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK
        ).render().pack(anchor="w")

        CTkLabel(
            frame,
            text="by Vans",
            font=("Verdana", 11),
            wraplength=400,
            justify="left"
        ).pack(anchor="w")

        CTkLabel(
            frame,
            text="Sed egestas, ante et vulputate volutpat, eros pede semper est, vitae luctus metus libero eu augue. Morbi purus liberpuro ate vol faucibus adipiscing.",
            font=("Verdana", 11),
            wraplength=400,
            justify="left"
        ).pack(anchor="w")

        return frame

    def __comment(self, master):
        """
        Renders the comment section.
        """
        frame = CTkFrame(
            master,
            fg_color=app.COLOR_DARK,
            bg_color=app.COLOR_DARK,
        )

        ImageComponent(
            frame,
            'assets/images/users/user1.jpg',
            (50, 50)
        ).render().pack(side="left", anchor="nw", padx=(20, 0), pady=(20, 0))

        self.__comment_description(frame).pack(
            side="left", padx=20, pady=(15, 20)
        )

        return frame

    def __tab_reviews(self, tab):
        """
        Renders the reviews section.
        """
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)
        self.__comment(tab).pack(pady=10)

    def __bottom_section(self):
        """
        Renders the bottom section.
        """
        frame = CTkTabview(
            self,
            segmented_button_fg_color=app.COLOR_DARK,
            segmented_button_selected_color=app.COLOR_SECONDARY_DARK,
            segmented_button_unselected_color=app.COLOR_DARK,
            segmented_button_selected_hover_color=app.COLOR_SECONDARY_DARK,
            segmented_button_unselected_hover_color=app.COLOR_DARK,
            text_color=app.COLOR_LIGHT,
        )

        self.__tab_additional_information(frame.add('Additional Information'))
        self.__tab_reviews(frame.add('Reviews'))

        return frame

    def render(self):
        """
        Renders the home page.
        """

        TopBarComponent(self, importlib.import_module(
            'views.pages.products'
        ).ProductsPage).render()
        self.__detail_section().pack(anchor="w", padx=30, pady=30)
        self.__bottom_section().pack(padx=30, pady=30)

        return self
