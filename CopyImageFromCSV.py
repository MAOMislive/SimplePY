import os
import shutil
import csv

# Define the paths
csv_file = r'C:\Users\csv_file.csv'  # Replace with the path to your CSV file
source_image_dir = r'C:\Users\src_folder' # Replace with the path to the directory containing the images'
destination_dir = r'C:\Users\des_folder'  # Replace with the path to the destination directory

# Create the destination directory if it does not exist
os.makedirs(destination_dir, exist_ok=True)

# Read the CSV file and get the image IDs
image_ids = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        image_ids.append(row['image_id'])

# Copy the images to the destination directory
for image_id in image_ids:
    image_filename = image_id + '.jpg'  # Assuming the images have .png extension
    source_image_path = os.path.join(source_image_dir, image_filename)
    destination_image_path = os.path.join(destination_dir, image_filename)

    # Check if the image file exists before copying
    if os.path.exists(source_image_path):
        shutil.copy(source_image_path, destination_image_path)
        print(f"Copied {image_filename} to {destination_dir}")
    else:
        print(f"Image {image_filename} not found in {source_image_dir}")

print("Image copying process completed.")
