import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def sort_files():
    # Get the selected directory
    source_dir = filedialog.askdirectory(title="Select directory to sort")

    if not source_dir:
        return

    # Define the destination directory
    destination_dir = os.path.join(source_dir, "FileTypes")

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of files in the selected directory
    files = os.listdir(source_dir)

    # Iterate over each file
    for file in files:
        file_path = os.path.join(source_dir, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(file)

        # Create the destination directory for the file type if it doesn't exist
        file_type_path = os.path.join(destination_dir, extension[1:])
        if not os.path.exists(file_type_path):
            os.makedirs(file_type_path)

        # Move the file to the destination directory
        destination_file_path = os.path.join(file_type_path, file)
        shutil.move(file_path, destination_file_path)

    messagebox.showinfo("Sorting Complete", "Files sorted successfully!")


# Create the main window
window = tk.Tk()
window.title("File Sorter")

# Create a button to trigger the file sorting
sort_button = tk.Button(window, text="Sort Files", command=sort_files)
sort_button.pack(pady=10)

# Run the GUI event loop
window.mainloop()