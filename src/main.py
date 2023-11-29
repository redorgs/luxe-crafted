import customtkinter


class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []
        self.buttons = []

        for i, value in enumerate(self.values):
            label = customtkinter.CTkLabel(
                self, text=value, fg_color="transparent")
            label.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(label)

            button = customtkinter.CTkButton(
                self, text="Hapus", command=lambda i=i: self.button_callback(i))
            button.grid(row=i, column=1, padx=10, pady=(10, 0), sticky="w")
            self.buttons.append(button)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

    def button_callback(self, i):
        # Remove the label and button from the grid
        self.checkboxes[i].grid_forget()
        self.buttons[i].grid_forget()

        # Remove the label and button from the lists
        del self.checkboxes[i]
        del self.buttons[i]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(
            self, values=["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Green"])
        self.checkbox_frame.grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()
