# Initialize master dictionary
master_dict = {
    "pages": {},
    "initial_frames": {},
    "categories": [],
    "items": [],
    "images": {},
    "category_names": {
        "Ulam": 1,
        "Rice": 2,
        "Sides": 3,
        "Desserts": 4,
        "Drinks": 5
    },
    "current_page": 0,
    "prev_category": "Ulam",
    "MAX_ROW": 8,
    "MAX_COLUMN": 4
}

# Update existing data in master dictionary
def update_data(data_object, destination, deep_dest=None):
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