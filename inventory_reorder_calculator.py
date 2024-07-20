import tkinter as tk

# Function to calculate the reorder quantity and months of stock
def calculate_reorder_quantity(event=None):
    # Monthly sales data
    sales_input = sales_entry.get()
    monthly_sales = [int(sale.strip()) for sale in sales_input.split(",")]

    # Current stock quantity
    current_stock = int(stock_entry.get())

    # Orders in progress
    orders_in_progress = int(orders_entry.get())

    # Lead time for new orders to arrive (in months)
    lead_time = float(lead_time_entry.get())

    # Target stock quantity
    target_stock = int(target_stock_entry.get())

    # Calculate the total sales and average sales
    total_sales = sum(monthly_sales)
    average_sales = total_sales / len(monthly_sales)

    # Calculate the average monthly demand
    average_demand = total_sales / len(monthly_sales)

    # Calculate the total demand during lead time
    total_demand = average_demand * lead_time

    # Calculate the total inventory (current stock + orders in progress)
    total_inventory = current_stock + orders_in_progress

    # Calculate the reorder quantity considering the target stock
    reorder_quantity = max(target_stock - total_inventory + total_demand, 0)  # Ensure the reorder quantity is non-negative

    # Calculate the number of months of stock represented by the reorder quantity
    months_of_stock = reorder_quantity / average_demand if average_demand != 0 else 0

    total_sales_label.config(text="Total Sales: {}".format(total_sales))
    average_sales_label.config(text="Average Sales: {:.1f}".format(average_sales))
    result_label.config(text="Reorder Quantity: {:.1f}".format(reorder_quantity))
    months_of_stock_label.config(text="({:.1f} months stock)".format(months_of_stock))

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

# Create GUI window
window = tk.Tk()
window.title("Purchase Quantity Calculator")

# Labels
sales_label = tk.Label(window, text="Monthly Sales (separated by comma):")
sales_label.grid(row=0, column=0, padx=10, pady=5)

stock_label = tk.Label(window, text="Current Stock:")
stock_label.grid(row=1, column=0, padx=10, pady=5)

orders_label = tk.Label(window, text="Orders in Progress:")
orders_label.grid(row=2, column=0, padx=10, pady=5)

lead_time_label = tk.Label(window, text="Lead Time (in months):")
lead_time_label.grid(row=3, column=0, padx=10, pady=5)

target_stock_label = tk.Label(window, text="Target Stock Quantity:")
target_stock_label.grid(row=4, column=0, padx=10, pady=5)

total_sales_label = tk.Label(window, text="")
total_sales_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

average_sales_label = tk.Label(window, text="")
average_sales_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

months_of_stock_label = tk.Label(window, text="", font=("Arial", 10, "italic"), fg="gray")
months_of_stock_label.grid(row=9, column=1, padx=(0, 10), pady=5, sticky="e")

# Entry fields
sales_entry = tk.Entry(window, width=50)  # Adjust width here
sales_entry.grid(row=0, column=1, padx=5, pady=5)
sales_entry.bind("<Return>", focus_next_widget)

stock_entry = tk.Entry(window)
stock_entry.grid(row=1, column=1, padx=5, pady=5)
stock_entry.bind("<Return>", focus_next_widget)

orders_entry = tk.Entry(window)
orders_entry.grid(row=2, column=1, padx=5, pady=5)
orders_entry.bind("<Return>", focus_next_widget)

lead_time_entry = tk.Entry(window)
lead_time_entry.grid(row=3, column=1, padx=5, pady=5)
lead_time_entry.bind("<Return>", focus_next_widget)

target_stock_entry = tk.Entry(window)
target_stock_entry.grid(row=4, column=1, padx=5, pady=5)
target_stock_entry.bind("<Return>", focus_next_widget)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_reorder_quantity)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
calculate_button.bind("<Return>", calculate_reorder_quantity)

# Create a frame for the information labels
info_frame = tk.Frame(window)
info_frame.grid(row=13, column=0, columnspan=2, padx=10, pady=20)  # Added extra padding to place it lower

# Information labels
info_label_1 = tk.Label(info_frame, text="Lead Time: Number of months between now and delivery of Reorder Quantity", font=("Arial", 8), fg="gray")
info_label_1.pack(anchor="w")

info_label_2 = tk.Label(info_frame, text="Reorder Quantity = Average Sales x Lead Time + Target Stock Quantity - Current Stock - Orders in Progress", font=("Arial", 8), fg="gray")
info_label_2.pack(anchor="w")

info_label_3 = tk.Label(info_frame, text="Months of Stock: How long the Reorder Quantity will last based on average monthly sales", font=("Arial", 8), fg="gray")
info_label_3.pack(anchor="w")

# Run the GUI
window.mainloop()
