import tkinter as tk
from tkinter import PhotoImage
import control as control

# Initializes main screen
root = tk.Tk()
root.title("Project Keyosk")
root.geometry("600x800")

# Create images
category_image = PhotoImage(file="./assets/png.png")
item_image = PhotoImage(file="./assets/item.png")
images_dict = {"item_image": item_image, "category_image": category_image}

control.pass_data(images_dict, "images")

control.setup(root)

control.switch_to_page(3)

control.retrieve_data("frames", "main").pack(expand=True, fill="both", padx=10)

# Ensures program keeps running
root.mainloop()