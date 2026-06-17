import display as display_mod
import model as model

# Load the main screen
def load_screen(root):
    display_mod.set_up_main_screen(root)

# Switch to specified page
def switch_to_page(page_number, callback=None):
    display_mod.switch_to(page_number, callback)

# Clear specified page
def clear_page():
    display_mod.clear_screen()

# Destroy specified list of widgets
def destroy_widgets(widgets):
    display_mod.update_widgets(widgets, destroy=True)

def clear_widgets(widgets):
    display_mod.update_widgets(widgets, clear=True)

# Load specified page
def load_page(page_number):
    display_mod.set_up_page(page_number)

# Render specified page
def render_page(page_number):
    display_mod.render_widgets(page_number)
    display_mod.configure_main(page_number)

# Pass data object to model
def pass_data(data_object, destination, deep_dest=None, switch=False):
    model.update_data(data_object, destination, deep_dest, switch)

# Retrieve data object from model
def retrieve_data(destination, deep_dest=None):
    return model.get_data(destination, deep_dest)

# Process item grid positions
def process_item_grid(item_row, item_column):
    return model.process_item_grid(item_row, item_column)

# Save chosen item to cart
def pass_to_cart(item_name):
    model.update_cart(item_name)

# Process order details
def process_order():
    model.process_order()

def delete_selected():
    model.remove_item()
    display_mod.update_cart()

def clear_orders():
    model.clear_items()