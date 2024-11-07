import os
import shutil
import cv2
import imgaug.augmenters as iaa
import numpy as np

# Define the paths
source_image_dir = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\real train'
destination_dir = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\real train\augmentated_images'

# Create the destination directory if it does not exist
os.makedirs(destination_dir, exist_ok=True)

# Define the augmentation sequence
aug_seq = iaa.Sequential([
    iaa.Fliplr(0.5),  # Horizontal flips
    iaa.Affine(rotate=(-90, 90)),  # Rotate by -20 to +20 degrees
    iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255)),  # Add Gaussian noise
    iaa.Multiply((0.8, 1.2)),  # Change brightness
    iaa.LinearContrast((0.75, 1.5)),  # Change contrast
    iaa.GaussianBlur(sigma=(0.0, 3.0))  # Apply Gaussian blur
])

# Read the source images and apply augmentations
image_filenames = [f for f in os.listdir(source_image_dir) if f.endswith('.jpg')]

# Print number of images found
print(f"Found {len(image_filenames)} images in the source directory.")

# Number of augmentations to generate per image
augmentations_per_image = 5
augmented_image_count = 0

for image_filename in image_filenames:
    # Read the image
    image_path = os.path.join(source_image_dir, image_filename)
    image = cv2.imread(image_path)

    # Check if image was read correctly
    if image is None:
        print(f"Failed to read image: {image_filename}")
        continue

    # Apply augmentations
    for i in range(augmentations_per_image):
        augmented_image = aug_seq(image=image)

        # Save the augmented image
        augmented_filename = f"{os.path.splitext(image_filename)[0]}_aug_{i}.png"
        augmented_image_path = os.path.join(destination_dir, augmented_filename)
        cv2.imwrite(augmented_image_path, augmented_image)

        augmented_image_count += 1

    # Also copy the original image to the destination directory
    shutil.copy(image_path, os.path.join(destination_dir, image_filename))
    augmented_image_count += 1

print(f"Augmentation completed. Generated {augmented_image_count} images in total.")
