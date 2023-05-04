import pymongo
import os

# Connect to the MongoDB client
client = pymongo.MongoClient("mongodb+srv://polar_project_database:polar_project_database@cluster0.mec6yfh.mongodb.net/test")

# Select the database and collection to use
db = client["database1"]
collection = db["Pole_vault"] #this defines that all the new updates will end up in "Sprints" section

# Pole_vault
# Hurdles
# Sprints

#Those previously mentioned 3 are the active collections where you can store data


# Set the path to the folder containing the data
folder_path = "Path/to/CSV/files"

# Iterate over the files in the folder
for file_name in os.listdir(folder_path):
    
    # Construct the full path to the file
    file_path = os.path.join(folder_path, file_name)
    
    # Open the file and read its contents
    with open(file_path, "r") as f:
        data = f.read()
    
    # Create a dictionary to store the data and its ID
    data_dict = {
        "data": data,
        "file_id": file_name
    }  
    
    # Insert the data into the MongoDB collection
    collection.insert_one(data_dict)




#mongodb+srv://polar_project_database:polar_project_database@cluster0.mec6yfh.mongodb.net/test