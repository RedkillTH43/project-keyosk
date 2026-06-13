import tkinter as tk
# ToDo: Fix KeyError: item_image

# Initialize necessary variables
ITEM_NUM = 7
category_names_arr = ["Home", "Breakfast", "Lunch", "Dinner", "Sides", "Desserts", "Drinks"]
main_dict = {
    "frames": {},
    "categories": [],
    "items": [],
    "images": {}
}

# Setup frames to be used
def setup_frames(main_frm, images):
    heading_frm = tk.Frame(main_frm)
    category_frm = tk.Frame(main_frm)
    item_frm = tk.Frame(main_frm)
    button_frm = tk.Frame(main_frm, padx=5)
    main_dict["images"] = images

    heading_lbl = tk.Label(heading_frm, text="Keyosk", font=("Arial", 40), pady=5)
    heading_lbl.pack()

    cancel_btn = tk.Button(button_frm, text="Cancel", cursor="hand2")
    done_btn = tk.Button(button_frm, text="Done", cursor="hand2")
    cancel_btn.pack(side="left", padx=5)
    done_btn.pack(side="left", padx=5)

    main_frm.columnconfigure(0, weight=1)
    main_frm.columnconfigure(1, weight=3)

    # Hold frames in a dictionary for quick access
    frames_dict = {
        "main": main_frm,
        "heading": heading_frm,
        "category": category_frm,
        "item": item_frm,
        "button": button_frm
    }
    main_dict["frames"] = frames_dict

# Create category buttons
def make_category_cards():
    categories_arr = []
    # Makes a category button based on category names
    for category_name in category_names_arr:
        category_btn = tk.Button(
            main_dict["frames"]["category"],
            text=category_name,
            image=main_dict["images"]["category_image"],
            width=120,
            compound="left",
            borderwidth=2,
            relief="solid",
            cursor="hand2",
            anchor="w",
            command=lambda category_name=category_name: change_category(category_name)
        )
        # Stores created button to an array
        categories_arr.append(category_btn)
    # Returns the array
    main_dict["categories"] = categories_arr

# Create item cards
def make_item_cards(image_object=main_dict["images"]["item_image"], amount=ITEM_NUM):
    items_arr = []
    # Makes an item button by amount times
    for item in range(amount):
        item_btn = tk.Button(
            main_dict["frames"]["item"],
            text="Lorem\nPHP 0.00",
            cursor="hand2",
            image=image_object,
            compound="top",
            borderwidth=2,
            relief="solid",
            command=lambda: pick_meal_type(image_object)
        )
        # Stores created button to an array
        items_arr.append(item_btn)
    # Returns the array
    main_dict["items"] = items_arr

# Change item display according to category
def change_category(_category_name):
    main_dict["items"].clear()
    main_dict["frames"]["item"].destroy()
    main_dict["frames"]["item"] = tk.Frame(main_dict["frames"]["main"])

    # Checks category and assign accordingly
    match _category_name:
        case "Home":
            item_amount = 1
        case "Breakfast":
            item_amount = 2
        case "Lunch":
            item_amount = 3
        case "Dinner":
            item_amount = 4
        case "Sides":
            item_amount = 5
        case "Desserts":
            item_amount = 6
        case "Drinks":
            item_amount = 7
        case _:
            item_amount = 8

    make_item_cards(amount = item_amount)
    update_items()

# Switch to page asking for meal type
def pick_meal_type(image_object):
    clear_screen()
    reset_main()

    main_dict["frames"]["main"].rowconfigure(0, weight=0)
    main_dict["frames"]["main"].rowconfigure(1, weight=0)
    main_dict["frames"]["main"].rowconfigure(2, weight=1)

    question_lbl = tk.Label(main_dict["frames"]["main"], text="Would you like to make it a meal?", font=("Arial", 20), pady=5)
    yes_btn = tk.Button(
        main_dict["frames"]["main"],
        text="Yes, make it a meal",
        cursor="hand2",
        image=image_object,
        compound="top",
        borderwidth=2,
        relief="solid",
        height=300
    )
    no_btn = tk.Button(
        main_dict["frames"]["main"],
        text="No, ala carte only",
        cursor="hand2",
        image=image_object,
        compound="top",
        borderwidth=2,
        relief="solid",
        height=300
    )

    question_lbl.grid(row=1, column=0, columnspan=2, sticky="n")
    yes_btn.grid(row=2, column=0, sticky="new", padx=5, pady=5)
    no_btn.grid(row=2, column=1, sticky="new", padx=5, pady=5)

# Resets configuration of main frame
def reset_main():
    main_dict["frames"]["main"].columnconfigure(0, weight=1)
    main_dict["frames"]["main"].columnconfigure(1, weight=1)

# Remove all frames in the screen except for main
def clear_screen():
    for frame in main_dict["frames"]:
        if frame == "main":
            continue
        main_dict["frames"][frame].destroy()

# Display item widgets
def update_items():
    item_row = 0
    item_column = 0

    for item in main_dict["items"]:
        if (item_column + 1 % 3) > 0 and item_column + 1 > 3:
            item_row += 1
            item_column = 0
        item.grid(row=item_row, column=item_column, padx=5, pady=5)
        item_column += 1
    main_dict["frames"]["item"].grid(row=1, column=1, sticky="n")

def render_widgets():
    for category in main_dict["categories"]:
        category.pack(anchor="w", pady=5, padx=5)
    update_items()
    main_dict["frames"]["heading"].grid(row=0, column=0, columnspan=2, sticky="n")
    main_dict["frames"]["category"].grid(row=1, column=0, sticky="nsew")
    main_dict["frames"]["item"].grid(row=1, column=1, sticky="nsew")
    main_dict["frames"]["button"].grid(row=2, column=0, columnspan=2, pady=10)