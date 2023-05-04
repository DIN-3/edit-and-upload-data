import os
import csv
import re

# Define the folder containing the CSV files
folder_path = 'path/to/CSV/files'

# Loop over each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Open the CSV file
        with open(os.path.join(folder_path, filename), 'r') as input_file:
            # Create a CSV reader and writer objects
            reader = csv.reader(input_file, delimiter=';')
            rows = list(reader)

        # Modify the data in each row
        for row in rows:
            # Remove the brackets and anything inside them
            for i in range(len(row)):
                row[i] = re.sub(r'\[.*?\]', '', row[i])

            # Remove column E or "marker"
            del row[4]

            # Replace commas with dots
            for i in range(len(row)):
                row[i] = row[i].replace(',', '.')

        # Write the modified data to the same CSV file
        with open(os.path.join(folder_path, filename), 'w', newline='') as output_file:
            writer = csv.writer(output_file, delimiter=';')
            writer.writerows(rows)