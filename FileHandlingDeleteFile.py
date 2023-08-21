import os
import shutil
path='ToDelete.txt'
path1='ToDel'
try:
    # os.remove(path)    #delete a file
    # os.rmdir(path1)    #cannot delete folder with files
    shutil.rmtree(path1) #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path1+" was deleted")