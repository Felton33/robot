# Robotic Inspection Workflow Interface

A Python-based GUI system for automating part inspection using a robotic arm and camera. This tool streamlines part selection, imaging, defect analysis, and final classification using a multi-step workflow.

---

## Key Features

- Guided workflow with GUI prompts at each step
- Camera-based image capture and video recording
- Automated defect analysis
- Optional manual inspection prompt
- Final classification into: ✅ Pass, ❌ Fail, ❓ Further Inspection

---

## Project Structure

```plaintext
├── main_workflow1.py           # Main inspection workflow logic and GUI
├── UI_Part_info1.py            # Part selection GUI and metadata
├── camera_module.py            # Camera initialization, image capture, video saving
├── arduino_arm_control.py      # Robotic arm movement commands
├── gui_confirm_part.py         # GUI to confirm part visibility in camera
├── defect_detection.py         # Defect analysis logic using images
├── report_generator.py         # (optional, currently not active)
├── gui_restart.py              # (optional, currently not active)
└── README.md                   # You're reading it!
