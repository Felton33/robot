import tkinter as tk
from tkinter import ttk, messagebox

# List of parts
parts = ["D Shaft", "Worm Gear", "PWB Board", "Spring"]

# List of positions (1 through 6)
positions = list(range(1, 7))

# Dictionary to store selections
selection_data = {
    "part": None,
    "part_number": None,
    "position": None
}

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

# Label and entry for part number
label_part_number = tk.Label(root, text="Enter the part number:")
label_part_number.pack(pady=5)

part_number_entry = tk.Entry(root)
part_number_entry.pack(pady=5)

# Label for position selection
label_position = tk.Label(root, text="Select a position (1-6):")
label_position.pack(pady=5)

selected_position = tk.StringVar()
position_dropdown = ttk.Combobox(root, textvariable=selected_position, values=positions, width=50)
position_dropdown.pack(pady=10)

# Display result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Function to confirm selection
def confirm_selection():
    part = selected_part.get()
    part_number = part_number_entry.get()
    position = selected_position.get()
    
    if not part:
        messagebox.showwarning("No Part Selected", "Please select a part before proceeding.")
    elif not part_number:
        messagebox.showwarning("No Part Number", "Please enter the part number.")
    elif not position:
        messagebox.showwarning("No Position", "Please select a position.")
    else:
        confirmation_text = (
            f"Part: {part}\n"
            f"Part Number: {part_number}\n"
            f"Position: {position}\n\n"
            "Is this correct?"
        )
        response = messagebox.askyesno("Confirm Selection", confirmation_text)
        if response:
            # Save data to selection_data
            selection_data["part"] = part
            selection_data["part_number"] = part_number
            selection_data["position"] = int(position)

            # Update result label
            result_label.config(
                text=f"Confirmed:\nPart: {part}\nPart Number: {part_number}\nPosition: {position}"
            )

            # Call the main workflow
            main_workflow()
        else:
            result_label.config(text="Please select the correct part, part number, and position.")

# Simulated main workflow function
def main_workflow():
    # Access data from selection_data
    part = selection_data["part"]
    part_number = selection_data["part_number"]
    position = selection_data["position"]
    print(f"Moving robotic arm to pick: {part} (Part Number: {part_number}, Position: {position})")
    # Add your robotic arm control logic here

# Button to confirm selection
confirm_button = tk.Button(root, text="Confirm Selection", command=confirm_selection)
confirm_button.pack(pady=10)

root.mainloop() 