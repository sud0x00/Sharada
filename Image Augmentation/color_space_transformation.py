import os
import cv2

# Define a dictionary to map color space names to their corresponding conversion code in OpenCV
""" COLOR_SPACES = {"RGB": cv2.COLOR_BGR2RGB,
                "Grayscale": cv2.COLOR_BGR2GRAY,
                "CMYK": cv2.COLOR_BGR2CMYK,
                "HCV": cv2.COLOR_BGR2HSV,
                "LAB": cv2.COLOR_BGR2LAB,
                "YUV": cv2.COLOR_BGR2YUV,
                "XYZ": cv2.COLOR_BGR2XYZ} """

COLOR_SPACES = {"HCV": cv2.COLOR_BGR2HSV,
                "LAB": cv2.COLOR_BGR2LAB,
                "YUV": cv2.COLOR_BGR2YUV}

# Define the path to the directory containing subfolders with images
dir_path = "."

# Loop over each subfolder in the directory
for subfolder in os.listdir(dir_path):
    subfolder_path = os.path.join(dir_path, subfolder)
    if os.path.isdir(subfolder_path):
        # Loop over each image file in the subfolder
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)
            if os.path.isfile(file_path):
                # Loop over each color space
                for color_space in COLOR_SPACES:
                    # Define the output folder for the transformed images
                    output_folder = os.path.join(subfolder_path, color_space)
                    if not os.path.exists(output_folder):
                        os.makedirs(output_folder)
                    # Load the image and perform the color space transformation
                    image = cv2.imread(file_path)
                    transformed_image = cv2.cvtColor(image, COLOR_SPACES[color_space])
                    # Save the transformed image
                    output_path = os.path.join(output_folder, filename)
                    cv2.imwrite(output_path, transformed_image)
