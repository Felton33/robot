# main_workflow1
import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import messagebox
from UI_Part_info1 import confirm_selection_via_gui
from camera_module import turn_on_camera, capture_images, save_video
from arduino_arm_control import move_to_shelf, move_to_camera
from gui_confirm_part import confirm_part_visibility
from defect_detection import analyze_defects
# from report_generator import generate_pdf_report
# from gui_restart import restart_prompt

class InspectionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inspection Log")
        self.log_text = tk.Text(self.root, height=20, width=60, state='disabled')
        self.log_text.pack(padx=10, pady=10)
        self.root.after(100, self.run_main_workflow)
        self.root.mainloop()

    def log(self, msg):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
        self.root.update()
    
    def custom_classification_dialog(self):
        decision = {}

        dialog = tk.Toplevel(self.root)
        dialog.title("Final Classification")
        dialog.grab_set()
        dialog.geometry("350x180")
        dialog.resizable(False, False)

        tk.Label(dialog, text="Final decision for this part:", font=("Helvetica", 12, "bold")).pack(pady=15)

        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=10)

        def choose(value):
            decision["result"] = value
            dialog.destroy()

        tk.Button(button_frame, text="✅ PASS", width=12, command=lambda: choose("pass")).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="❌ FAIL", width=12, command=lambda: choose("fail")).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="❓ FURTHER", width=18, command=lambda: choose("further")).grid(row=1, column=0, columnspan=2, pady=10)

        dialog.wait_window()
        return decision.get("result", None)

    # Modular Workflow Steps

    def get_user_selection(self):
        from UI_Part_info1 import confirm_selection_via_gui
        return confirm_selection_via_gui(self.root)

    def confirm_part_pickup(self):
        return messagebox.askyesno("Pickup Confirmation", "Was the part successfully picked up?", parent=self.root)

    def prompt_move_to_camera(self):
        return messagebox.askyesno("Move to Camera", "Has the arm been moved to the camera position?", parent=self.root)

    def check_camera_visibility(self, camera):
        from gui_confirm_part import confirm_part_visibility
        return confirm_part_visibility(camera)

    def capture_images_and_video(self, camera):
        from camera_module import capture_images, save_video
        if messagebox.askyesno("Begin Imaging", "Start capturing inspection photos and video?", parent=self.root):
            images = capture_images(camera)
            video = save_video(camera)
            return images, video
        else:
            return None, None

    def analyze_part_defects(self, images):
        from defect_detection import analyze_defects
        self.log("🧠 Analyzing defects...")
        return analyze_defects(images)

    def prompt_manual_inspection(self):
        if messagebox.askyesno("Manual Inspection", "Do you want to inspect manually under the microscope?", parent=self.root):
            pos = tk.simpledialog.askinteger("Microscope Position", "Enter microscope position (1–6):", parent=self.root)
            if pos:
                self.log(f"🔬 Moving to microscope position {pos}")
                # move_to_microscope(pos)
                messagebox.showinfo("Microscope", "Inspect the part, then click OK to continue.", parent=self.root)
            else:
                self.log("⚠️ No manual inspection position provided.")
        else:
            self.log("Skipping manual inspection.")

    def classify_final_decision(self):
        result = messagebox.askquestion(
            "Final Classification",
            "Does the part pass inspection?\n\nYes = PASS\nNo = FAIL\nCancel = Further Inspection Needed",
            parent=self.root
        )
        if result == "yes":
            self.log("✅ Part PASSED.")
            # move_to_pass_bin()
        elif result == "no":
            self.log("❌ Part FAILED.")
            # move_to_fail_bin()
        else:
            self.log("❓ Part marked for FURTHER INSPECTION.")
            # move_to_further_review_bin()

    # Main Workflow Runner

    def run_main_workflow(self):
        while True:
            selection = self.get_user_selection()
            if not selection:
                self.log("❌ Selection cancelled.")
                break

            part = selection["part"]
            part_number = selection["part_number"]
            position = selection["position"]
            quantity = 1

            self.log(f"🧩 Selected Part: {part}")
            self.log(f"🔢 Part Number: {part_number}")
            self.log(f"📍 Shelf Position: {position}")

            from camera_module import turn_on_camera
            from arduino_arm_control import move_to_shelf, move_to_camera

            camera = turn_on_camera()
            self.log("📷 Camera module initialized.")

            for i in range(quantity):
                self.log(f"🔁 Processing part {i+1} of {quantity}...")
                move_to_shelf(part)
                self.log("🤖 Moving arm to part...")

                if not self.confirm_part_pickup():
                    self.log("⚠️ Pickup failed.")
                    break

                if not self.prompt_move_to_camera():
                    self.log("🚫 Skipped camera step.")
                    break

                move_to_camera()
                self.log("📍 Moved to camera.")

                if not self.check_camera_visibility(camera):
                    self.log("❌ Part not visible.")
                    break

                images, video_path = self.capture_images_and_video(camera)
                if not images:
                    self.log("🚫 Imaging canceled.")
                    break

                defects = self.analyze_part_defects(images)
                # Log system recommendation
                if defects == "maybe":
                    self.log("🔶 POSSIBLE DEFECT detected.")
                elif defects == "fail":
                    self.log("❌ DEFECT detected.")
                else:
                    self.log("✅ No defects detected.")

                # Step: Always offer manual inspection
                self.prompt_manual_inspection()

                # Step: Ask for final classification
                final_choice = self.custom_classification_dialog()

                if final_choice == "pass":
                    self.log("✅ Final decision: PASS. Moving to pass receptacle.")
                    # move_to_pass_bin()
                elif final_choice == "fail":
                    self.log("❌ Final decision: FAIL. Moving to fail receptacle.")
                    # move_to_fail_bin()
                elif final_choice == "further":
                    self.log("❓ Final decision: FURTHER INSPECTION needed.")
                    # move_to_further_review_bin()
                else:
                    self.log("⚠️ No final decision made.")

                break  # End loop after one part

            self.log("✅ Inspection complete.")
            break

if __name__ == "__main__":
    InspectionApp()