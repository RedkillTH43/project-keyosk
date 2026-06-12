import tkinter as tk
from tkinter import PhotoImage

# Initializes main screen
root = tk.Tk()
root.title("Project Keyosk")
root.geometry("600x800")

# Declare constant variables
CATEGORY_NUM = 5
ITEM_NUM = 7

# Declares arrays to hold widgets
categories_arr = []
items_arr = []

# Create images
image_object = PhotoImage(file="./assets/png.png")
item_image = PhotoImage(file="./assets/item.png")

# Create frames to hold widgets
main_frm = tk.Frame(root)
main_frm.columnconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=3)

category_frm = tk.Frame(main_frm)
item_frm = tk.Frame(main_frm, padx=5)
button_frm = tk.Frame(main_frm, padx=5)

# Create button widgets
cancel_btn = tk.Button(button_frm, text="Cancel", cursor="hand2")
done_btn = tk.Button(button_frm, text="Done", cursor="hand2")

# Create category buttons
for category in range(CATEGORY_NUM):
    category_btn = tk.Button(category_frm, text="Lorem", image=image_object, compound="left", borderwidth=2, relief="solid", cursor="hand2")
    categories_arr.append(category_btn)

# Create item cards
"""
item_btn = tk.Button(button_frm, text="Lorem\nPHP 0.00", cursor="hand2", image=item_image, compound="top", borderwidth=2, relief="solid")
items_arr.append(item_btn)
"""

for item in range(ITEM_NUM):
    item_card_frm = tk.Frame(item_frm, borderwidth=2, relief="solid", padx=5, pady=5, cursor="hand2")
    item_image_lbl = tk.Label(item_card_frm, image=item_image, relief="solid", borderwidth=2)
    item_name_lbl = tk.Label(item_card_frm, text="Lorem Ipsum")
    item_price_lbl = tk.Label(item_card_frm, text="PHP 0.00")
    item_card_object = {
        "frame": item_card_frm,
        "image": item_image_lbl,
        "name": item_name_lbl,
        "price": item_price_lbl
    }
    items_arr.append(item_card_object)

# Create heading widget
heading_lbl = tk.Label(main_frm, text="Keyosk", font=("Arial", 40), pady=5)

# Display widgets
heading_lbl.grid(row=0, column=0, columnspan=2)
category_frm.grid(row=1, column=0, sticky="n")
item_frm.grid(row=1, column=1, sticky="n")
button_frm.grid(row=2, column=0, columnspan=2, pady=10, sticky="s")

# Display category widgets
for category in categories_arr:
    category.pack(anchor="w", pady=5)

# Display item widgets
item_row_length = len(items_arr) // 3
if len(items_arr) % 3 != 0:
    item_row_length = (len(items_arr) // 3) + 1

item_row = 0
item_column = 0
for item in items_arr:
    #item.pack()

    if (item_column + 1 % 3) > 0 and item_column + 1 > 3:
        item_row += 1
        item_column = 0
    item["frame"].grid(row=item_row, column=item_column, padx=5, pady=5)
    item["image"].pack()
    item["name"].pack()
    item["price"].pack()
    item_column += 1

# Display buttons
cancel_btn.pack(side="left", padx=5)
done_btn.pack(side="left", padx=5)

main_frm.pack(expand=True, fill="both")

# Ensures program keeps running
root.mainloop()