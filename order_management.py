

import tkinter as tk

class OrderManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KEYOSK - Order Management")
        self.root.geometry("450x720")
        self.root.resizable(False, False)

        self.orders = {
            39: {
                "status": "Unpaid",
                "items": [
                    ("Main", "Burger", 1, 120.00),
                    ("Side", "Fries", 1, 55.00),
                    ("Dessert", "Cake", 1, 75.00),
                    ("Drinks", "Iced Tea", 2, 35.00),
                ]
            },
            25: {"status": "In Progress", "items": []},
            36: {"status": "In Progress", "items": []},
            15: {"status": "In Progress", "items": []},
            11: {"status": "In Progress", "items": []},
            50: {"status": "Done", "items": []},
        }

        self.current_frame = None
        self.show_page_10()

    def clear(self):
        if self.current_frame:
            self.current_frame.destroy()

    def picture_slot(self, parent):
        slot = tk.Frame(parent, width=55, height=55, bg="white", bd=1, relief="solid")
        slot.pack_propagate(False)
        tk.Label(slot, text="IMG", font=("Arial", 10)).pack(expand=True)
        return slot

    def show_page_10(self):
        self.clear()
        self.current_frame = tk.Frame(self.root, bg="white")
        self.current_frame.pack(fill="both", expand=True)

        top = tk.Frame(self.current_frame, bg="light yellow", bd=2, relief="solid")
        top.pack(fill="x")
        tk.Label(top, text="KEYOSK", font=("Arial", 20, "bold"), bg="light yellow").pack(pady=5)
        tk.Label(top, text="CURRENT ORDERS", font=("Arial", 22), bg="light yellow").pack()

        body = tk.Frame(self.current_frame, bg="beige")
        body.pack(fill="both", expand=True)

        left = tk.Frame(body, bg="white", bd=2, relief="solid")
        left.place(x=0, y=0, relwidth=0.5, relheight=0.82)

        right = tk.Frame(body, bg="white", bd=2, relief="solid")
        right.place(relx=0.5, y=0, relwidth=0.5, relheight=0.82)

        tk.Label(left, text="In-Progress", font=("Arial", 16), bg="white").pack(pady=10)
        tk.Label(right, text="Done", font=("Arial", 16), bg="white").pack(pady=10)

        self.create_order_buttons(left, [39, 25, 36, 15, 11])
        self.create_order_buttons(right, [50])

        bottom = tk.Frame(self.current_frame, bg="light yellow", bd=2, relief="solid")
        bottom.pack(side="bottom", fill="x")

        tk.Button(
            bottom, text="GO BACK", font=("Arial", 14, "bold"),
            command=self.root.quit, width=15
        ).pack(pady=10)

    def create_order_buttons(self, parent, order_list):
        container = tk.Frame(parent, bg="white")
        container.pack(pady=8)

        row = 0
        col = 0
        for order_no in order_list:
            tk.Button(
                container,
                text=str(order_no),
                font=("Arial", 16, "bold"),
                width=6,
                height=2,
                command=lambda n=order_no: self.show_page_11(n)
            ).grid(row=row, column=col, padx=8, pady=8)

            col += 1
            if col > 1:
                col = 0
                row += 1

    def show_page_11(self, order_no):
        self.clear()
        self.current_frame = tk.Frame(self.root, bg="red")
        self.current_frame.pack(fill="both", expand=True)

        top = tk.Frame(self.current_frame, bg="light yellow", bd=2, relief="solid")
        top.pack(fill="x")
        tk.Label(top, text="KEYOSK", font=("Arial", 20, "bold"), bg="light yellow").pack(pady=5)

        order = self.orders.get(order_no, {"status": "Unpaid", "items": []})

        tk.Label(
            self.current_frame,
            text=f"Order No. {order_no}",
            font=("Arial", 22),
            bg="red"
        ).pack(anchor="w", padx=18, pady=12)

        table = tk.Frame(self.current_frame, bg="light yellow")
        table.pack(fill="both", expand=True, padx=18)

        headers = ["Item", "Qty", "PHP"]
        widths = [28, 8, 10]

        for i, h in enumerate(headers):
            tk.Label(
                table,
                text=h,
                font=("Arial", 13, "bold"),
                bg="light green",
                bd=1,
                relief="solid",
                width=widths[i]
            ).grid(row=0, column=i, padx=2, pady=2)

        total = 0
        items = order["items"] or [
            ("Main", "Burger", 1, 120.00),
            ("Side", "Fries", 1, 55.00),
            ("Dessert", "Cake", 1, 75.00),
            ("Drinks", "Iced Tea", 2, 35.00),
        ]

        for idx, (cat, name, qty, price) in enumerate(items, start=1):
            subtotal = qty * price
            total += subtotal

            item_frame = tk.Frame(table, bg="white", bd=1, relief="solid")
            item_frame.grid(row=idx, column=0, padx=2, pady=2, sticky="nsew")

            img_box = self.picture_slot(item_frame)
            img_box.pack(side="left", padx=5, pady=5)

            text_frame = tk.Frame(item_frame, bg="white")
            text_frame.pack(side="left", fill="both", expand=True, padx=5)

            tk.Label(
                text_frame,
                text=f"{cat} - {name}",
                font=("Arial", 11),
                bg="white",
                anchor="w"
            ).pack(anchor="w")

            tk.Label(
                text_frame,
                text="Item description here",
                font=("Arial", 9),
                bg="white",
                fg="gray",
                anchor="w"
            ).pack(anchor="w")

            tk.Label(
                table,
                text=str(qty),
                font=("Arial", 11),
                bg="white",
                bd=1,
                relief="solid",
                width=8
            ).grid(row=idx, column=1, padx=2, pady=2)

            tk.Label(
                table,
                text=f"₱{subtotal:.2f}",
                font=("Arial", 11),
                bg="white",
                bd=1,
                relief="solid",
                width=10
            ).grid(row=idx, column=2, padx=2, pady=2)

        bottom = tk.Frame(self.current_frame, bg="light yellow", bd=2, relief="solid")
        bottom.pack(side="bottom", fill="x")

        tk.Label(
            bottom,
            text=f"Status: {order['status']}",
            font=("Arial", 13),
            bg="light yellow"
        ).pack(side="left", padx=14, pady=10)

        tk.Label(
            bottom,
            text=f"Total: ₱{total:.2f}",
            font=("Arial", 13),
            bg="light yellow"
        ).pack(side="right", padx=14, pady=10)

        tk.Button(
            self.current_frame,
            text="GO BACK",
            font=("Arial", 14, "bold"),
            width=15,
            command=self.show_page_10
        ).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderManagementApp(root)
    root.mainloop()

