# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
shutil.copyfile('Text_py.txt','copy.txt') #src,dest copy.txt will be created if doesn't exist
shutil.copy('Text_py.txt','copy.txt') #same arguments
shutil.copy2('Text_py.txt','copy.txt')