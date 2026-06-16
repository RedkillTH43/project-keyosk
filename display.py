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
            main_frm.rowconfigure(1, weight=0)
            main_frm.rowconfigure(2, weight=0)
            main_frm.rowconfigure(3, weight=1)
            main_frm.rowconfigure(4, weight=0)

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
            create_third_page()
            make_category_cards()
            make_item_cards(len(control.retrieve_data("item_names").get(control.retrieve_data("current_category"))))
            update_items()
        case 4:
            create_fourth_page()

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
        command=lambda: control.pass_data({"mode": "dine-in"}, "order_details", switch=True),
    )

    take_btn = tk.Button(
        button_frm,
        text="TAKE-OUT",
        font=("Arial", 16, "bold"),
        bg="#3498db",
        fg="white",
        width=8,
        height=12,
        command=lambda: control.pass_data({"mode": "take-out"}, "order_details", switch=True)
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
def create_third_page():
    main_frm = control.retrieve_data("initial_frames").get("main")
    category_frm = tk.Frame(main_frm, bg="white")
    item_frm = tk.Frame(main_frm, bg="white")
    cart_frm = tk.Frame(main_frm, bg="#fafafa")
    listbox_frm = tk.Frame(cart_frm, bg="white")
    cart_button_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, padx=5)

    cart_frm.columnconfigure(0, weight=1)
    cart_frm.columnconfigure(1, weight=2)
    cart_frm.columnconfigure(2, weight=1)

    cart_heading = tk.Label(
        cart_frm,
        text="Order Details",
        font=("Arial", 14, "bold"),
        bg="#fafafa"
    )

    cart_listbox = tk.Listbox(
        listbox_frm,
        width=35,
        height=8
    )

    cart_scrollbar = ttk.Scrollbar(
        listbox_frm,
        orient="vertical",
        command=cart_listbox.yview
    )

    cart_total_lbl = tk.Label(
        cart_frm,
        text="Total: PHP 0.00",
        font=("Arial", 12, "bold"),
        bg="#fafafa"
    )

    remove_selected_btn = tk.Button(
        cart_button_frm,
        text="Remove Selected",
        bg="tomato",
        fg="white",
        command=lambda: control.delete_selected()
    )

    clear_cart_btn = tk.Button(
        cart_button_frm,
        text="Clear Cart"
    )

    cancel_btn = tk.Button(
        button_frm,
        text="Cancel",
        cursor="hand2",
        command=lambda: control.switch_to_page(1),
        bg="white"
    )

    # ToDo: Connect to the review page of ordersequence.py
    done_btn = tk.Button(
        button_frm,
        text="Done",
        cursor="hand2",
        bg="white"
    )

    cart_listbox["yscrollcommand"] = cart_scrollbar.set

    # Display all widgets
    cart_heading.grid(row=0, column=0, sticky="n")
    cart_listbox.pack(fill="both", side="left")
    cart_scrollbar.pack(fill="y", side="right")
    listbox_frm.grid(row=1, column=0, sticky="nsew", padx=10)
    cart_total_lbl.grid(row=2, column=0, columnspan=2, sticky="n")
    remove_selected_btn.grid(row=0, column=0)
    clear_cart_btn.grid(row=0, column=1)
    cancel_btn.grid(row=0, column=0, padx=5)
    done_btn.grid(row=0, column=1, padx=5)

    # Hold frames in a dictionary for quick access
    frames_dict = {
        "category": category_frm,
        "item": item_frm,
        "cart": cart_frm,
        "cart_button": cart_button_frm,
        "button": button_frm
    }

    widgets_dict = {
        "listbox": cart_listbox,
        "total": cart_total_lbl
    }

    # Make dictionary to hold page widgets
    page_dict = { control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False } }

    control.pass_data(page_dict, "pages")
    control.pass_data(widgets_dict, "cart_widgets")

# Make the widgets and frames for the fourth page
def create_fourth_page():
    pass

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
def make_item_cards(amount):
    items_arr = []
    current_category = control.retrieve_data("current_category")
    # Makes an item button by amount times
    for item in range(amount):
        item_name = list(control.retrieve_data("item_names")[current_category].keys())[item]
        item_btn = tk.Button(
            control.retrieve_data("pages", "frames").get("item"),
            text=item_name,
            cursor="hand2",
            image=control.retrieve_data("images").get("item_image"),
            compound="top",
            width=100,
            height=150,
            borderwidth=2,
            relief="solid",
            command=lambda item_name=item_name: add_to_cart(item_name),
            bg="white"
        )
        # Stores created button to an array
        items_arr.append(item_btn)
    # Returns the array
    control.pass_data(items_arr, "items")

# Store chosen item to cart
def add_to_cart(item_name):
    control.pass_to_cart(item_name)
    update_cart()

# Change item display according to category
def change_category(_category_name):
    destroy_widgets(control.retrieve_data("items"))
    control.pass_data(_category_name, "current_category")

    make_item_cards(amount = len(control.retrieve_data("item_names")[_category_name]))
    update_items()

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
def update_items():
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

def update_cart():
    item_details = []
    total_cost = 0
    cart_listbox = control.retrieve_data("cart_widgets")["listbox"]
    cart_total = control.retrieve_data("cart_widgets")["total"]
    orders = control.retrieve_data("cart_orders")

    if not orders:
        cart_total.config(text=f"Total: PHP 0.00")
        return

    for item in list(orders.keys()):
        quantity = orders[item]["quantity"]
        cost = orders[item]["cost"]
        item_details.append(f"{item} x{quantity} = PHP {cost * quantity}")

    for item in list(orders.keys()):
        quantity = orders[item]["quantity"]
        cost = orders[item]["cost"]
        total_cost += quantity * cost

    cart_total.config(text=f"Total: PHP {total_cost}.00")
    cart_items = tk.Variable(value=item_details)

    cart_listbox.config(listvariable=cart_items)


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
            for category in control.retrieve_data("categories"):
                category.pack(anchor="w", pady=5, padx=5)

            frames.get("category").grid(row=1, column=0, sticky="nsew", pady=20)
            frames.get("item").grid(row=1, column=1, sticky="nsew", pady=20)
            frames.get("cart").grid(row=2, column=0, columnspan=2, sticky="n")
            frames.get("cart_button").grid(row=3, column=0, columnspan=2, sticky="n", pady=10)
            frames.get("button").grid(row=4, column=0, columnspan=2, sticky="s", pady=10)
        case 4:
            pass

def destroy_widgets(widgets):
    for widget in widgets:
        widget.destroy()
