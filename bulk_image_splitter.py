import os
import shutil


def select_25_images(src_folder, dest_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # List all files in the source folder
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    # Select the first 25 images
    selected_files = files[:25]

    # Copy the selected images to the destination folder
    for file in selected_files:
        shutil.copy(os.path.join(src_folder, file), os.path.join(dest_folder, file))

    print(f"Copied {len(selected_files)} images to {dest_folder}")


def create_folders_of_25_images(src_folder, base_dest_folder):
    # List all files in the source folder
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    # Calculate the number of folders needed
    total_files = len(files)
    num_folders = (total_files + 24) // 25

    for i in range(num_folders):
        # Create a new folder for this batch of 25 images
        dest_folder = os.path.join(base_dest_folder, f"folder_{i + 1}")
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Get the files for this folder
        start_idx = i * 25
        end_idx = start_idx + 25
        batch_files = files[start_idx:end_idx]

        # Copy the files to the new folder
        for file in batch_files:
            shutil.copy(os.path.join(src_folder, file), os.path.join(dest_folder, file))

        print(f"Copied {len(batch_files)} images to {dest_folder}")


# Example usage
src_folder = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\real train\augmentated_images'
dest_folder_25 = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\real train\augmentated_images\folder_25'
base_dest_folder = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\real train\augmentated_images\folders'

# Select 25 images
select_25_images(src_folder, dest_folder_25)

# Create folders of 25 images each
create_folders_of_25_images(src_folder, base_dest_folder)
