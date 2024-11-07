import os
import json
import csv

# Define the directory containing JSON files
json_dir = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\labelme pith annotation'  # Replace with the path to your JSON files directory
output_csv = r'C:\Users\User\Desktop\Team Brikkho\dataset_1\Tree-Dataset-1\Final_Dataset.v1i.tensorflow\train\labelme pith annotation\output.csv'

# Initialize a list to hold all data
all_data = []

# Read each JSON file
for json_file in os.listdir(json_dir):
    if json_file.endswith('.json'):
        file_path = os.path.join(json_dir, json_file)
        with open(file_path, 'r') as f:
            data = json.load(f)

            # Extracting relevant fields from JSON
            version = data.get('version', '')
            image_id = os.path.splitext(json_file)[0]  # Get the filename without extension
            for shape in data.get('shapes', []):
                label = shape.get('label', '')
                points = shape.get('points', [])
                group_id = shape.get('group_id', '')
                description = shape.get('description', '')
                shape_type = shape.get('shape_type', '')
                flags = shape.get('flags', {})
                mask = shape.get('mask', '')

                # Flattening points for CSV
                points_str = '; '.join([f"{point[0]},{point[1]}" for point in points])

                # Append the extracted data to the list
                all_data.append(
                    [version, image_id, label, points_str, group_id, description, shape_type, json.dumps(flags), mask])

# Define the CSV header
header = ['version', 'image_id', 'label', 'points', 'group_id', 'description', 'shape_type', 'flags', 'mask']

# Write data to CSV
with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(all_data)

print(f"Data successfully written to {output_csv}")
