# UI_Part_info1.py
import tkinter as tk
from tkinter import ttk, messagebox

def confirm_selection_via_gui(parent=None):
    parts = ["D Shaft", "Worm Gear", "PWB Board", "Spring"]
    positions = list(range(1, 7))
    result = {}

    if parent:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Select Part for Inspection")
    window.configure(bg="#f0f0f5")  # Light gray-blue background
    window.geometry("400x300")

    selected_part = tk.StringVar()
    selected_position = tk.StringVar()

    # --- Title ---
    tk.Label(window, text="Robotic Inspection Setup", font=("Helvetica", 16, "bold"), bg="#f0f0f5").pack(pady=(10, 5))

    form_frame = tk.Frame(window, bg="#f0f0f5")
    form_frame.pack(pady=10)

    # --- Part Dropdown ---
    tk.Label(form_frame, text="Select Part:", font=("Helvetica", 12), bg="#f0f0f5").grid(row=0, column=0, sticky="w", pady=5)
    part_dropdown = ttk.Combobox(form_frame, textvariable=selected_part, values=parts, width=30, state="readonly")
    part_dropdown.grid(row=0, column=1, pady=5)
    part_dropdown.set(parts[0])

    # --- Part Number Entry ---
    tk.Label(form_frame, text="Part Number:", font=("Helvetica", 12), bg="#f0f0f5").grid(row=1, column=0, sticky="w", pady=5)
    part_number_entry = ttk.Entry(form_frame, width=32)
    part_number_entry.grid(row=1, column=1, pady=5)

    # --- Position Dropdown ---
    tk.Label(form_frame, text="Shelf Position (1–6):", font=("Helvetica", 12), bg="#f0f0f5").grid(row=2, column=0, sticky="w", pady=5)
    position_dropdown = ttk.Combobox(form_frame, textvariable=selected_position, values=positions, width=30, state="readonly")
    position_dropdown.grid(row=2, column=1, pady=5)
    position_dropdown.set(str(positions[0]))

    # --- Confirm Button ---
    def confirm_selection():
        part = selected_part.get().strip()
        part_number = part_number_entry.get().strip()
        position = selected_position.get().strip()

        if not part or not part_number or not position:
            messagebox.showwarning("Incomplete", "Please fill out all fields.", parent=window)
            return

        summary = f"Part: {part}\nPart Number: {part_number}\nPosition: {position}\n\nIs this correct?"
        if messagebox.askyesno("Confirm Selection", summary, parent=window):
            result["part"] = part
            result["part_number"] = part_number
            result["position"] = int(position)
            window.destroy()

    ttk.Button(window, text="Confirm Selection", command=confirm_selection).pack(pady=15)

    if not parent:
        window.mainloop()

    window.wait_window()
    return result