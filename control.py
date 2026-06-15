import display as display_mod
import model as model

# Load the main screen
def load_screen(root):
    display_mod.set_up_main_screen(root)

# Switch to specified page
def switch_to_page(page_number):
    display_mod.switch_to(page_number)

# Clear specified page
def clear_page():
    display_mod.clear_screen()

# Destroy specified list of widgets
def destroy_widgets(widgets):
    display_mod.destroy_widgets(widgets)

# Update specified page
def update_page():
    display_mod.update_items()

# Load specified page
def load_page(page_number):
    display_mod.set_up_page(page_number)

# Render specified page
def render_page(page_number):
    display_mod.render_widgets(page_number)

# Pass data object to model
def pass_data(data_object, destination, deep_dest=None):
    model.update_data(data_object, destination, deep_dest)

# Retrieve data object from model
def retrieve_data(destination, deep_dest=None):
    return model.get_data(destination, deep_dest)