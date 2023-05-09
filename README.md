# edit-and-upload-data


There are 3 different script that allow you to modify and upload the data to database.
In order yo make these scripts work you need to install Python
https://www.python.org/downloads/

after you've installed it we'll continue by Navigating to the folder with all the data, that you want to upload.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/7233b144-bb77-4f50-b06d-bd091499085f)

This sensor that we used gave me data, that looked like this. From here we must **copy address as text**, by right-clicking the path to the folder.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/790d5ec8-bb87-496a-8387-dc9b6d62ab26)

Now that since that is selected lets go back to the folder where you've downloaded the scripts. They should look something like this.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/22de75c2-df96-40db-ab19-909219a520d4)

Start by editing the "convert.py"-file.
Easiest way to edit these is to right-click and open with -> Notepad.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/4c500df2-8ec6-4ec8-8711-9cce87479e99)

After opening these with Notepad make sure you **Copy and paste** your path to the folder with all the data in text-file format to this **Highlighted** part.
Make sure you have slash symbols there ( / ) instead of backslash ( \ )

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/bc28a17a-4d17-4165-a50c-db4ead856b9c)

You'll also see output_folder there remember to select a folder where you will save the CSV-files, by replacing the "Route/where/you/want/to/save"-part.
Now run this by right-clicking the Python script and selecting Open with -> Python.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/5106c31f-2749-4a45-8229-fa675c0e34c7)

Now you have a folder, which has all the data in CSV-files, and it should look something like this.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/fa807c8f-bd47-4c8c-9245-71ddf81f3d67)

Here we must edit the "editData.py"-file, again by right-clicking and selecting open with -> Notepad.
Go and edit the "path/to/CSV/files"-part of the code to the path to the folder, where you have created your CSV-files.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/ae135de7-6508-4f1d-a961-aa662c77232f)

Run this by right-clicking the "editData.py", and Open with -> Python.
This code will edit the existing CSV-files in your folder, which means that it wont be creating any unnecessary CSV-files.

As a last thing we must edit "uploadData.py"-file and run it after editing it.
Right click, open with -> Notepad and you will see a file which looks like this.

![image](https://github.com/DIN-3/edit-and-upload-data/assets/70267456/375504a9-8f5a-4068-abed-af429466e761)

Edit the **Highlighted** part of the code, and give it path the to folder address, where you have your CSV-files.
Run the "uploadData.py"-file by right-clicking and opening with Python.





