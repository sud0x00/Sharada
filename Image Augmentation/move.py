import os
import shutil
import random

# Get the list of files in the current directory
files = os.listdir()

# Iterate over each file
for file in files:
    # Check if it is a file (not a folder) and not the Python file
    if os.path.isfile(file) and file != os.path.basename(__file__):
        # Get the file name and extension
        file_name, file_ext = os.path.splitext(file)
        # Create the folder with the same name as the file (exclude extension) if it doesn't exist
        folder_name = file_name
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # Generate a random name for the file
        new_file_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)) + file_ext
        # Move the file to the folder with the random name
        shutil.move(file, os.path.join(folder_name, new_file_name))

# The script will finish with only the Python file remaining in the current directory
