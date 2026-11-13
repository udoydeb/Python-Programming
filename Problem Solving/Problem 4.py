
import os

# Specify the directory path
directory_path = "/"

# List directory contents
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
