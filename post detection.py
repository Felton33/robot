import tkinter as tk
from tkinter import messagebox, ttk

def move_to_microscope():
    # Code to command the arm to move to the microscope
    messagebox.showinfo("Action", "The arm is moving to the microscope for manual inspection.")
    print("Command: Arm moving to microscope.")

def select_position():
    selected_position = position_var.get()
    if selected_position:
        # Code to command the arm to move to the selected defect position
        messagebox.showinfo("Action", f"The arm is moving to position: {selected_position}.")
        print(f"Command: Arm moving to position {selected_position}.")
    else:
        messagebox.showwarning("Warning", "Please select a position before proceeding.")

def arm_decision():
    response = messagebox.askyesno("Decision", "Defect analysis complete. Move part to the microscope for manual inspection?")
    if response:
        move_to_microscope()
    else:
        if defect_positions:
            position_selection_window()

def position_selection_window():
    pos_window = tk.Toplevel(root)
    pos_window.title("Select Defect Position")
    pos_window.geometry("300x200")

    tk.Label(pos_window, text="Select defect position:").pack(pady=10)

    for pos in defect_positions:
        ttk.Radiobutton(pos_window, text=pos, variable=position_var, value=pos).pack(anchor="w")

    ttk.Button(pos_window, text="Move to Position", command=select_position).pack(pady=10)

# Example defect positions (can be dynamically set based on analysis)
defect_positions = ["Position 1", "Position 2", "Position 3", "Position 4", "Position 5"]

# Initialize the main GUI window
root = tk.Tk()
root.title("Defect Analysis Result")
root.geometry("400x200")

position_var = tk.StringVar()

# Main GUI Layout
ttk.Label(root, text="Defect Analysis Report Compiled").pack(pady=20)
ttk.Button(root, text="Decide Next Action", command=arm_decision).pack(pady=10)

# Run the GUI
root.mainloop()
