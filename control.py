import tkinter as tk
import display as display_mod
import model as model

# Setup main screen
def setup(root):
    model.master_dict["frames"]["main"] = tk.Frame(root)

# Switch to specified page
def switch_to_page(page_number):
    model.master_dict["current_page"] = page_number
    match page_number:
        case 3:
            display_mod.setup_frames()
            display_mod.make_category_cards()
            display_mod.make_item_cards()
            render_page(page_number)
        case 4:
            clear_page()
            display_mod.pick_meal_type()
            render_page(page_number)



# Clear specified page
def clear_page():
    display_mod.clear_screen()

# Update specified page
def update_page(page_number):
    pass

# Load specified page
def load_page(page_number):
    pass

# Render specified page
def render_page(page_number):
    display_mod.render_widgets(page_number)

# Pass data object to model
def pass_data(data_object, destination, deep_dest=None):
    try:
        model.master_dict[destination].update(data_object)
    except AttributeError, ValueError:
        model.master_dict[destination] = data_object

# Retrieve data object from model
def retrieve_data(destination, deep_dest=None):
    try:
        request = model.master_dict.get(destination).get(deep_dest)
        if not request:
            request = model.master_dict.get(destination)
    except AttributeError:
        request = model.master_dict.get(destination)
    return request