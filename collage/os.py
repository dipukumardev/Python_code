# import os
# print(os.getcwd())

import os

# Get the current working directory
current_directory = os.getcwd()
print("Current directory:", current_directory)

# List files and directories in the current directory
print("Contents of current directory:")
for item in os.listdir():
    print(item)

# Create a new directory
new_directory = "new_directory"
os.mkdir(new_directory)

# Rename the directory
os.rename(new_directory, "renamed_directory")

# Delete the directory
os.rmdir("renamed_directory")
