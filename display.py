import tkinter as tk
import control as control

# Set up initial frames for the main screen
def set_up_main_screen(root):
    main_frm = tk.Frame(root)
    title_frm = tk.Frame(main_frm)
    title_lbl = tk.Label(title_frm, text="Keyosk", font=("Arial", 40), pady=5)

    title_lbl.grid(row=0, column=0)
    title_frm.grid(row=0, column=0, columnspan=2, sticky="n")
    main_frm.pack(expand=True, fill="both", padx=10)

    frames_dict = {
        "main": main_frm,
        "title": title_frm
    }

    control.pass_data(frames_dict, "initial_frames")
    control.switch_to_page(3)

# Set up the frames of the specified page
def set_up_page(page_number):
    if page_number == 3:
        set_up_frames()
        make_category_cards()
        make_item_cards()
    elif page_number == 4:
        pick_meal_type()

    # Make is_page_loaded of specified page to True
    control.pass_data(True, "pages", "is_page_loaded")

# Set up frames to be used
def set_up_frames():
    main_frm = control.retrieve_data("initial_frames").get("main")
    category_frm = tk.Frame(main_frm)
    item_frm = tk.Frame(main_frm)
    button_frm = tk.Frame(main_frm, padx=5)

    cancel_btn = tk.Button(button_frm, text="Cancel", cursor="hand2")
    done_btn = tk.Button(button_frm, text="Done", cursor="hand2")
    cancel_btn.grid(row=0, column=0, padx=5)
    done_btn.grid(row=0, column=1, padx=5)

    main_frm.columnconfigure(0, weight=1)
    main_frm.columnconfigure(1, weight=3)

    # Hold frames in a dictionary for quick access
    frames_dict = {
        "category": category_frm,
        "item": item_frm,
        "button": button_frm
    }

    # Make dictionary to hold page widgets
    page_dict = { control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False } }

    control.pass_data(page_dict, "pages")

# Switch to specified page
def switch_to(page_number):
    control.clear_page()
    control.pass_data(page_number, "current_page")
    if not control.retrieve_data("pages", "is_page_loaded"):
        #print(control.retrieve_data("pages", "is_page_loaded"))
        control.load_page(page_number)
    control.render_page(page_number)

# Create category buttons
def make_category_cards():
    categories_arr = []
    # Makes a category button based on category names
    for category_name in control.retrieve_data("category_names"):
        category_btn = tk.Button(
            control.retrieve_data("pages", "frames").get("category"),
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
def make_item_cards(amount=1):
    items_arr = []
    # Makes an item button by amount times
    for item in range(amount):
        item_btn = tk.Button(
            control.retrieve_data("pages", "frames").get("item"),
            text="Lorem\nPHP 0.00",
            cursor="hand2",
            image=control.retrieve_data("images").get("item_image"),
            compound="top",
            borderwidth=2,
            relief="solid",
            command=lambda next_page=control.retrieve_data("current_page") + 1: control.switch_to_page(next_page)
        )
        # Stores created button to an array
        items_arr.append(item_btn)
    # Returns the array
    control.pass_data(items_arr, "items")

# Change item display according to category
def change_category(_category_name):
    destroy_widgets(control.retrieve_data("items"))
    control.pass_data(_category_name, "prev_category")

    make_item_cards(amount = control.retrieve_data("category_names").get(_category_name))
    control.render_page(3)

# Switch to page asking for meal type
def pick_meal_type():
    main_frm = control.retrieve_data("initial_frames").get("main")
    main_frm.rowconfigure(0, weight=0)
    main_frm.rowconfigure(1, weight=0)
    main_frm.rowconfigure(2, weight=1)

    heading_frm = tk.Frame(main_frm)
    choices_frm = tk.Frame(main_frm)

    choices_frm.columnconfigure(0, weight=1)
    choices_frm.columnconfigure(1, weight=1)

    question_lbl = tk.Label(heading_frm, text="Would you like to make it a meal?", font=("Arial", 20), pady=5)
    yes_btn = tk.Button(
        choices_frm,
        text="Yes, make it a meal",
        cursor="hand2",
        image=control.retrieve_data("images")["item_image"],
        compound="top",
        borderwidth=2,
        relief="solid",
        height=300
    )
    no_btn = tk.Button(
        choices_frm,
        text="No, ala carte only",
        cursor="hand2",
        image=control.retrieve_data("images")["item_image"],
        compound="top",
        borderwidth=2,
        relief="solid",
        height=300,
        command=lambda: control.switch_to_page(3)
    )

    question_lbl.grid(row=0, column=0, sticky="n")
    yes_btn.grid(row=0, column=0, sticky="new", padx=5, pady=5)
    no_btn.grid(row=0, column=1, sticky="new", padx=5, pady=5)

    frames_dict = {
        "heading": heading_frm,
        "choices": choices_frm
    }
    page_dict = { control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False } }
    control.pass_data(page_dict, "pages")

# Resets configuration of main frame
def reset_main():
    main_frm = control.retrieve_data("initial_frames").get("main")
    main_frm.columnconfigure(0, weight=1)
    main_frm.columnconfigure(1, weight=1)
    main_frm.rowconfigure(0, weight=0)
    main_frm.rowconfigure(1, weight=0)
    main_frm.rowconfigure(2, weight=0)

# Remove all frames in the screen except for main
def clear_screen():
    reset_main()
    if control.retrieve_data("current_page"):
        for frame in control.retrieve_data("pages", "frames"):
            control.retrieve_data("pages", "frames").get(frame).grid_remove()

# Display item widgets
def update_items():
    item_row = 0
    item_column = 0
    items = control.retrieve_data("items")

    for item in items:
        if (item_column + 1 % 3) > 0 and item_column + 1 > 3:
            item_row += 1
            item_column = 0
        item.grid(row=item_row, column=item_column, padx=5, pady=5)
        item_column += 1

def render_widgets(page_number):
    match page_number:
        case 3:
            control.update_page()

            for category in control.retrieve_data("categories"):
                category.pack(anchor="w", pady=5, padx=5)
            control.retrieve_data("pages", "frames").get("category").grid(row=1, column=0, sticky="nsew")
            control.retrieve_data("pages", "frames").get("item").grid(row=1, column=1, sticky="nsew")
            control.retrieve_data("pages", "frames").get("button").grid(row=2, column=0, columnspan=2, sticky="n", pady=10)
        case 4:
            control.retrieve_data("pages", "frames").get("heading").grid(row=1, column=0, columnspan=2, sticky="n")
            control.retrieve_data("pages", "frames").get("choices").grid(row=2, column=0, columnspan=2, sticky="new")

def destroy_widgets(widgets):
    for widget in widgets:
        widget.destroy()
