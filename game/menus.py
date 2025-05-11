import tkinter as tk
from tkinter import messagebox
from data_manager import *

class MenuGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MENUS")
        self.geometry("1700x600")
        self.configure(bg="black")  # Set background color to black

        self.filter = ""  # Default filter

        self.flavour_filter = ""
        self.type_filter = ""
        
        self.__menu = DataManager()
        self.items = self.__menu.get_data("menu")

        grid = tk.Frame(self, bg="black")  # Set background color to black
        grid.pack(pady=10)

        self.create_filter_buttons(grid)
        self.create_scrollable_menus()

        # Add Exit Button
        exit_button = tk.Button(self, text="Exit", command=self.destroy)
        exit_button.pack(pady=10)

    def create_filter_buttons(self, parent):
        # Filters for Flavour and Type
        flavour_filters = ["All Flavours", "Bitter", "Bubbly", "Sour", "Spicy", "Sweet"]
        type_filters = ["All Types", "Classic", "Classy", "Girly", "Manly", "Promo"]

        # Flavour filter buttons
        flavour_label = tk.Label(parent, text="Flavours:", bg="black", fg="white")  # Set background and text color
        flavour_label.grid(row=0, column=0, padx=5, pady=5)
        for i, flavour in enumerate(flavour_filters):
            button = tk.Button(parent, text=flavour, command=lambda f=flavour: self.apply_filter(f, "Flavour"))
            button.grid(row=0, column=i + 1, padx=5, pady=5)

        # Type filter buttons
        type_label = tk.Label(parent, text="Types:", bg="black", fg="white")  # Set background and text color
        type_label.grid(row=1, column=0, padx=5, pady=5)
        for i, type_filter in enumerate(type_filters):
            button = tk.Button(parent, text=type_filter, command=lambda t=type_filter: self.apply_filter(t, "Type"))
            button.grid(row=1, column=i + 1, padx=5, pady=5)

    def apply_filter(self, filter_value, filter_category):
        if filter_category == "Flavour":
            self.flavour_filter = "" if filter_value == "All Flavours" else filter_value
        elif filter_category == "Type":
            self.type_filter = "" if filter_value == "All Types" else filter_value

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.populate_items()

    def create_scrollable_menus(self):
        # Container for scrollbar and canvas
        container = tk.Frame(self, bg="black")  # Set background color to black
        container.pack(fill="both", expand=True)

        # Canvas and vertical scrollbar
        canvas = tk.Canvas(container, bg="black", highlightthickness=0)  # Set background color to black
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview, bg="black")  # Set scrollbar background color to black
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Scrollable frame inside the canvas
        self.scrollable_frame = tk.Frame(canvas, bg="black")  # Set background color to black
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        # Embed scrollable_frame into the canvas
        window = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Make the canvas resizable with the window
        def resize_canvas(event):
            canvas.itemconfig(window, width=event.width)
        canvas.bind("<Configure>", resize_canvas)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Enable mouse wheel scrolling (Windows & Linux)
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        # For macOS (use <Button-4> and <Button-5> if needed)

        self.populate_items()

    def populate_items(self):
        filtered_items = self.items
        if self.flavour_filter:
            filtered_items = filtered_items[filtered_items['Flavour'] == self.flavour_filter]
        if self.type_filter:
            filtered_items = filtered_items[filtered_items['Type'] == self.type_filter]

        filtered_items = filtered_items.to_dict(orient='records')

        # Add column headers
        headers = ["Picture", "Drinks", "Price", "A", "B", "D", "F", "K", "Rocks", "Aged", "Mix_or_Blend", "Flavour", "Type", "Sec_Type", "Description"]
        for col, header in enumerate(headers):
            header_label = tk.Label(self.scrollable_frame, text=header, font=("Arial", 10, "bold"), bg="black", fg="white", bd=1, relief="solid")  # Set border color and style
            header_label.grid(row=0, column=col, padx=5, pady=5, sticky="w")

        # Add items
        for row, item in enumerate(filtered_items, start=1):
            image = tk.PhotoImage(file=("sprite/drink_img/" + item['Drinks'] + ".png").replace(" ", "_"))  # Load image for the drink
            image_label = tk.Label(self.scrollable_frame, image=image, bg="black", bd=1, relief="solid")
            image_label.image = image  # Keep a reference to avoid garbage collection
            image_label.grid(row=row, column=0, padx=5, pady=5, sticky="w")

            tk.Label(self.scrollable_frame, text=item['Drinks'].replace("_", " "), width=20, fg="aqua", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=1, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=f"${item['Price']}", width=5, fg="green", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=2, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['A'], width=5, fg="red", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=3, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['B'], width=5, fg="yellow", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=4, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['D'], width=5, fg="aqua", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=5, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['F'], width=5, fg="light green", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=6, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text="any" if item["K"] == -1 else item['K'], width=5, fg="light gray", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=7, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text="Yes" if item['Rocks'] == 1 else "No", width=5, fg="aqua", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=8, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text="Yes" if item['Aged'] == 1 else "No", width=5, fg="purple", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=9, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['Mix_or_Blend'], width=7, fg="white", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=10, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['Flavour'], width=5, fg="purple", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=11, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['Type'], width=10, fg="orange", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=12, padx=5, pady=5, sticky="w")
            tk.Label(self.scrollable_frame, text=item['Sec_Type'], width=10, fg="brown", bg="black", anchor="w", bd=1, relief="solid").grid(row=row, column=13, padx=5, pady=5, sticky="w")
            description_label = tk.Label(self.scrollable_frame, text=item['Description'], width=20, fg="gray", bg="black", wraplength=100, justify="left", anchor="w", bd=1, relief="solid")
            description_label.grid(row=row, column=14, columnspan=2, padx=5, pady=5, sticky="w")
            
        

if __name__ == "__main__":
    shop = MenuGUI()
    shop.mainloop()