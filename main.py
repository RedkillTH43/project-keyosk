import tkinter as tk
from tkinter import PhotoImage

# Initializes main screen
root = tk.Tk()
root.title("Project Keyosk")
root.geometry("600x800")

# Declare constant variables
ITEM_NUM = 7
category_names_arr = ["Home", "Breakfast", "Lunch", "Dinner", "Sides", "Desserts", "Drinks"]

# Declares arrays to hold widgets
categories_arr = []
items_arr = []

# Create images
image_object = PhotoImage(file="./assets/png.png")
item_image = PhotoImage(file="./assets/item.png")

# Change item display according to category
def change_category(_category_name):
    items_arr.clear()
    frames_dict["item"].destroy()
    frames_dict["item"] = tk.Frame(main_frm)

    # Checks category and assign accordingly
    match _category_name:
        case "Home":
            print("You clicked Home")
            item_amount = 1
        case "Breakfast":
            print("You clicked Breakfast")
            item_amount = 2
        case "Lunch":
            print("You clicked Lunch")
            item_amount = 3
        case "Dinner":
            print("You clicked Dinner")
            item_amount = 4
        case "Sides":
            print("You clicked Sides")
            item_amount = 5
        case "Desserts":
            print("You clicked Desserts")
            item_amount = 6
        case "Drinks":
            print("You clicked Drinks")
            item_amount = 7
        case _:
            print("Invalid")
            item_amount = 8

    make_item_cards(item_amount)
    update()

# Create frames to hold widgets
main_frm = tk.Frame(root)
main_frm.columnconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=3)

category_frm = tk.Frame(main_frm)
item_frm = tk.Frame(main_frm)
button_frm = tk.Frame(main_frm, padx=5)

frames_dict = {
    "main": main_frm,
    "category": category_frm,
    "item": item_frm,
    "button": button_frm
}

# Create button widgets
cancel_btn = tk.Button(button_frm, text="Cancel", cursor="hand2")
done_btn = tk.Button(button_frm, text="Done", cursor="hand2")

# Create category buttons
for category_name in category_names_arr:
    category_btn = tk.Button(
        category_frm,
        text=category_name,
        image=image_object,
        width=120,
        compound="left",
        borderwidth=2,
        relief="solid",
        cursor="hand2",
        anchor="w",
        command=lambda category_name=category_name: change_category(category_name)
    )
    categories_arr.append(category_btn)

# Create item cards
def make_item_cards(amount):
    for item in range(amount):
        item_btn = tk.Button(
            frames_dict["item"],
            text="Lorem\nPHP 0.00",
            cursor="hand2",
            image=item_image,
            compound="top",
            borderwidth=2,
            relief="solid"
        )
        items_arr.append(item_btn)
make_item_cards(ITEM_NUM)

# Create heading widget
heading_lbl = tk.Label(main_frm, text="Keyosk", font=("Arial", 40), pady=5)

# Display widgets
heading_lbl.grid(row=0, column=0, columnspan=2)
frames_dict["category"].grid(row=1, column=0, sticky="nsew")
frames_dict["item"].grid(row=1, column=1, sticky="nsew")
frames_dict["button"].grid(row=2, column=0, columnspan=2, pady=10)

# Display category widgets
for category in categories_arr:
    category.pack(anchor="w", pady=5, padx=5)

# Display item widgets
def update():
    item_row = 0
    item_column = 0

    for item in items_arr:
        if (item_column + 1 % 3) > 0 and item_column + 1 > 3:
            item_row += 1
            item_column = 0
        item.grid(row=item_row, column=item_column, padx=5, pady=5)
        item_column += 1
    frames_dict["item"].grid(row=1, column=1, sticky="n")
update()

# Display buttons
cancel_btn.pack(side="left", padx=5)
done_btn.pack(side="left", padx=5)

frames_dict["main"].pack(expand=True, fill="both")

# Ensures program keeps running
root.mainloop()