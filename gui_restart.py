import tkinter as tk
from tkinter import messagebox

def restart_prompt():

    #Displays a GUI dialog asking the user if they want to restart the workflow.
    #Returns True if the user wants to restart, False otherwise.
    
    def on_restart():
        nonlocal restart
        restart = True
        root.destroy()

    def on_exit():
        nonlocal restart
        restart = False
        root.destroy()

    root = tk.Tk()
    root.title("Restart Workflow")
    root.geometry("300x150")

    tk.Label(root, text="Do you want to restart the process?", font=("Arial", 12)).pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack()

    restart = False

    tk.Button(button_frame, text="Restart", command=on_restart, width=10).pack(side="left", padx=10)
    tk.Button(button_frame, text="Exit", command=on_exit, width=10).pack(side="right", padx=10)

    root.mainloop()

    return restart
