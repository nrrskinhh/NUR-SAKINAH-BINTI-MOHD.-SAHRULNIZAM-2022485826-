import tkinter as tk
from tkinter import ttk

# Define the prices globally
prices = {
    "Personal": 50,
    "Corporate": 300,
}

# Function to handle the calculation and database saving
def collect_data():
    full_name = full_name_entry.get()
    email_value = email_entry.get()
    phone_number_value = int(phone_number_entry.get())
    registration_fee_value = registration_fee_combobox.get()
    participants_value = int(participants_entry.get())
    
    # Check if the selected item exists in the dictionary
    if registration_fee_value in prices:
        total_price = prices[registration_fee_value] * participants_value
        output_label.config(text=f"Total Price: RM{total_price}")
    else:
        output_label.config(text="Invalid registration fee selection")

# Tkinter GUI
root = tk.Tk()
root.title("ONLINE CONFERENCE REGISTRATION")
root.geometry("600x400")  # Adjusted the size

# Page Title
label = tk.Label(root, text='ONLINE CONFERENCE REGISTRATION', font=("Times New Roman", 14, "bold"))
label.pack(ipadx=10, ipady=10)

# Full Name
full_name_label = tk.Label(root, text="FULL NAME:", font=(15))
full_name_label.pack()
full_name_entry = tk.Entry(root)
full_name_entry.pack()

# Email
email_label = tk.Label(root, text="EMAIL:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Phone Number
phone_number_label = tk.Label(root, text="PHONE NUMBER:")
phone_number_label.pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()

# Registration info
registration_fee_label = tk.Label(root, text="REGISTRATION FEE:")
registration_fee_label.pack()
registration_fee_combobox = ttk.Combobox(root, values=list(prices.keys()))
registration_fee_combobox.pack()

# Participants
participants_label = tk.Label(root, text="PARTICIPANTS:")
participants_label.pack()
participants_entry = tk.Entry(root)
participants_entry.pack()

# Output label
output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack()

# Buttons to perform operations
insert_button = tk.Button(root, text="Insert Data", command=collect_data)
insert_button.pack()

root.mainloop()

