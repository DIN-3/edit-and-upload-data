import csv
import os
import glob

# define the input and output folder paths
input_folder = 'Route/to/text/files' #folder where Text-files are located
output_folder = 'Route/where/you/want/to/save' #folder where you want to store the CSV-files

# create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# iterate over all the text files in the input folder
for filepath in glob.glob(os.path.join(input_folder, '*.txt')):
    # create the corresponding output file path
    filename = os.path.basename(filepath)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.csv')

    # read the data from the input file
    with open(filepath, 'r') as infile:
        data = [line.strip().split() for line in infile]

    # write the data to the output CSV file using semicolon as a separator
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=';') #Semicolon is needed in order to make the database understand the data
        writer.writerows(data)





            