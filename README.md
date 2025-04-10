# Robot Inspection Workflow UI

A Python-based graphical user interface (GUI) for automating part inspection using a robotic arm. Built with Tkinter, this tool guides the user through a multi-step process for visual inspection, classification, and routing of mechanical components.

---

## Features

- User-friendly interface for part inspection
- Step-by-step workflow with confirmation prompts
- Visual inspection with defect detection (optional)
- Final classification into **Pass**, **Fail**, or **Further Inspection**
- Modular code structure for easy extension

---

## Project Structure

```plaintext
├── main_workflow1.py         # Main GUI logic and workflow controller
├── canvas_module.py         # Custom canvas drawing for part visualization
├── Upart_info.py            # Part information and logic
├── detect_module.py         # (Optional) Vision/defect detection logic
└── README.md                # You're reading this!
