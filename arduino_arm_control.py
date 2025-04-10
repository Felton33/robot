def move_to_shelf(part, return_to_shelf=False):
    if return_to_shelf:
        print(f"Returning {part} to the shelf.")
    else:
        print(f"Fetching {part} from the shelf.")

def move_to_camera():
    print("Moving part under the camera.")

def move_to_microscope():
    print("Moving part under the microscope.")

def place_back_on_shelf(part):
    print(f"Placing {part} back on the shelf.")
