import tkinter as tk
from tkinter import ttk, messagebox
import control as control

# Configure main frame's row and column weight
def configure_main(page_number):
    main_frm = control.retrieve_data("initial_frames")["main"]

    match page_number:
        case 1:
            main_frm.rowconfigure(2, weight=2)
            main_frm.rowconfigure(3, weight=1)
            main_frm.rowconfigure(4, weight=3)
        case 3:
            main_frm.columnconfigure(0, weight=1)
            main_frm.columnconfigure(1, weight=3)
            main_frm.columnconfigure(2, weight=1)
            main_frm.rowconfigure(1, weight=1)
            main_frm.rowconfigure(2, weight=1)
        case 4:
            main_frm.rowconfigure(1, weight=0)
            main_frm.rowconfigure(2, weight=1)
            main_frm.rowconfigure(3, weight=0)
        case 6:
            main_frm.rowconfigure(1, weight=1)
            main_frm.rowconfigure(2, weight=1)
        case 7:
            main_frm.rowconfigure(1, weight=0)
            main_frm.rowconfigure(2, weight=0)
            main_frm.rowconfigure(3, weight=1)
        case 8:
            main_frm.columnconfigure(0, weight=1)
            main_frm.columnconfigure(1, weight=1)
            main_frm.rowconfigure(1, weight=0)
            main_frm.rowconfigure(2, weight=0)
            main_frm.rowconfigure(3, weight=1)
        case 9:
            main_frm.rowconfigure(1, weight=0)
            main_frm.rowconfigure(2, weight=2)
            main_frm.rowconfigure(3, weight=1)
            main_frm.rowconfigure(4, weight=1)

# Set up initial frames for the main screen
def set_up_main_screen(root):
    main_frm = tk.Frame(root, bg="white")
    title_frm = tk.Frame(main_frm, bg="white")
    title_lbl = tk.Label(title_frm, text="Project Keyosk", font=("Arial", 20), pady=5, justify="center", bg="white")
    separator = ttk.Separator(title_frm, orient="horizontal", style="secondary.Horizontal.TSeparator")

    main_frm.rowconfigure(0, weight=0)
    main_frm.columnconfigure(0, weight=1)
    title_frm.columnconfigure(0, weight=1)

    title_lbl.grid(row=0, column=0, sticky="ew")
    separator.grid(row=1, column=0, columnspan=3, sticky="ew")

    title_frm.grid(row=0, column=0, columnspan=3, sticky="ew")
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
            control.update_page(page_number)
        case 4:
            create_fourth_page()
        case 5:
            create_fifth_page()
        case 6:
            create_sixth_page()
        case 7:
            create_seventh_page()
        case 8:
            create_eighth_page()
        case 9:
            create_ninth_page()

    # Make is_page_loaded of specified page to True
    control.pass_data(True, "pages", "is_page_loaded")

