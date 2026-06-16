import tkinter as tk
from tkinter import ttk
import control as control

# Configure main frame's row and column weight
def configure_main(page_number):
    main_frm = control.retrieve_data("initial_frames")["main"]

    match page_number:
        case 1:
            main_frm.columnconfigure(1, weight=1)
            main_frm.rowconfigure(2, weight=2)
            main_frm.rowconfigure(3, weight=1)
            main_frm.rowconfigure(4, weight=3)
        case 3:
            main_frm.columnconfigure(1, weight=3)

# Set up initial frames for the main screen
def set_up_main_screen(root):
    main_frm = tk.Frame(root, bg="white")
    title_frm = tk.Frame(main_frm)
    title_lbl = tk.Label(title_frm, text="Keyosk", font=("Arial", 20), pady=5, justify="center", bg="white")
    separator = ttk.Separator(title_frm, orient="horizontal")

    main_frm.rowconfigure(0, weight=0)
    main_frm.columnconfigure(0, weight=1)
    title_frm.columnconfigure(0, weight=1)

    title_lbl.grid(row=0, column=0, sticky="ew")
    separator.grid(row=1, column=0, columnspan=2, sticky="ew")

    title_frm.grid(row=0, column=0, columnspan=2, sticky="ew")
    main_frm.pack(expand=True, fill="both")

    frames_dict = {
        "main": main_frm,
        "title": title_frm
    }

    control.pass_data(frames_dict, "initial_frames")

# Set up the frames of the specified page
def set_up_page(page_number):
    match page_number:
        case 1:
            home_page()
        case 2:
            create_second_page()
        case 3:
            set_up_frames()
            make_category_cards()
            make_item_cards()
        case 4:
            pick_meal_type()

    # Make is_page_loaded of specified page to True
    control.pass_data(True, "pages", "is_page_loaded")

