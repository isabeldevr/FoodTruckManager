import tkinter as tk
from classes import Order, Payment
from gui import root, label_orders

# Dummy data for demonstration
Order_list = [Order('John Doe'), Order('Jane Smith')]

def resgister_payment(payment):
    print("Payment registered")
    payment.payment_registered()
    label_orders.config(text="Pending Orders: " + str(len(Order_list)))

def show_order_list():
    print("\n ---------------------- \n Total Orders: ", len(Order_list))
    for order in Order_list:
        order.show_order()
        payment = Payment(order, "Credit Card")
        payment.pay()

def create_order():
    # new window for entering customer details
    order_window = tk.Toplevel(root)
    order_window.title("Enter Order Details")
    order_window.geometry("300x300")
    
    tk.Label(order_window, text="Enter Customer Name:").pack(pady=10)
    customer_name_entry = tk.Entry(order_window)
    customer_name_entry.pack(pady=10)

    # empty order
    order = Order("", [])

    def add_pizza_to_order():
        order.add_food(Pizza(10, ["cheese", "pepperoni"]))
        print("Pizza added to order")

    def add_burger_to_order():
        order.add_food(Burger(5, ["bun", "patty"]))
        print("Burger added to order")
    
    # button to add pizza
    pizza_button = tk.Button(order_window, text="Add Pizza", width=20, height=2, command=add_pizza_to_order)
    pizza_button.pack(pady=10)
    
    # button to add burger
    burger_button = tk.Button(order_window, text="Add Burger", width=20, height=2, command=add_burger_to_order)
    burger_button.pack(pady=10)

    def submit_order():
        name = customer_name_entry.get()
        order.ordername = name
        print(f"Order created for {order.ordername}")
        order.show_order()
        Order_list.append(order)
        label_orders.config(text="Pending Orders: " + str(len(Order_list)))
        order_window.destroy()
    
    submit_button = tk.Button(order_window, text="Submit", width=20, height=2, command=submit_order)
    submit_button.pack(pady=10)   

def customer_payment():
    payment_window = tk.Toplevel(root)
    payment_window.title("Payment")
    payment_window.geometry("300x300")

    tk.Label(payment_window, text="Enter Customer Name:").pack(pady=10)
    customer_name_entry = tk.Entry(payment_window)
    customer_name_entry.pack(pady=10)

    tk.Label(payment_window, text="Enter Payment Type:").pack(pady=10)
    payment_type_entry = tk.Entry(payment_window)
    payment_type_entry.pack(pady=10)

    def pay_order():
        name = customer_name_entry.get()
        payment_type = payment_type_entry.get()
        for order in Order_list:
            if order.ordername == name:
                payment = Payment(order, payment_type)
                payment.pay()
                payment_complete_button = tk.Button(payment_window, text="Payment Complete", width=20, height=2, command=lambda: resgister_payment(payment))
                payment_complete_button.pack(pady=10)
            else:
                print("ERROR: Order not found")
                import time
                time.sleep(2)
                payment_window.destroy()
    
    # submit payment after entering customer name and payment type with enter key
    payment_window.bind('<Return>', lambda event=None: pay_order())

def orders_page():
    orders_window = tk.Toplevel(root)
    orders_window.title("Orders")
    orders_window.geometry("300x300")
    
    # button show order list
    show_order_button = tk.Button(orders_window, text="Show Order List", width=20, height=2, command=show_order_list)
    show_order_button.pack(pady=10)

    # button to edit an order
    edit_order_button = tk.Button(orders_window, text="Edit Order", width=20, height=2, command=edit_orders)
    edit_order_button.pack(pady=10)

def edit_orders():
    if not Order_list:
        print("No orders to edit")
        return
    
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Order")
    edit_window.geometry("400x400")

    canvas = tk.Canvas(edit_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(edit_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    tk.Label(frame, text="Enter Customer Name:").pack(pady=10)
    customer_name_entry = tk.Entry(frame)
    customer_name_entry.pack(pady=10)

    # Function to search for an order
    def search_order():
        customer_name = customer_name_entry.get()
        for order in Order_list:
            if order.ordername == customer_name:

                def cancel_order():
                    order.cancel_order()
                    print("Order cancelled")
                    label_orders.config(text="Pending Orders: " + str(len(Order_list)))
                    frame.destroy()

                cancel_order_button = tk.Button(
                    frame,
                    text="Cancel Order",
                    width=20,
                    height=2,
                    command=cancel_order
                )
                cancel_order_button.pack(pady=10)
                
                for item in order.items:
                    def remove_item_button_func(order, item, button):
                        order.remove_food(item)
                        button.destroy()
                   
                    remove_item_button = tk.Button(
                        frame,
                        text=f"Remove {item.name}",
                        width=20,
                        height=2
                    )
                    remove_item_button.config(command=lambda o=order, i=item, b=remove_item_button: remove_item_button_func(o, i, b))
                    remove_item_button.pack(pady=10)
                    break
        else:
            print("Customer order not found")

    search_button = tk.Button(frame, text="Search", command=search_order)
    search_button.pack(pady=10)
