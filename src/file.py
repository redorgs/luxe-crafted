import tkinter
import customtkinter
from functools import partial
from PIL import Image, ImageTk

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    frames = {}
    current = None
    bg = ""

    def __init__(self):
        super().__init__()
        self.bg = self.cget("fg_color")
        self.title("Product Page")

        # screen size
        self.geometry("800x600")

        # root!
        main_container = customtkinter.CTkFrame(self, corner_radius=8, fg_color=self.bg)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=8, pady=8)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkFrame(main_container, width=280, corner_radius=8, fg_color=self.bg)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=18, pady=10)

        # right side panel -> to show the frame
        self.right_side_panel = customtkinter.CTkFrame(main_container, corner_radius=8, fg_color="#212121")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        self.right_side_panel.configure(border_width = 1)
        self.right_side_panel.configure(border_color = "#323232")

        # Create the product page menu and its page
        self.create_nav(self.left_side_panel, "Product Page", "white")
        # Create the product list page menu and its page
        self.create_nav(self.left_side_panel, "Product List", "white")
        # Create the user profile page menu and its page
        self.create_nav(self.left_side_panel, "User Profile", "white")
        # Create the cart page menu and its page
        self.create_nav(self.left_side_panel, "Cart", "white")
        # Create the checkout page menu and its page
        self.create_nav(self.left_side_panel, "Checkout", "white")
        # Add this line in the __init__ method to create a button for the tracking page
        self.create_nav(self.left_side_panel, "Tracking Page", "white")
        # Add this line in the __init__ method to create a button for the store profile page
        self.create_nav(self.left_side_panel, "Store Profile", "white")

    # button to select the correct frame
    def frame_selector_bt(self, parent, frame_id):
        # create frame
        bt_frame = customtkinter.CTkButton(parent)
        # style frame
        bt_frame.configure(height = 40)
        # creates a text label
        bt_frame.configure(text = frame_id)
        bt_frame.configure(command =  partial(self.toggle_frame_by_id, frame_id))
        # set layout
        bt_frame.pack(pady = 3)
        return bt_frame

    # create the frame
    def create_frame(self, frame_id, color):
        frame = customtkinter.CTkFrame(self.right_side_panel, fg_color=self.cget("fg_color"))
        frame.configure(corner_radius = 8)
        frame.configure(fg_color = color)
        frame.configure(border_width = 2)
        frame.configure(border_color = "#323232")
        frame.padx = 8

        if frame_id == "Product Page":
            # Product image
            # Replace 'iphone.jpg' with the path to your product image
            product_image = Image.open('iphone.jpg')
            product_image = product_image.resize((200, 200), Image.LANCZOS)  # Resize the image
            product_image = ImageTk.PhotoImage(product_image)
            image_label = tkinter.Label(frame, image=product_image)
            image_label.image = product_image  # keep a reference to the image
            image_label.pack()

            # Product title
            title_label = tkinter.Label(frame, text="Product Title", font=("Arial", 24), background=color)
            title_label.pack()

            # Product description
            description_label = tkinter.Label(frame, text="Product description goes here.", font=("Arial", 16), background=color)
            description_label.pack()

            # Product price
            price_label = tkinter.Label(frame, text="$99.99", font=("Arial", 20), background=color)
            price_label.pack()
        elif frame_id == "Product List":
            # List of products
            products = [
                {"title": "Product 1", "price": "$99.99", "image": "iphone.jpg"},
                {"title": "Product 2", "price": "$89.99", "image": "iphone.jpg"},
                {"title": "Product 3", "price": "$79.99", "image": "iphone.jpg"},
                {"title": "Product 3", "price": "$79.99", "image": "iphone.jpg"},
                {"title": "Product 3", "price": "$79.99", "image": "iphone.jpg"},
                {"title": "Product 3", "price": "$79.99", "image": "iphone.jpg"},
                {"title": "Product 3", "price": "$79.99", "image": "iphone.jpg"},
                {"title": "Product 3", "price": "$79.99", "image": "iphone.jpg"},
                {"title": "Product 3", "price": "$79.99", "image": "iphone.jpg"},
            ]  # Replace with your list of products

            for i, product in enumerate(products):
                # Create a new frame for each product
                product_frame = tkinter.Frame(frame, background=color)
                product_frame.grid(row=i // 8, column=i % 8)  # Arrange the product frames in a 3-column grid

                # Product image
                product_image = Image.open(product["image"])
                product_image = product_image.resize((100, 100), Image.LANCZOS)  # Resize the image
                product_image = ImageTk.PhotoImage(product_image)
                image_label = tkinter.Label(product_frame, image=product_image, background=color)
                image_label.image = product_image  # keep a reference to the image
                image_label.pack()

                # Bind a click event to the image label
                image_label.bind("<Button-1>", lambda event, product=product: self.show_product_detail(product))

                # Product title
                title_label = tkinter.Label(product_frame, text=product["title"], font=("Arial", 16), background=color)
                title_label.pack()

                # Bind a click event to the title label
                title_label.bind("<Button-1>", lambda event, product=product: self.show_product_detail(product))

                # Product price
                price_label = tkinter.Label(product_frame, text=product["price"], font=("Arial", 16), background=color)
                price_label.pack()

                # Bind a click event to the price label
                price_label.bind("<Button-1>", lambda event, product=product: self.show_product_detail(product))
        elif frame_id == "User Profile":
            # User profile image
            # Replace 'user.jpg' with the path to your user profile image
            user_image = Image.open('avatar.jpg')
            user_image = user_image.resize((200, 200), Image.LANCZOS)  # Resize the image
            user_image = ImageTk.PhotoImage(user_image)
            image_label = tkinter.Label(frame, image=user_image)
            image_label.image = user_image  # keep a reference to the image
            image_label.pack()

            # User name
            name_label = tkinter.Label(frame, text="User Name", font=("Arial", 24), background=color)
            name_label.pack()

            # User email
            email_label = tkinter.Label(frame, text="user@example.com", font=("Arial", 16), background=color)
            email_label.pack()
        elif frame_id == "Cart":
            # Cart items
            cart_items = [
                {"title": "Product 1", "price": "$99.99", "quantity": 1},
                {"title": "Product 2", "price": "$89.99", "quantity": 2},
                {"title": "Product 3", "price": "$79.99", "quantity": 3},
            ]  # Replace with your cart items

            for i, item in enumerate(cart_items):
                # Create a new frame for each cart item
                item_frame = tkinter.Frame(frame, background=color)
                item_frame.grid(row=i, column=0, sticky="w")  # Arrange the item frames in a single column

                # Item title
                title_label = tkinter.Label(item_frame, text=item["title"], font=("Arial", 16), background=color)
                title_label.pack(side=tkinter.LEFT)

                # Item quantity
                quantity_label = tkinter.Label(item_frame, text="x" + str(item["quantity"]), font=("Arial", 16), background=color)
                quantity_label.pack(side=tkinter.LEFT)

                # Item price
                price_label = tkinter.Label(item_frame, text=item["price"], font=("Arial", 16), background=color)
                price_label.pack(side=tkinter.LEFT)
        elif frame_id == "Checkout":
            # Checkout items
            checkout_items = [
                {"title": "Product 1", "price": "$99.99", "quantity": 1},
                {"title": "Product 2", "price": "$89.99", "quantity": 2},
                {"title": "Product 3", "price": "$79.99", "quantity": 3},
            ]  # Replace with your checkout items

            total_price = 0

            for i, item in enumerate(checkout_items):
                # Create a new frame for each checkout item
                item_frame = tkinter.Frame(frame, background=color)
                item_frame.grid(row=i, column=0, sticky="w")  # Arrange the item frames in a single column

                # Item title
                title_label = tkinter.Label(item_frame, text=item["title"], font=("Arial", 16), background=color)
                title_label.pack(side=tkinter.LEFT)

                # Item quantity
                quantity_label = tkinter.Label(item_frame, text="x" + str(item["quantity"]), font=("Arial", 16), background=color)
                quantity_label.pack(side=tkinter.LEFT)

                # Item price
                price_label = tkinter.Label(item_frame, text=item["price"], font=("Arial", 16), background=color)
                price_label.pack(side=tkinter.LEFT)

                # Calculate the total price
                total_price += float(item["price"].replace("$", "")) * item["quantity"]

            # Display the total price
            total_price_label = tkinter.Label(frame, text="Total: $" + str(total_price), font=("Arial", 20), background=color)
            total_price_label.grid(row=len(checkout_items), column=0)  # Add the total price label below the checkout items

            # Checkout button
            checkout_button = customtkinter.CTkButton(frame, text="Checkout", command=self.checkout)
            checkout_button.grid(row=len(checkout_items) + 1, column=0)  # Add the checkout button below the total price label
        elif frame_id == "Tracking Page":
            # Tracking information
            tracking_info = [
                {"number": "1234567890", "status": "In Transit", "estimated_delivery": "2022-12-31"},
                {"number": "0987654321", "status": "Delivered", "estimated_delivery": "2022-12-30"},
            ]  # Replace with your tracking information

            for i, info in enumerate(tracking_info):
                # Create a new frame for each tracking information
                info_frame = tkinter.Frame(frame, background=color)
                info_frame.grid(row=i, column=0, sticky="w")  # Arrange the info frames in a single column

                # Tracking number
                number_label = tkinter.Label(info_frame, text="Tracking Number: " + info["number"], font=("Arial", 16), background=color)
                number_label.pack(side=tkinter.LEFT)

                # Current status
                status_label = tkinter.Label(info_frame, text="Status: " + info["status"], font=("Arial", 16), background=color)
                status_label.pack(side=tkinter.LEFT)

                # Estimated delivery date
                delivery_label = tkinter.Label(info_frame, text="Estimated Delivery: " + info["estimated_delivery"], font=("Arial", 16), background=color)
                delivery_label.pack(side=tkinter.LEFT)
        elif frame_id == "Store Profile":
            # Store information
            store_info = {
                "name": "My Store",
                "address": "123 Main St, Anytown, USA",
                "contact": "(123) 456-7890",
                "description": "We sell high-quality products at affordable prices.",
            }  # Replace with your store information

            # Load the logo image
            image = Image.open("logo.png")  # Replace with your logo file

            # Resize the image
            max_size = (100, 100)  # Replace with the desired size
            image.thumbnail(max_size)

            logo = ImageTk.PhotoImage(image)

            # Display the logo
            logo_label = tkinter.Label(frame, image=logo)
            logo_label.image = logo  # Keep a reference to the image object to prevent it from being garbage collected
            logo_label.pack()

            # Store name
            name_label = tkinter.Label(frame, text="Store Name: " + store_info["name"], font=("Arial", 16), background=color)
            name_label.pack()

            # Store address
            address_label = tkinter.Label(frame, text="Address: " + store_info["address"], font=("Arial", 16), background=color)
            address_label.pack()

            # Store contact information
            contact_label = tkinter.Label(frame, text="Contact: " + store_info["contact"], font=("Arial", 16), background=color)
            contact_label.pack()

            # Store description
            description_label = tkinter.Label(frame, text="Description: " + store_info["description"], font=("Arial", 16), background=color)
            description_label.pack()

        self.frames[frame_id] = frame

    # method to change frames
    def toggle_frame_by_id(self, frame_id):
        if self.frames[frame_id] is not None:
            if self.current is self.frames[frame_id]:
                self.current.pack_forget()
                self.current = None
            elif self.current is not None:
                self.current.pack_forget()
                self.current = self.frames[frame_id]
                self.current.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
            else:
                self.current = self.frames[frame_id]
                self.current.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    # method to create a pair button selector and its related frame
    def create_nav(self, parent, frame_id, frame_color):
        bt_frame = self.frame_selector_bt(parent, frame_id)
        self.create_frame(frame_id, frame_color)
        bt_frame.configure(command=partial(self.toggle_frame_by_id, frame_id))

    def show_product_detail(self, product):
        # Change the page to the product detail page
        self.toggle_frame_by_id("Product Page")

    def checkout(self):
        # Implement your checkout process here
        print("Checkout")

a = App()
a.mainloop()