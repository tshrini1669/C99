import os
import time
import shutil
path="https://www.dropbox.com/home/TestFolder"
days = 30
if(os.path.exists(path)):
    remove_folder()
    deletefolder = deletefolder + 1
else:
    print("The path does not exist")
def remove_folder():
    if not shutil.rmtree(path):
        print("It is removed")
    else:
        print("Unable to remove!")