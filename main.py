import tkinter as tk
from tkinter import PhotoImage
import control as control

# Initializes main screen
root = tk.Tk()
root.title("Project Keyosk")
root.geometry("1000x800")

# Create images
category_names = control.retrieve_data("category_names")
item_names = control.retrieve_data("item_names")

print("Loading images...")
logo_image = PhotoImage(file=f"./assets/logo.png")
logo_image = logo_image.subsample(6, "")

take_out_image = PhotoImage(file=f"./assets/take-out.png")
take_out_image = take_out_image.subsample(8, "")

dine_in_image = PhotoImage(file=f"./assets/dine-in.png")
dine_in_image = dine_in_image.subsample(8 , "")

scan_image = PhotoImage(file=f"./assets/scan.png")
scan_image = scan_image.subsample(6, "")

images_dict = {
    "Filipino Dishes": {},
    "Rice": {},
    "Sides": {},
    "Desserts": {},
    "Drinks": {},
    "categories": {},
    "logo": logo_image,
    "dine-in": dine_in_image,
    "take-out": take_out_image,
    "scan": scan_image,
}

for category in category_names:
    image_object = PhotoImage(file=f"./assets/categories/{category.lower()}.png")
    image_object = image_object.subsample(22, "")
    images_dict["categories"].update({category: image_object})

    for item in item_names[category]:
        image_object = PhotoImage(file=f"./assets/{category.lower()}/{item.lower()}.png")
        image_object = image_object.subsample(20, "")
        images_dict[category].update({item: image_object})

control.pass_data(images_dict, "images")
print("Loaded successfully!")

control.load_screen(root)
control.switch_to_page(1)

# Ensures program keeps running
root.mainloop()