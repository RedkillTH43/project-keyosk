import tkinter as tk
from tkinter import messagebox


class OrderSequenceApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("KEYOSK - Order Sequence Module")
        self.geometry("900x700")
        self.configure(bg="white")

        self.cart = []
        self.total_price = 0

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (Page5_Ordering, Page6_Review):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Page5_Ordering")

    def show_frame(self, page_name):

        frame = self.frames[page_name]

        if hasattr(frame, "refresh_page"):
            frame.refresh_page()

        frame.tkraise()


# ==================================================
# PAGE 5
# ==================================================
class Page5_Ordering(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")

        self.controller = controller

        self.menu_data = {

            "Ulam": [
                ("Adobo", 120),
                ("Sinigang", 150),
                ("Kare-Kare", 180),
                ("Chicken Inasal", 140),
                ("Bistek Tagalog", 160)
            ],

            "Rice": [
                ("Plain Rice", 20),
                ("Sinangag", 35),
                ("Brown Rice", 40)
            ],

            "Sides": [
                ("Lumpiang Shanghai", 60),
                ("Tokwa't Baboy", 80),
                ("Chicharon Bulaklak", 90),
                ("Kwek-Kwek", 50)
            ],

            "Desserts": [
                ("Halo-Halo", 90),
                ("Leche Flan", 70),
                ("Turon", 40),
                ("Buko Pandan", 60)
            ],

            "Drinks": [
                ("Coke", 45),
                ("Sprite", 45),
                ("Iced Tea", 40),
                ("Calamansi Juice", 35)
            ]
        }

        # Header
        tk.Label(
            self,
            text="KEYOSK",
            font=("Arial", 22, "bold"),
            bg="white"
        ).pack(pady=10)

        # Main Body
        body = tk.Frame(self, bg="white")
        body.pack(fill="both", expand=True)

        # Sidebar
        sidebar = tk.Frame(body, bg="#f0f0f0", width=130)
        sidebar.pack(side="left", fill="y")

        tk.Label(
            sidebar,
            text="Categories",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack(pady=10)

        for category in self.menu_data.keys():

            tk.Button(
                sidebar,
                text=category,
                width=12,
                command=lambda c=category: self.load_category(c)
            ).pack(pady=5)

        # Menu Area
        self.menu_frame = tk.Frame(body, bg="white")
        self.menu_frame.pack(side="left", fill="both", expand=True)

        # Cart Area
        cart_frame = tk.Frame(body, bg="#fafafa", width=280)
        cart_frame.pack(side="right", fill="y")

        tk.Label(
            cart_frame,
            text="MY ORDERS",
            font=("Arial", 14, "bold"),
            bg="#fafafa"
        ).pack(pady=10)

        self.cart_listbox = tk.Listbox(
            cart_frame,
            width=35,
            height=20
        )

        self.cart_listbox.pack()

        self.total_label = tk.Label(
            cart_frame,
            text="Total: PHP 0.00",
            font=("Arial", 12, "bold"),
            bg="#fafafa"
        )

        self.total_label.pack(pady=10)

        tk.Button(
            cart_frame,
            text="Remove Selected",
            bg="tomato",
            fg="white",
            command=self.remove_item
        ).pack(pady=5)

        tk.Button(
            cart_frame,
            text="Clear Cart",
            command=self.clear_cart
        ).pack()

        # Quantity
        qty_frame = tk.Frame(self, bg="white")
        qty_frame.pack(pady=10)

        tk.Label(
            qty_frame,
            text="Quantity:",
            bg="white",
            font=("Arial", 11)
        ).pack(side="left")

        self.qty_var = tk.IntVar(value=1)

        tk.Spinbox(
            qty_frame,
            from_=1,
            to=20,
            width=5,
            textvariable=self.qty_var
        ).pack(side="left", padx=10)

        # Footer
        footer = tk.Frame(self, bg="white")
        footer.pack(fill="x", pady=10)

        tk.Button(
            footer,
            text="BACK",
            width=15,
            command=lambda: messagebox.showinfo(
                "Back",
                "Connect this to Page 4"
            )
        ).pack(side="left", padx=20)

        tk.Button(
            footer,
            text="NEXT",
            width=15,
            command=self.go_to_review
        ).pack(side="right", padx=20)

        self.load_category("Ulam")

    def load_category(self, category):

        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        row = 0
        col = 0

        for name, price in self.menu_data[category]:

            card = tk.Frame(
                self.menu_frame,
                width=150,
                height=130,
                relief="solid",
                bd=1
            )

            card.grid(row=row, column=col, padx=10, pady=10)

            card.pack_propagate(False)

            tk.Label(
                card,
                text=name,
                font=("Arial", 10, "bold")
            ).pack(pady=10)

            tk.Label(
                card,
                text=f"PHP {price}"
            ).pack()

            tk.Button(
                card,
                text="ADD",
                command=lambda n=name, p=price:
                self.add_to_cart(n, p)
            ).pack(pady=10)

            col += 1

            if col == 2:
                col = 0
                row += 1

    def add_to_cart(self, name, price):

        qty = self.qty_var.get()

        for item in self.controller.cart:

            if item["name"] == name:
                item["qty"] += qty
                item["subtotal"] = item["qty"] * price

                self.update_cart()
                self.qty_var.set(1)
                return

        self.controller.cart.append({
            "name": name,
            "price": price,
            "qty": qty,
            "subtotal": qty * price
        })

        self.update_cart()

        self.qty_var.set(1)

    def update_cart(self):

        self.cart_listbox.delete(0, tk.END)

        total = 0

        for item in self.controller.cart:

            self.cart_listbox.insert(
                tk.END,
                f"{item['name']} x{item['qty']} = PHP {item['subtotal']}"
            )

            total += item["subtotal"]

        self.controller.total_price = total

        self.total_label.config(
            text=f"Total: PHP {total:.2f}"
        )

    def remove_item(self):

        selected = self.cart_listbox.curselection()

        if not selected:
            return

        del self.controller.cart[selected[0]]

        self.update_cart()

    def clear_cart(self):

        self.controller.cart.clear()

        self.update_cart()

    def go_to_review(self):

        if len(self.controller.cart) == 0:

            messagebox.showwarning(
                "Empty Cart",
                "Please add an item first."
            )

            return

        self.controller.show_frame("Page6_Review")


# ==================================================
# PAGE 6
# ==================================================
class Page6_Review(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")

        self.controller = controller

        tk.Label(
            self,
            text="ORDER REVIEW",
            font=("Arial", 22, "bold"),
            bg="white"
        ).pack(pady=10)

        self.textbox = tk.Text(
            self,
            width=60,
            height=20,
            font=("Courier New", 11)
        )

        self.textbox.pack(pady=10)

        self.total_label = tk.Label(
            self,
            text="Total: PHP 0.00",
            font=("Arial", 14, "bold"),
            bg="white"
        )

        self.total_label.pack()

        footer = tk.Frame(self, bg="white")
        footer.pack(fill="x", pady=20)

        tk.Button(
            footer,
            text="GO BACK",
            width=15,
            command=lambda:
            controller.show_frame("Page5_Ordering")
        ).pack(side="left", padx=20)

        tk.Button(
            footer,
            text="CONTINUE",
            width=15,
            command=self.continue_payment
        ).pack(side="right", padx=20)

    def refresh_page(self):

        self.textbox.delete("1.0", tk.END)

        total = 0

        self.textbox.insert(
            tk.END,
            "ITEM\t\tQTY\tSUBTOTAL\n"
        )

        self.textbox.insert(
            tk.END,
            "-" * 40 + "\n"
        )

        for item in self.controller.cart:

            self.textbox.insert(
                tk.END,
                f"{item['name']:<20}"
                f"{item['qty']:<5}"
                f"{item['subtotal']:.2f}\n"
            )

            total += item["subtotal"]

        self.total_label.config(
            text=f"Total: PHP {total:.2f}"
        )

    def continue_payment(self):

        messagebox.showinfo(
            "Next Module",
            "Connect this to Page 7 (Payment Module)"
        )


# ==================================================
# RUN PROGRAM
# ==================================================
if __name__ == "__main__":

    app = OrderSequenceApp()
    app.mainloop()