import tkinter as tk
from tkinter import PhotoImage
import display as display_mod

# Initializes main screen
root = tk.Tk()
root.title("Project Keyosk")
root.geometry("600x800")

# Create images
category_image = PhotoImage(file="./assets/png.png")
item_image = PhotoImage(file="./assets/item.png")
images_dict = {"item_image": item_image, "category_image": category_image}

# Create main frame
main_frm = tk.Frame(root)

display_mod.setup(main_frm, images_dict)
display_mod.make_category_cards()
display_mod.make_item_cards()
display_mod.render_widgets()

main_frm.pack(expand=True, fill="both", padx=10)

# Ensures program keeps running
root.mainloop()