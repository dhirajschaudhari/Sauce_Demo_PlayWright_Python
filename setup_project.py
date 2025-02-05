import os

# Define the required folder structure
folders = [
    "configs",
    "logs",
    "screenshots",
    "tests",
    "tests/pages",
    "tests/features",
    "tests/step_definitions",
    "tests/data",
    "reports"
]

def create_folders():
    """Creates the necessary folders for the automation framework."""
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("Folder structure created successfully!")

if __name__ == "__main__":
    create_folders()
