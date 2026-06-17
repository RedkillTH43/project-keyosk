import control

# Initialize master dictionary
master_dict = {
    "pages": {},
    "initial_frames": {},
    "categories": [],
    "items": [],
    "images": {},
    "current_order_number": 0,
    "current_page": 0,
    "current_category": "Ulam",
    "order_details": {},
    "order_records": [],
    "in_progress_items": [],
    "done_items": [],
    "home_widgets": {},
    "cart_widgets": {},
    "review_widgets": {},
    "payment_widgets": {},
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
        except (AttributeError, TypeError): # Run this if not
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
def process_order(switch=False):
    order_details = master_dict["order_details"]
    next_page = master_dict["current_page"] + 1
    current_order_number = master_dict["current_order_number"]
    orders = master_dict["cart_orders"]
    total_cost = 0

    for item in list(orders.keys()):
        quantity = orders[item].get("quantity")
        cost = orders[item].get("cost")
        total_cost += quantity * cost

    order_details[current_order_number]["orders"] = orders
    order_details[current_order_number].update({ "total": total_cost })
    master_dict["order_records"].append(order_details)
    if switch:
        control.switch_to_page(next_page)

def update_order_details(data, destination):
    current_order_number = master_dict["current_order_number"]
    master_dict["order_details"][current_order_number].update({destination: data})

def sort_records():
    order_records = master_dict["order_records"]
    in_progress_list = []
    done_list = []
    counter = 1

    for record in order_records:
        if record[counter].get("status") == "in-progress":
            in_progress_list.append(list(record.keys())[0])
        else:
            done_list.append(list(record.keys())[0])
        counter += 1

    master_dict["in_progress_items"] = in_progress_list
    master_dict["done_items"] = done_list

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

def clear_items(destination):
    master_dict[destination] = {}