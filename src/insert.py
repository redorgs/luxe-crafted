import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.name = ["John Doe", "Jane Smith",
                     "Alice Johnson", "Bob Brown", "Charlie Green"]

        self.title("my app")
        self.geometry("400x600")
        customtkinter.CTkEntry(self, placeholder_text="CTkEntry").grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        save_button = customtkinter.CTkButton(
            self, text="Save", command=self.button_callback)
        save_button.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        for i, name in enumerate(self.name):
            i = i+1
            customtkinter.CTkLabel(self, text=name, fg_color="transparent").grid(
                row=i, column=0, padx=10, pady=(10, 0), sticky="nsw")

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()

# Existing code continues...
