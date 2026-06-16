# Initialize master dictionary
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
    "cart_orders": {},
    "MAX_ROW": 8,
    "MAX_COLUMN": 4,
    "category_names": {
        "Ulam": 1,
        "Rice": 2,
        "Sides": 3,
        "Desserts": 4,
        "Drinks": 5
    },
    "item_names": {
        "Ulam": [
            "Adobo",
            "Sinigang",
            "Kare-Kare",
            "Chicken Inasal",
            "Bistek Tagalog"
        ],
        "Rice": [
            "Plain Rice",
            "Sinangag",
            "Brown Rice"
        ],
        "Sides": [
            "Lumpiang Shanghai",
            "Tokwa't Baboy",
            "Chicharon Bulaklak",
            "Kwek-Kwek"
        ],
        "Desserts": [
            "Halo-Halo",
            "Leche Flan",
            "Turon",
            "Buko Pandan"
        ],
        "Drinks": [
            "Coke",
            "Sprite",
            "Iced Tea",
            "Calamansi Juice"
        ]
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

    if item_name in cart_orders.keys():
        quantity = cart_orders[item_name].get("quantity")
        quantity += 1
        quantity_dict = {"quantity": quantity}
        cart_orders[item_name].update(quantity_dict)
    else:
        item_dict = { item_name: {"quantity": 1} }
        cart_orders.update(item_dict)

# Process order details into readable format
def process_order(order_details):
    pass

# Process the position change of items
def process_item_grid(item_row, item_column):
    if (item_column + 1 % 3) > 0 and item_column + 1 > 3:
        item_row += 1
        item_column = 0
    item_column += 1

    return item_row, item_column