# Create home page
def home_page():
    next_page = control.retrieve_data("current_page") + 1
    main_frm = control.retrieve_data("initial_frames")["main"]
    image_object = control.retrieve_data("images")["logo"]
    order_management_page = 8

    heading_frm = tk.Frame(main_frm, bg="white")
    subtitle_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, bg="white")

    image_frm = tk.Frame(
        main_frm,
        relief="solid",
        bd=2,
        bg="white"
    )

    heading = tk.Label(
        heading_frm,
        text="WELCOME!",
        font=("Comic Sans MS", 30, "bold"),
        bg="white"
    )

    image_object = tk.Label(
        image_frm,
        image=image_object,
        width=image_object.width(),
        height=image_object.height(),
        justify="center",
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
        cursor="hand2",
        command=lambda: control.switch_to_page(order_management_page, callback=control.sort_records)
    )

    start_btn = tk.Button(
        button_frm,
        text="START ORDER",
        width=20,
        height=2,
        font=("Arial", 12, "bold"),
        cursor="hand2",
        command=lambda: control.switch_to_page(next_page),
        bg="white"
    )

    # Display all widgets
    heading.grid(row=0, column=0)
    image_object.grid(row=0, column=0)
    subtitle.grid(row=0, column=0)
    see_order_btn.grid(row=0, column=0, padx=5)
    start_btn.grid(row=0, column=1, padx=5)

    frames_dict = {
        "heading": heading_frm,
        "image": image_frm,
        "subtitle": subtitle_frm,
        "button": button_frm
    }

    widgets_dict = {
        "see_order_btn": see_order_btn,
        "start_btn": start_btn
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")
    control.pass_data(widgets_dict, "home_widgets")

def create_second_page():
    main_frm = control.retrieve_data("initial_frames")["main"]
    heading_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, bg="white")
    dine_in_image = control.retrieve_data("images")["dine-in"]
    take_out_image = control.retrieve_data("images")["take-out"]

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
        image=dine_in_image,
        width=dine_in_image.width(),
        height=dine_in_image.height(),
        cursor="hand2",
        command=lambda: control.pass_data({ control.retrieve_data("current_order_number"): {"mode": "dine-in"}}, "order_details", switch=True),
    )

    take_btn = tk.Button(
        button_frm,
        text="TAKE-OUT",
        font=("Arial", 16, "bold"),
        image=take_out_image,
        width=take_out_image.width(),
        height=take_out_image.height(),
        cursor="hand2",
        command=lambda: control.pass_data({ control.retrieve_data("current_order_number"): {"mode": "take-out"}}, "order_details", switch=True)
    )

    # Display all widgets
    heading.grid(row=0, column=0)
    dine_btn.grid(row=0, column=0, sticky="ew", padx=10)
    take_btn.grid(row=0, column=1, sticky="ew", padx=10)

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
    cart_button_frm = tk.Frame(cart_frm, bg="white")
    button_frm = tk.Frame(main_frm, padx=5, bg="white")

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
        height=20
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
        command=control.delete_selected
    )

    clear_cart_btn = tk.Button(
        cart_button_frm,
        text="Clear Cart",
        command=clear_listbox
    )

    cancel_btn = tk.Button(
        button_frm,
        text="CANCEL",
        cursor="hand2",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=lambda: control.switch_to_page(1, callback=clear_listbox),
    )

    done_btn = tk.Button(
        button_frm,
        text="DONE",
        cursor="hand2",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        bg="white",
        command=check_for_input,
    )

    cart_listbox["yscrollcommand"] = cart_scrollbar.set

    # Display all widgets
    cart_heading.grid(row=0, column=0, sticky="n")
    cart_listbox.pack(fill="both", side="left")
    cart_scrollbar.pack(fill="y", side="right")
    listbox_frm.grid(row=1, column=0, sticky="nsew", padx=10)
    cart_total_lbl.grid(row=2, column=0, columnspan=2, sticky="n")
    cart_button_frm.grid(row=3, column=0, sticky="n")
    remove_selected_btn.grid(row=0, column=0)
    clear_cart_btn.grid(row=0, column=1)
    cancel_btn.grid(row=0, column=0, padx=5)
    done_btn.grid(row=0, column=1, padx=5)

    # Hold frames in a dictionary for quick access
    frames_dict = {
        "category": category_frm,
        "item": item_frm,
        "cart": cart_frm,
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
    prev_page = control.retrieve_data("current_page") - 1
    main_frm = control.retrieve_data("initial_frames")["main"]
    heading_frm = tk.Frame(main_frm, bg="white")
    order_details_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, bg="white")

    heading_lbl = tk.Label(
        heading_frm,
        text="ORDER REVIEW",
        font=("Arial", 22, "bold"),
        bg="white"
    )

    order_details_textbox = tk.Text(
        order_details_frm,
        width=60,
        height=20,
        font=("Courier New", 11)
    )

    total_lbl = tk.Label(
        order_details_frm,
        text="Total: PHP 0.00",
        font=("Arial", 14, "bold"),
        bg="white"
    )

    back_btn = tk.Button(
        button_frm,
        text="GO BACK",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=lambda: control.switch_to_page(prev_page, callback=clear_textbox),
    )

    continue_btn = tk.Button(
        button_frm,
        text="CONTINUE",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        bg="white",
        command=lambda: control.process_order(True)
    )

    # Display all widgets
    heading_lbl.grid(row=0, column=0)
    order_details_textbox.grid(row=0, column=0)
    total_lbl.grid(row=1, column=0)
    back_btn.grid(row=0, column=0)
    continue_btn.grid(row=0, column=1)

    frame_dict = {
        "heading": heading_frm,
        "order_details": order_details_frm,
        "button": button_frm
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frame_dict, "is_page_loaded": False }
    }

    widgets_dict = {
        "textbox": order_details_textbox,
        "total": total_lbl
    }

    control.pass_data(page_dict, "pages")
    control.pass_data(widgets_dict, "review_widgets")

