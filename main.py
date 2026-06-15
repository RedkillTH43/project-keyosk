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

control.load_screen(root)

control.retrieve_data("pages", "frames").get("main")

# Ensures program keeps running
root.mainloop()