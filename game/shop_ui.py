import tkinter as tk
from tkinter import messagebox
from data_manager import *

class ShopGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shop")
        self.geometry("500x600")

        self.items = DataManager().get_data("items").to_dict(orient='records')

        self.balance = PlayerData().get_money()
        self.balance_label = tk.Label(self, text=f"Balance: ${int(self.balance)}")
        self.balance_label.pack(pady=10)

        self.create_scrollable_shop()

        # Add Exit Button
        exit_button = tk.Button(self, text="Exit", command=self.destroy)
        exit_button.pack(pady=10)

    def create_scrollable_shop(self):
        # Container for scrollbar and canvas
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Canvas and vertical scrollbar
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Scrollable frame inside the canvas
        self.scrollable_frame = tk.Frame(canvas)
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
        for item in self.items:
            if {"Name" : item["Item Name"], "Bonus" : item["Bonus"]} in PlayerData().get_items():
                continue
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(padx=10, pady=5, fill="x")

            buy_button = tk.Button(frame, text="Buy", command=lambda i=item: self.buy_item(i))
            buy_button.pack(side="left")

            name_label = tk.Label(frame, text=item['Item Name'], width=20, anchor='w')
            name_label.pack(side="left")

            price_label = tk.Label(frame, text=f"${item['Price']}", width=10)
            price_label.pack(side="left")

            bonus_label = tk.Label(frame, text=f"{item['Bonus']}%", width=10)
            bonus_label.pack(side="left")

            
    def buy_item(self, item):
        if self.balance >= item['Price']:
            self.balance -= item['Price']
            PlayerData().minus_money(item['Price'])
            DataManager().items.loc[DataManager().items['Item Name'] == item['Item Name'], 'times bought'] += 1
            self.balance_label.config(text=f"Balance: ${int(self.balance)}")
            messagebox.showinfo("Purchase", f"You bought {item['Item Name']}!")
            PlayerData().add_item({"Name" : item['Item Name'], "Bonus" : item['Bonus']})

        else:
            messagebox.showwarning("Not Enough Money", "You don't have enough money to buy this.")

if __name__ == "__main__":
    shop = ShopGUI()
    shop.mainloop()