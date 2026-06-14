import display as display_mod
import model as model

def setup():
    display_mod.setup_frames()
    display_mod.make_category_cards()
    display_mod.make_item_cards()

# Switch to specified page
def switch_to_page(page_number):
    model.master_dict["current_page"] = page_number
    clear_page()
    if not model.master_dict.get("tracker").get("is_page_loaded").get(page_number):
        load_page(page_number)
    render_page(page_number)

# Clear specified page
def clear_page():
    display_mod.clear_screen()

def destroy_widgets(widgets):
    display_mod.destroy_widgets(widgets)

# Update specified page
def update_page(page_number):
    pass

# Load specified page
def load_page(page_number):
    if page_number == 3:
        setup()

    elif page_number == 4:
        display_mod.pick_meal_type()

    model.master_dict["tracker"].get("is_page_loaded")[page_number] = True

# Render specified page
def render_page(page_number):
    display_mod.render_widgets(page_number)

# Pass data object to model
def pass_data(data_object, destination):
    try:
        model.master_dict[destination].update(data_object)
    except AttributeError:
        model.master_dict[destination] = data_object

# Retrieve data object from model
def retrieve_data(destination):
    return model.master_dict.get(destination)