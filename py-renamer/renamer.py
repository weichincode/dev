import os, glob

# path to folder
home_dir = "/home/User/Folder"

# change dir to home_dir
path_parent = os.chdir(home_dir)

# add all files names into list
file_names = os.listdir()
print("Here are all the files in the directory: " + str(file_names))

for folder in file_names:
    os.chdir(folder)

    for vid in glob.glob("*.mp4"):
        new_name = folder + ".mp4"
        os.rename(vid, new_name)
        print("File has been renamed to: " + new_name)
        os.chdir(home_dir)