# Create home page
def home_page():
    next_page = control.retrieve_data("current_page") + 1

    main_frm = control.retrieve_data("initial_frames")["main"]

    heading_frm = tk.Frame(main_frm, bg="white")
    subtitle_frm = tk.Frame(main_frm, bg="white")
    #separator_frm = tk.Frame(main_frm)
    button_frm = tk.Frame(main_frm, bg="white")

    image_frm = tk.Frame(
        main_frm,
        bg="white",
        relief="solid",
        bd=2,
    )

    heading = tk.Label(
        heading_frm,
        text="THIS IS KEYOSK",
        font=("Arial", 30, "bold"),
        bg="white"
    )

    image_object = tk.Label(
        image_frm,
        text="PLACE IMAGE HERE",
        font=("Arial", 16),
        justify="center",
        bg="white"
    )

    subtitle = tk.Label(
        subtitle_frm,
        text='"A Self-Ordering System Kiosk for Restaurants"',
        font=("Arial", 16),
        bg="white"
    )

    see_order_btn = tk.Button(
        button_frm,
        text="SEE ORDERS",
        width=15,
        height=2,
        font=("Arial", 12, "bold"),
        bg="white"
    )

    start_btn = tk.Button(
        button_frm,
        text="START ORDER",
        width=20,
        height=2,
        font=("Arial", 12, "bold"),
        command=lambda: control.switch_to_page(next_page),
        bg="white"
    )

    # Display all widgets
    heading.grid(row=0, column=0)
    image_object.grid(row=0, column=0, sticky="nsew")
    subtitle.grid(row=0, column=0)
    see_order_btn.grid(row=0, column=0, padx=5)
    start_btn.grid(row=0, column=1, padx=5)

    frames_dict = {
        "heading": heading_frm,
        "image": image_frm,
        "subtitle": subtitle_frm,
        "button": button_frm
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")

def create_second_page():
    next_page = control.retrieve_data("current_page") + 1
    main_frm = control.retrieve_data("initial_frames")["main"]
    heading_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, bg="white")

    button_frm.columnconfigure(0, weight=1)
    button_frm.columnconfigure(1, weight=1)

    heading = tk.Label(
        heading_frm,
        text="Where would you like to eat?",
        font=("Arial", 24),
        justify="center",
        bg="white"
    )

    dine_btn = tk.Button(
        button_frm,
        text="DINE-IN",
        font=("Arial", 16, "bold"),
        bg="#2ecc71",
        fg="white",
        width=8,
        height=12,
        command=lambda: control.switch_to_page(next_page),
    )

    take_btn = tk.Button(
        button_frm,
        text="TAKE-OUT",
        font=("Arial", 16, "bold"),
        bg="#3498db",
        fg="white",
        width=8,
        height=12,
        command=lambda: control.switch_to_page(next_page)
    )

    # Display all widgets
    heading.grid(row=0, column=0)
    dine_btn.grid(row=0, column=0, sticky="ew", padx=5)
    take_btn.grid(row=0, column=1, sticky="ew", padx=5)

    frames_dict = {
        "heading": heading_frm,
        "button": button_frm
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")

# Set up frames to be used
def set_up_frames():
    main_frm = control.retrieve_data("initial_frames").get("main")
    category_frm = tk.Frame(main_frm, bg="white")
    item_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, padx=5, bg="white")

    cancel_btn = tk.Button(
        button_frm,
        text="Cancel",
        cursor="hand2",
        command=lambda: control.switch_to_page(1),
        bg="white"
    )
    
    done_btn = tk.Button(
        button_frm,
        text="Done",
        cursor="hand2",
        bg="white"
    )
    
    cancel_btn.grid(row=0, column=0, padx=5)
    done_btn.grid(row=0, column=1, padx=5)

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
            command=lambda category_name=category_name: change_category(category_name),
            bg="white"
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
            width=100,
            height=150,
            borderwidth=2,
            relief="solid",
            command=lambda next_page=control.retrieve_data("current_page") + 1: control.switch_to_page(next_page),
            bg="white"
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
    main_frm.rowconfigure(1, weight=0)
    main_frm.rowconfigure(2, weight=1)

    heading_frm = tk.Frame(main_frm, bg="white")
    choices_frm = tk.Frame(main_frm, bg="white")

    choices_frm.columnconfigure(0, weight=1)
    choices_frm.columnconfigure(1, weight=1)

    question_lbl = tk.Label(heading_frm, text="Would you like to make it a meal?", font=("Arial", 20), pady=5, bg="white")
    yes_btn = tk.Button(
        choices_frm,
        text="Yes, make it a meal",
        cursor="hand2",
        image=control.retrieve_data("images")["item_image"],
        compound="top",
        borderwidth=2,
        relief="solid",
        height=300,
        bg="white"
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
        command=lambda: control.switch_to_page(3),
        bg="white"
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
    max_row = control.retrieve_data("MAX_ROW")
    max_column = control.retrieve_data("MAX_COLUMN")

    for row in range(1, max_row + 1):
        main_frm.rowconfigure(row, weight=0)

    for column in range(1, max_column + 1):
        main_frm.columnconfigure(column, weight=0)

# Remove all frames in the screen except for main
def clear_screen():
    reset_main()
    if control.retrieve_data("current_page"):
        for frame in control.retrieve_data("pages", "frames"):
            control.retrieve_data("pages", "frames").get(frame).grid_remove()

# Display item widgets
def update_items(page_number):
    match page_number:
        case 3:
            item_frm = control.retrieve_data("pages", "frames")["item"]
            item_frm.columnconfigure(0, weight=1)
            item_frm.columnconfigure(1, weight=1)
            item_frm.columnconfigure(2, weight=1)

            items = control.retrieve_data("items")
            item_row = 0
            item_column = 0

            for item in items:
                item_row, item_column = control.process_item_grid(item_row, item_column)
                item.grid(row=item_row, column=item_column, sticky="nsew", padx=5, pady=5)

def render_widgets(page_number):
    frames = control.retrieve_data("pages", "frames")
    configure_main(page_number)
    match page_number:
        case 1:
            # Display all frames
            frames.get("heading").grid(row=1, column=0, columnspan=2, pady=30)
            frames.get("image").grid(row=2, column=0, columnspan=2, sticky="nsew", padx=30, pady=10)
            frames.get("subtitle").grid(row=3, column=0, columnspan=2, sticky="n", pady=10)
            frames.get("button").grid(row=4, column=0, columnspan=2, sticky="s", pady=20)

        case 2:
            # Display all frames
            frames.get("heading").grid(row=1, column=0, columnspan=2, sticky="n", pady=30)
            frames.get("button").grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=10)
        case 3:
            control.update_page(page_number)

            for category in control.retrieve_data("categories"):
                category.pack(anchor="w", pady=5, padx=5)

            frames.get("category").grid(row=1, column=0, sticky="nsew")
            frames.get("item").grid(row=1, column=1, sticky="nsew")
            frames.get("button").grid(row=2, column=0, columnspan=2, sticky="n", pady=10)
        case 4:
            frames.get("heading").grid(row=1, column=0, columnspan=2, sticky="n")
            frames.get("choices").grid(row=2, column=0, columnspan=2, sticky="new")

def destroy_widgets(widgets):
    for widget in widgets:
        widget.destroy()
