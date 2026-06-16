# Initialize master dictionary
from turtledemo.clock import current_day

import control

master_dict = {
    "pages": {},
    "initial_frames": {},
    "categories": [],
    "items": [],
    "images": {},
    "current_page": 0,
    "current_category": "Ulam",
    "order_details": {},
    "cart_widgets": {},
    "review_widgets": {},
    "cart_orders": {},
    "MAX_ROW": 8,
    "MAX_COLUMN": 4,
    "category_names": [
        "Ulam",
        "Rice",
        "Sides",
        "Desserts",
        "Drinks"
    ],
    "item_names": {
        "Ulam": {
            "Adobo": 120,
            "Sinigang": 150,
            "Kare-Kare": 180,
            "Chicken Inasal": 140,
            "Bistek Tagalog": 160
        },
        "Rice": {
            "Plain Rice": 20,
            "Sinangag": 35,
            "Brown Rice": 40
        },
        "Sides": {
            "Lumpiang Shanghai": 60,
            "Tokwa't Baboy": 80,
            "Chicharon Bulaklak": 90,
            "Kwek-Kwek": 50
        },
        "Desserts": {
            "Halo-Halo": 90,
            "Leche Flan": 70,
            "Turon": 40,
            "Buko Pandan": 60
        },
        "Drinks": {
            "Coke": 45,
            "Sprite": 45,
            "Iced Tea": 40,
            "Calamansi Juice": 35
        }
    }
}

# Update existing data in master dictionary
def update_data(data_object, destination, deep_dest=None, switch=False):
    current_page = master_dict.get("current_page")

    if deep_dest:
        try:
            master_dict[destination][current_page][deep_dest].update(data_object)
        except AttributeError:
            master_dict[destination][current_page][deep_dest] = data_object
    else:
        try: # Run this if destination is a dictionary
            master_dict[destination].update(data_object)
        except AttributeError, TypeError: # Run this if not
            master_dict[destination] = data_object

    if switch:
        control.switch_to_page(current_page + 1)

# Get existing data in master dictionary
def get_data(destination, deep_dest=None):
    request = master_dict.get(destination)
    current_page = master_dict.get("current_page")
    if deep_dest:
        try:
            request = master_dict[destination][current_page][deep_dest]
        except KeyError:
            request = 0
    return request

# Update values in the cart
def update_cart(item_name):
    cart_orders = master_dict.get("cart_orders")
    current_category = master_dict.get("current_category")

    if item_name in cart_orders:
        quantity = cart_orders[item_name].get("quantity")
        quantity += 1
        quantity_dict = {"quantity": quantity}
        cart_orders[item_name].update(quantity_dict)
    else:
        item_cost = master_dict["item_names"][current_category].get(item_name)
        item_dict = { item_name: {"quantity": 1, "cost": item_cost} }
        cart_orders.update(item_dict)

# Process order details into readable format
def process_order():
    control.switch_to_page(4)

# Process the position change of items
def process_item_grid(item_row, item_column):
    if (item_column + 1 % 3) > 0 and item_column + 1 > 3:
        item_row += 1
        item_column = 0
    item_column += 1

    return item_row, item_column

def remove_item():
    listbox = master_dict["cart_widgets"]["listbox"]
    orders = list(master_dict["cart_orders"].keys())
    cart_orders = master_dict["cart_orders"]
    selected_item_index = listbox.curselection()

    if not selected_item_index:
        return

    selected_item = orders[selected_item_index[0]]
    listbox.delete(selected_item_index[0])
    del cart_orders[selected_item]

def clear_items():
    cart_orders = master_dict["cart_orders"]
    cart_orders.clear()