import os
import shutil

# Define the source and destination directories
desktop_path = os.path.expanduser("~/Documents")
destination_path = os.path.expanduser("~/Documents/Sorted Documents")

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Get a list of files on the desktop
files = os.listdir(desktop_path)

# Iterate over each file
for file in files:
    if file == "Sorted Documents":  # Skip the destination directory
        continue

    file_path = os.path.join(desktop_path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    _, extension = os.path.splitext(file)

    # Create the destination directory for the file type if it doesn't exist
    file_type_path = os.path.join(destination_path, extension[1:])
    if not os.path.exists(file_type_path):
        os.makedirs(file_type_path)

    # Move the file to the destination directory
    destination_file_path = os.path.join(file_type_path, file)
    shutil.move(file_path, destination_file_path)

print("Documents sorted successfully!")
