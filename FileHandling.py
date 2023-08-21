import os
path1="C:\\Users\\adity\\Desktop\\PMSS" #add escape sequence at all slash point
if os.path.exists(path1):
     print("That location exists:")
     if os.path.isfile(path1):
         print("That is a file")
     elif os.path.isdir(path1):
         print("That is a directory!")

else:
    print("That location doesn't exist:")