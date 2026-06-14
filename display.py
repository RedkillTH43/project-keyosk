import tkinter as tk
import control as control

# ToDo: Fix button frame being replaced with new buttons
# ToDo: Reformat data retrieval from controller
# ToDo: Implement grid_forget() method in hiding widgets and grid() for revealing them
# ToDo: Remove unnecessary recreations of new frames; don't create more, just hide them then restore later

# Setup frames to be used
def setup_frames():
    main_frm = control.retrieve_data("frames", "main")
    title_frm = tk.Frame(main_frm)
    category_frm = tk.Frame(main_frm)
    item_frm = tk.Frame(main_frm)
    button_frm = tk.Frame(main_frm, padx=5)

    title_lbl = tk.Label(title_frm, text="Keyosk", font=("Arial", 40), pady=5)
    title_lbl.grid(row=0, column=0)

    cancel_btn = tk.Button(button_frm, text="Cancel", cursor="hand2")
    done_btn = tk.Button(button_frm, text="Done", cursor="hand2")
    cancel_btn.grid(row=0, column=0, padx=5)
    done_btn.grid(row=0, column=1, padx=5)

    main_frm.columnconfigure(0, weight=1)
    main_frm.columnconfigure(1, weight=3)

    # Hold frames in a dictionary for quick access
    frames_dict = {
        "main": main_frm,
        "title": title_frm,
        "category": category_frm,
        "item": item_frm,
        "button": button_frm
    }
    control.pass_data(frames_dict, "frames")

# Create category buttons
def make_category_cards():
    categories_arr = []
    # Makes a category button based on category names
    for category_name in control.retrieve_data("category_names"):
        category_btn = tk.Button(
            control.retrieve_data("frames", "category"),
            text=category_name,
            image=control.retrieve_data("images").get("category_image"),
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
    control.pass_data(categories_arr, "categories")

# Create item cards
def make_item_cards(amount=3):
    items_arr = []
    # Makes an item button by amount times
    for item in range(amount):
        item_btn = tk.Button(
            control.retrieve_data("frames", "item"),
            text="Lorem\nPHP 0.00",
            cursor="hand2",
            image=control.retrieve_data("images", "item_image"),
            compound="top",
            borderwidth=2,
            relief="solid",
            command=lambda: control.switch_to_page(4)
        )
        # Stores created button to an array
        items_arr.append(item_btn)
    # Returns the array
    control.pass_data(items_arr, "items")

# Change item display according to category
def change_category(_category_name):
    control.retrieve_data("items").clear()
    control.retrieve_data("frames").get("item").destroy()
    control.pass_data(tk.Frame(control.retrieve_data("frames").get("main")), "frames", "item")
    control.pass_data(_category_name, "tracker")

    make_item_cards(amount = control.retrieve_data("category_names", _category_name))
    update_items()

# Switch to page asking for meal type
def pick_meal_type():
    control.retrieve_data("frames")["main"].rowconfigure(0, weight=0)
    control.retrieve_data("frames")["main"].rowconfigure(1, weight=0)
    control.retrieve_data("frames")["main"].rowconfigure(2, weight=1)

    control.retrieve_data("frames")["heading"] = tk.Frame(control.retrieve_data("frames")["main"])
    control.retrieve_data("frames")["button"] = tk.Frame(control.retrieve_data("frames")["main"])

    control.retrieve_data("frames")["button"].columnconfigure(0, weight=1)
    control.retrieve_data("frames")["button"].columnconfigure(1, weight=1)

    question_lbl = tk.Label(control.retrieve_data("frames")["heading"], text="Would you like to make it a meal?", font=("Arial", 20), pady=5)
    yes_btn = tk.Button(
        control.retrieve_data("frames")["button"],
        text="Yes, make it a meal",
        cursor="hand2",
        image=control.retrieve_data("images")["item_image"],
        compound="top",
        borderwidth=2,
        relief="solid",
        height=300
    )
    no_btn = tk.Button(
        control.retrieve_data("frames")["button"],
        text="No, ala carte only",
        cursor="hand2",
        image=control.retrieve_data("images")["item_image"],
        compound="top",
        borderwidth=2,
        relief="solid",
        height=300,
        command=return_to_order
    )

    question_lbl.grid(row=0, column=0, sticky="n")
    yes_btn.grid(row=0, column=0, sticky="new", padx=5, pady=5)
    no_btn.grid(row=0, column=1, sticky="new", padx=5, pady=5)

# Switch to ordering process
def switch_to_order():
    pass

# Return to ordering screen
def return_to_order():
    clear_screen()
    restore_screen()

# Resets configuration of main frame
def reset_main():
    control.retrieve_data("frames")["main"].columnconfigure(0, weight=1)
    control.retrieve_data("frames")["main"].columnconfigure(1, weight=1)

def restore_screen():
    for frame in control.retrieve_data("frames"):
        if frame in ["main", "title", "button", "heading"]:
            continue
        control.retrieve_data("frames", frame).grid()

# Remove all frames in the screen except for main
def clear_screen():
    reset_main()
    for frame in control.retrieve_data("frames"):
        if frame in ["main", "title"]:
            continue
        control.retrieve_data("frames", frame).grid_remove()

# Display item widgets
def update_items():
    item_row = 0
    item_column = 0

    for item in control.retrieve_data("items"):
        if (item_column + 1 % 3) > 0 and item_column + 1 > 3:
            item_row += 1
            item_column = 0
        item.grid(row=item_row, column=item_column, padx=5, pady=5)
        item_column += 1
    control.retrieve_data("frames", "item").grid(row=1, column=1, sticky="nw")

def render_widgets(page_number):
    match page_number:
        case 3:
            for category in control.retrieve_data("categories"):
                category.pack(anchor="w", pady=5, padx=5)
            update_items()

            control.retrieve_data("frames", "title").grid(row=0, column=0, columnspan=2, sticky="n")
            control.retrieve_data("frames", "category").grid(row=1, column=0, sticky="nsew")
            control.retrieve_data("frames", "item").grid(row=1, column=1, sticky="nsew")
            control.retrieve_data("frames", "button").grid(row=2, column=0, columnspan=2, sticky="n", pady=10)
        case 4:
            control.retrieve_data("frames", "heading").grid(row=1, column=0, columnspan=2, sticky="n")
            control.retrieve_data("frames", "button").grid(row=2, column=0, columnspan=2, sticky="new")