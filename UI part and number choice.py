import tkinter as tk
from tkinter import ttk, messagebox

# List of parts
parts = ["D Shaft", "Worm Gear", "PWB Board", "Spring"]

# List of positions (1 through 6)
positions = list(range(1, 7))

# Initialize window
root = tk.Tk()
root.title("Part Selection")

# Label for instructions
label = tk.Label(root, text="Please select a part:")
label.pack(pady=10)

# Menu for parts selection
selected_part = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_part, values=parts, width=50)
dropdown.pack(pady=10)

# Display selected part
def display_selection():
    part = selected_part.get()
    if part:
        result_label.config(text="You selected: {part}")
    else:
        result_label.config(text="No part selected.")

# Function to confirm selection
def confirm_selection():
    part = selected_part.get()
    if not part:
        messagebox.showwarning("No Selection", "Please select a part before proceeding.")
    else:
        response = messagebox.askyesno("Confirm Selection", "Is '{part}' the correct part?")
        if response:
            result_label.config(text="You confirmed: {part}")
        else:
            result_label.config(text="Please select the correct part.")

# Label and entry for part number
label_part_number = tk.Label(root, text="Enter the part number:")
label_part_number.pack(pady=5)

part_number_entry = tk.Entry(root)
part_number_entry.pack(pady=5)

# Function to confirm selection and part number
def confirm_selection():
    part = selected_part.get()
    part_number = part_number_entry.get()
    
    if not part:
        messagebox.showwarning("No Part Selected", "Please select a part before proceeding.")
    elif not part_number:
        messagebox.showwarning("No Part Number", "Please enter the part number.")
    else:
        response = messagebox.askyesno("Confirm Selection", "Is '{part}' with part number '{part_number}' correct?")
        if response:
            result_label.config(text=f"Confirmed: {part} (Part Number: {part_number})")
        else:
            result_label.config(text="Please select the correct part and part number.")

# Button to confirm selection and part number
confirm_button = tk.Button(root, text="Confirm Part and Number", command=confirm_selection)
confirm_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()