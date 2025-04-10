import tkinter as tk
from tkinter import messagebox
from UI_Part_info1 import confirm_selection
from camera_module import turn_on_camera, capture_images, save_video
from arduino_arm_control import move_to_shelf, move_to_camera, move_to_microscope, place_back_on_shelf
from gui_confirm_part import confirm_part_visibility
from defect_detection import analyze_defects
from report_generator import generate_pdf_report
from gui_restart import restart_prompt

def main():
    while True:
        # Step 1: Select part, number and position using GUI
        part, number, location = select_part_and_quantity()
        print("Selected Part: {part}, Quantity: {quantity}")

        # Step 2: Turn on the camera
        camera = turn_on_camera()
        print("Camera module initialized.")

        for i in range(quantity):
            print("Processing part {i+1} of {quantity}...")
            
            # Step 3: Move arm to fetch the part from the shelf
            move_to_shelf(part)
            move_to_camera()
            
            # Step 4: Confirm part visibility via GUI
            is_visible = confirm_part_visibility(camera)
            if not is_visible:
                print("Part not detected on camera. Restarting process...")
                move_to_shelf(part, return_to_shelf=True)
                continue

            # Step 5: Capture images and save video
            images = capture_images(camera)
            video_path = save_video(camera)

            # Step 6: Analyze defects
            defect_results = analyze_defects(images)
            print(f"Defect analysis complete: {defect_results}")

            # Step 7: Generate a PDF report
            report_path = generate_pdf_report(part, images, defect_results, video_path)
            print(f"Report generated: {report_path}")

            # Step 8: Ask user for manual inspection
            manual_inspection = input("Do you want to perform a manual inspection? (yes/no): ").strip().lower()
            if manual_inspection == 'yes':
                move_to_microscope()
                print("Manual inspection mode active. Please check the microscope view.")
                input("Press Enter to continue after inspection.")
                break  # Exit loop after manual inspection is completed
            elif manual_inspection == 'no':
                print("Skipping manual inspection.")
                break  # Exit loop if user doesn't want manual inspection

            # Step 9: Place the part in good or bad collection
            # place_back_on_shelf(part)

            # Step 10: Restart?
           # def main():
                #while True:
       
            # GUI-based restart prompt
                    #if not restart_prompt():
                        #break

    print("Inspection complete. Exiting program.")
        
        

   # print("Inspection complete. Exiting program.")

if __name__ == "__main__":
    main()