def create_fifth_page():
    next_page = control.retrieve_data("current_page") + 1
    thank_you_page = control.retrieve_data("current_page") + 2
    main_frm = control.retrieve_data("initial_frames")["main"]
    heading_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, bg="white")
    
    heading_lbl = tk.Label(heading_frm, text="Mode of Payment", font=("Arial", 22), bg="white")

    cashless_payment_button = tk.Button(
        button_frm,
        text="Pay Here\n(Cashless)",
        font=("Arial", 16),
        width=20,
        height=7,
        bd=2,
        relief="solid",
        bg="lightgreen",
        command=lambda: control.switch_to_page(next_page)
    )

    or_label = tk.Label(button_frm, text="or", font=("Arial", 18), bg="white")

    cash_payment_button = tk.Button(
        button_frm,
        text="Pay at the\ncounter\n(Cash)",
        font=("Arial", 16),
        width=20,
        height=7,
        bd=2,
        relief="solid",
        bg="lightyellow",
        command=lambda: update_details("cash", page=thank_you_page)
    )

    # Display all widgets
    heading_lbl.grid(row=0, column=0, pady=15)
    cashless_payment_button.grid(row=0, column=0, pady=30)
    or_label.grid(row=1, column=0, pady=8)
    cash_payment_button.grid(row=2, column=0, pady=30)

    frames_dict = {
        "heading": heading_frm,
        "button": button_frm
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")

def create_sixth_page():
    next_page = control.retrieve_data("current_page") + 1
    prev_page = control.retrieve_data("current_page") - 1
    main_frm = control.retrieve_data("initial_frames")["main"]
    scan_box_frm = tk.Frame(main_frm, bg="white", relief="solid", bd=2)
    scan_area_frm = tk.Frame(scan_box_frm, width=380, height=250, bd=2, relief="solid", bg="lightgray")
    button_frm = tk.Frame(main_frm, bg="white")

    scan_lbl = tk.Label(scan_box_frm, text="SCAN HERE", font=("Arial", 20, "bold"), bg="white")
    scan_separator = ttk.Separator(scan_box_frm, orient="horizontal")
    scan_image_holder = tk.Label(
        scan_area_frm,
        image=control.retrieve_data("images")["scan"],
        font=("Arial", 100, "bold"),
        bg="lightgray"
    )

    back_btn = tk.Button(
        button_frm,
        text="GO BACK",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        bd=1,
        relief="solid",
        cursor="hand2",
        command=lambda: control.switch_to_page(prev_page)
    )

    done_btn = tk.Button(
        button_frm,
        text="DONE",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        bd=1,
        bg="white",
        cursor="hand2",
        command=lambda: update_details("cashless", page=next_page)
    )

    # Display all widgets
    scan_lbl.grid(row=0, column=0)
    scan_separator.grid(row=1, column=0, sticky="ew")
    scan_image_holder.grid(row=0, column=0)
    scan_area_frm.grid(row=2, column=0, padx=30, pady=30)
    back_btn.grid(row=0, column=0)
    done_btn.grid(row=0, column=1)

    frames_dict = {
        "scan_box": scan_box_frm,
        "button": button_frm
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")

def create_seventh_page():
    main_frm = control.retrieve_data("initial_frames")["main"]
    heading_frm = tk.Frame(main_frm, bg="white")
    order_box_frm = tk.Frame(main_frm, bg="white", bd=2, relief="solid")
    button_frm = tk.Frame(main_frm, bg="white")
    order_number = control.retrieve_data("current_order_number")

    heading_lbl = tk.Label(heading_frm, text="THANK YOU!", font=("Arial", 30, "bold"), fg="green", bg="white")
    subheading_lbl = tk.Label(heading_frm, text="Here's your order no:", font=("Arial", 20), bg="white")
    order_title_lbl = tk.Label(order_box_frm, text="ORDER NO.", font=("Arial", 20, "bold"), bg="white")
    box_separator = ttk.Separator(order_box_frm, orient="horizontal")
    order_number_lbl = tk.Label(order_box_frm, text=str(order_number), font=("Arial", 120, "bold"), fg="red", bg="white")

    ok_btn = tk.Button(
        button_frm,
        text="OK",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        bd=1,
        relief="solid",
        bg="lightgreen",
        cursor="hand2",
        command=lambda: control.switch_to_page(1, callback=clear_order_details)
    )

    # Display all widgets
    heading_lbl.grid(row=0, column=0, pady=15)
    subheading_lbl.grid(row=1, column=0, pady=12)
    order_title_lbl.grid(row=0, column=0)
    box_separator.grid(row=1, column=0, sticky="ew")
    order_number_lbl.grid(row=2, column=0, padx=20, pady=20)
    ok_btn.grid(row=0, column=0)

    frames_dict = {
        "heading": heading_frm,
        "order_box": order_box_frm,
        "button": button_frm
    }

    widgets_dict = {
        "order_number": order_number_lbl
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")
    control.pass_data(widgets_dict, "payment_widgets")

def create_eighth_page():
    main_frm = control.retrieve_data("initial_frames")["main"]
    heading_frm = tk.Frame(main_frm, bg="white")
    in_progress_frm = tk.Frame(main_frm, bg="white")
    done_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, bg="white")

    heading_lbl = tk.Label(heading_frm, text="CURRENT ORDERS", font=("Arial", 22), bg="white")
    in_progress_lbl = tk.Label(in_progress_frm, text="In-Progress", font=("Arial", 16), bg="white")
    done_lbl = tk.Label(done_frm, text="Done", font=("Arial", 16), bg="white")
    go_back_btn = tk.Button(
        button_frm,
        text="GO BACK",
        font=("Arial", 14, "bold"),
        cursor="hand2",
        width=20,
        height=2,
        command=lambda: control.switch_to_page(1)
    )

    in_progress_frm.columnconfigure(0, weight=1)
    done_frm.columnconfigure(0, weight=1)

    # Display all widgets
    heading_lbl.grid(row=0, column=0)
    in_progress_lbl.grid(row=0, column=0, sticky="n")
    done_lbl.grid(row=0, column=0, sticky="n")
    in_progress_frm.grid(row=0, column=0, sticky="n", padx=10)
    done_frm.grid(row=0, column=1, sticky="n", padx=10)
    go_back_btn.grid(row=0, column=1)

    frames_dict = {
        "heading": heading_frm,
        "in-progress": in_progress_frm,
        "done": done_frm,
        "button": button_frm
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")

def create_ninth_page():
    prev_page = control.retrieve_data("current_page") - 1
    main_frm = control.retrieve_data("initial_frames")["main"]
    heading_frm = tk.Frame(main_frm, bg="white")
    textbox_frm = tk.Frame(main_frm, bg="white")
    scrollbar = tk.Scrollbar(textbox_frm, orient="vertical")
    table_textbox = tk.Text(textbox_frm)
    status_frm = tk.Frame(main_frm, bg="white")
    button_frm = tk.Frame(main_frm, bg="white")

    heading_lbl = tk.Label(
        heading_frm,
        text="Order No.",
        font=("Arial", 22),
        bg="white"
    )

    status_lbl = tk.Label(
        status_frm,
        text="Status: ",
        font=("Arial", 13),
        bg="white"
    )

    total_lbl = tk.Label(
        status_frm,
        text=f"Total: ₱",
        font=("Arial", 13),
        bg="white"
    )

    finish_order_btn = tk.Button(
        button_frm,
        text="FINISH ORDER",
        font = ("Arial", 12, "bold"),
        width = 20,
        height = 2,
        command = lambda: control.switch_to_page(prev_page, update_status)
    )

    go_back_btn = tk.Button(
        button_frm,
        text="GO BACK",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=lambda: control.switch_to_page(prev_page)
    )

    status_frm.columnconfigure(0, weight=1)
    status_frm.columnconfigure(1, weight=1)

    table_textbox["yscrollcommand"] = scrollbar.set
    scrollbar.config(command=table_textbox.yview)

    # Display all widgets
    heading_lbl.grid(row=0, column=0, sticky="ew")
    table_textbox.grid(row=0, column=0)
    scrollbar.grid(row=0, column=1, sticky="ns")
    status_lbl.grid(row=0, column=0, sticky="w", padx=50)
    total_lbl.grid(row=0, column=1, sticky="e", padx=50)
    finish_order_btn.grid(row=0, column=0)
    go_back_btn.grid(row=0, column=1)

    frames_dict = {
        "heading": heading_frm,
        "textbox": textbox_frm,
        "status": status_frm,
        "button": button_frm
    }

    widgets_dict = {
        "heading": heading_lbl,
        "status": status_lbl,
        "total": total_lbl,
        "textbox": table_textbox,
        "finish_order": finish_order_btn
    }

    page_dict = {
        control.retrieve_data("current_page"): { "frames": frames_dict, "is_page_loaded": False }
    }

    control.pass_data(page_dict, "pages")
    control.pass_data(widgets_dict, "management_widgets")

# Switch to specified page
def switch_to(page_number, callback=None):
    control.clear_page()
    control.pass_data(page_number, "current_page")

    if not control.retrieve_data("pages", "is_page_loaded"):
        control.load_page(page_number)
    control.render_page(page_number)

    if callback:
        callback()

# Create category buttons
def make_category_cards():
    categories_arr = []
    # Makes a category button based on category names
    for category_name in control.retrieve_data("category_names"):
        image_object = control.retrieve_data("images")["categories"].get(category_name)
        category_btn = tk.Button(
            control.retrieve_data("pages", "frames").get("category"),
            image=image_object,
            width=image_object.width(),
            height=image_object.height(),
            borderwidth=2,
            relief="solid",
            cursor="hand2",
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
    item_names = control.retrieve_data("item_names")
    current_category = control.retrieve_data("current_category")

    # Makes an item button by amount times
    for item in range(amount):
        item_name = list(item_names[current_category].keys())[item]
        image_object = control.retrieve_data("images")[current_category][item_name]
        text_info = f"{item_name}\nPHP {item_names[current_category][item_name]}.00"

        item_btn = tk.Button(
            control.retrieve_data("pages", "frames").get("item"),
            text=text_info,
            font=("Arial", 12, "bold"),
            cursor="hand2",
            image=image_object,
            compound="top",
            width=image_object.width() + 40,
            height=200,
            borderwidth=2,
            relief="solid",
            command=lambda item_name=item_name: add_to_cart(item_name),
            bg="white"
        )
        # Stores created button to an array
        items_arr.append(item_btn)
    # Returns the array
    control.pass_data(items_arr, "items")

def update_details(payment_mode, page):
    current_order_number = control.retrieve_data("current_order_number")
    control.update_order_details("Unpaid", "payment_status")
    control.update_order_details("in-progress", "status")

    if payment_mode == "cashless":
        control.update_order_details("Paid", "payment_status")
        control.update_order_details("done", "status")


    control.switch_to_page(page)

    control.retrieve_data("payment_widgets")["order_number"].config(text=str(current_order_number))

def check_for_input():
    cart_orders = control.retrieve_data("cart_orders")

    if not cart_orders:
        messagebox.showerror("Error", "Your cart is empty.")
        return
    control.switch_to_page(4)

# Store chosen item to cart
def add_to_cart(item_name):
    control.pass_to_cart(item_name)
    update_page(3)

# Change item display according to category
def change_category(_category_name):
    control.destroy_widgets(control.retrieve_data("items"))
    control.pass_data(_category_name, "current_category")

    make_item_cards(amount = len(control.retrieve_data("item_names")[_category_name]))
    update_page(3)

def create_order_buttons(parent, order_list, status):
    container = tk.Frame(parent, bg="white")
    container.grid(row=1, column=0)

    row = 0
    col = 0
    for order_no in order_list:
        order_button = tk.Button(
            container,
            text=str(order_no),
            font=("Arial", 16, "bold"),
            width=6,
            height=2,
            command=lambda order_no=order_no: update_order_info(order_no)
        )

        order_button.grid(row=row, column=col, padx=8, pady=8)
        destination = "in_progress_buttons"
        if status == "done":
            destination = "done_buttons"
        control.pass_data({order_no: order_button}, destination)

        col += 1
        if col > 1:
            col = 0
            row += 1

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

def clear_textbox():
    textbox = control.retrieve_data("review_widgets")["textbox"]
    textbox.config(state="normal")
    control.clear_widgets(textbox)

def clear_listbox():
    listbox = control.retrieve_data("cart_widgets")["listbox"]
    total_lbl = control.retrieve_data("cart_widgets")["total"]
    control.clear_widgets(listbox)
    control.clear_orders("cart_orders")
    total_lbl.config(text="Total: PHP 0.00")

def clear_order_details():
    clear_listbox()
    clear_textbox()
    update_order_number()
    control.clear_orders("order_details")

def update_order_info(order_num):
    control.switch_to_page(9)
    heading_lbl = control.retrieve_data("management_widgets")["heading"]
    textbox = control.retrieve_data("management_widgets")["textbox"]
    status_lbl = control.retrieve_data("management_widgets")["status"]
    total_lbl = control.retrieve_data("management_widgets")["total"]
    finish_order_btn = control.retrieve_data("management_widgets")["finish_order"]
    records = control.retrieve_data("order_records")
    item_names = control.retrieve_data("item_names")

    control.pass_data(order_num, "selected_order_number")

    update_widgets(textbox, clear=True)
    textbox.config(state="normal")

    textbox.insert(1.0, "-".ljust(80, "-") + "Item".ljust(50) + "Qty".ljust(8) + "PHP".ljust(22) + "-".ljust(80, "-"))

    record_object = {}
    items = []
    orders = []

    for record in records:
        if record == order_num:
            record_object = records[record]
            orders = records[record]["orders"]
            break

    for order in orders:
        for category in item_names:
            if order in item_names[category]:
                order_info = (category, order, orders[order].get("quantity"), orders[order].get("cost"))
                items.append(order_info)

    total = 0
    for idx, (cat, name, qty, price) in enumerate(items, start=1):
        subtotal = qty * price
        total += subtotal
        image_object = control.retrieve_data("images")[cat][name]

        textbox.image_create(f"{idx + 1}.end", image=image_object)
        textbox.insert(f"{idx + 1}.end", f" {cat} - {name}".ljust(34) + str(qty).ljust(8) + f"₱{subtotal:.2f}".ljust(23))

    heading_lbl.config(text=f"Order No. {order_num}")
    status_lbl.config(text=f"Status: {record_object.get("payment_status")}")
    total_lbl.config(text=f"Total: PHP {total}.00")
    textbox.config(state="disabled")
    if "Unpaid" in status_lbl.cget("text"):
        finish_order_btn.grid()
    else:
        finish_order_btn.grid_remove()

def update_order_number():
    current_order_number = control.retrieve_data("current_order_number")
    control.pass_data(current_order_number + 1, "current_order_number")

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

def update_review_widgets():
    cart_orders = control.retrieve_data("cart_orders")
    order_names = list(cart_orders.keys())
    textbox = control.retrieve_data("review_widgets")["textbox"]
    total_lbl = control.retrieve_data("review_widgets")["total"]

    content = "ITEM".ljust(20) + "QTY".ljust(8) + "SUBTOTAL\n" + "-".ljust(60, "-") + "\n"
    textbox.insert("end", content)

    for order_name in order_names:
        quantity = cart_orders[order_name]["quantity"]
        cost = cart_orders[order_name]["cost"]
        content = f"{order_name}".ljust(20) + f"{quantity}".ljust(8) + f"{quantity * cost}.00\n"
        textbox.insert("end", content)

    total_lbl.config(text=f"{control.retrieve_data('cart_widgets')['total'].cget('text')}")
    textbox.config(state="disabled")

def update_order_cards():
    in_progress_items = control.retrieve_data("in_progress_items")
    done_items = control.retrieve_data("done_items")
    in_progress_frm = control.retrieve_data("pages", "frames")["in-progress"]
    done_frm = control.retrieve_data("pages", "frames")["done"]

    create_order_buttons(in_progress_frm, in_progress_items, "in-progress")
    create_order_buttons(done_frm, done_items, "done")

def picture_slot(parent, category, item_name):
    image_object = control.retrieve_data("images")[category][item_name]
    slot = tk.Frame(parent, width=image_object.width(), height=image_object.height(), bg="white", bd=1, relief="solid")
    tk.Label(slot, image=image_object, font=("Arial", 10)).pack(expand=True)
    return slot

def update_status():
    records = control.retrieve_data("order_records")
    order_num = control.retrieve_data("selected_order_number")
    in_progress_items = control.retrieve_data("in_progress_items")
    done_items = control.retrieve_data("done_items")
    in_progress_buttons = control.retrieve_data("in_progress_buttons")
    finish_order_btn = control.retrieve_data("management_widgets")["finish_order"]

    for record in records:
        if record == order_num:
            record_object = records[record]
            record_object["status"] = "done"
            record_object["payment_status"] = "Paid"
            break

    in_progress_items.remove(order_num)
    done_items.append(order_num)
    in_progress_buttons[order_num].destroy()
    finish_order_btn.grid_remove()
    update_page(8)

def update_page(page_number):
    match page_number:
        case 3:
            update_cart()
            update_items()
        case 4:
            update_review_widgets()
        case 8:
            update_order_cards()

def render_widgets(page_number):
    frames = control.retrieve_data("pages", "frames")
    match page_number:
        case 1:
            # Display all frames
            frames.get("heading").grid(row=1, column=0, pady=10)
            frames.get("image").grid(row=2, column=0, padx=30, pady=10)
            frames.get("subtitle").grid(row=3, column=0, sticky="n", pady=10)
            frames.get("button").grid(row=4, column=0, sticky="s", pady=20)
        case 2:
            # Display all frames
            frames.get("heading").grid(row=1, column=0, columnspan=2, sticky="n", pady=30)
            frames.get("button").grid(row=2, column=0, columnspan=2, padx=20, pady=30)
        case 3:
            for category in control.retrieve_data("categories"):
                category.pack(anchor="w", pady=5, padx=10)

            frames.get("category").grid(row=1, column=0, sticky="nsew", pady=20)
            frames.get("item").grid(row=1, column=1, sticky="nsew", pady=20)
            frames.get("cart").grid(row=1, column=2, columnspan=2, sticky="n", pady=20)
            frames.get("button").grid(row=3, column=0, columnspan=4, sticky="s", pady=10)
        case 4:
            update_page(4)
            frames.get("heading").grid(row=1, column=0, pady=10)
            frames.get("order_details").grid(row=2, column=0, sticky="n", pady=10)
            frames.get("button").grid(row=3, column=0, padx=10, pady=10)
        case 5:
            frames.get("heading").grid(row=1, column=0)
            frames.get("button").grid(row=2, column=0)
        case 6:
            frames.get("scan_box").grid(row=1, column=0, pady=20)
            frames.get("button").grid(row=2, column=0, pady=20, sticky="s")
        case 7:
            frames.get("heading").grid(row=1, column=0)
            frames.get("order_box").grid(row=2, column=0, pady=30)
            frames.get("button").grid(row=3, column=0)
        case 8:
            frames.get("heading").grid(row=1, column=0, columnspan=2, pady=30)
            frames.get("in-progress").grid(row=2, column=0, sticky="n", pady=30)
            frames.get("done").grid(row=2, column=1, sticky="n", pady=30)
            frames.get("button").grid(row=3, column=0, columnspan=2, sticky="s", pady=20)
        case 9:
            frames.get("heading").grid(row=1, column=0, sticky="n", pady=10)
            frames.get("textbox").grid(row=2, column=0)
            frames.get("status").grid(row=3, column=0, sticky="n")
            frames.get("button").grid(row=4, column=0, sticky="s", pady=10)

            textbox = control.retrieve_data("management_widgets")["textbox"]

            if textbox:
                textbox.config(state="normal")
                textbox.delete("end")

def update_widgets(widgets, destroy=False, clear=False):
    if destroy:
        for widget in widgets:
            widget.destroy()
    elif clear:
        try:
            widgets.delete(1.0, "end")
        except tk.TclError:
            widgets.delete(0, "end")