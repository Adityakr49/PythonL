import os

source ="copy.txt"
destination = "C:\\Users\\adity\\copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")#can also move a folder(directory)
except FileNotFoundError:
    print(source+" was not found")