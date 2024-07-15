import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the CSV file
csv_file_path = r"C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\_annotations.csv"
annotations = pd.read_csv(csv_file_path)


# Function to parse points from string to a list of tuples
def parse_points(points_str):
    points_list = points_str.split(';')
    points = []
    for point in points_list:
        x, y = map(float, point.split(','))
        points.append((x, y))
    return points


# Plotting function
def plot_annotations(image_path, points, save_path=None):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    points_np = np.array(points, np.int32)
    points_np = points_np.reshape((-1, 1, 2))
    cv2.polylines(image, [points_np], isClosed=True, color=(255, 0, 0), thickness=2)

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


# Directory containing images
images_dir = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\real train'

# Loop through each annotation and plot the polygon on the image
for idx, row in annotations.iterrows():
    image_id = row['image_id'] + '.jpg'
    points_str = row['points']
    points = parse_points(points_str)

    image_path = os.path.join(images_dir, image_id)

    if os.path.exists(image_path):
        plot_annotations(image_path, points)
    else:
        print(f"Image {image_id} not found in {images_dir}")