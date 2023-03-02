import os
import subprocess
# get working directory
rootDir = os.getcwd()
# Command-line argument was provided
for dirName, subdirList, fileList in os.walk(rootDir):
    # loop through each file
    for fname in fileList:
        # if the file is a certain type, keep it
        if fname.endswith('.mkv') or fname.endswith('.mp4') or fname.endswith('.srt') or fname.endswith('.!qB'):
            continue
        # otherwise, delete it
        os.remove(os.path.join(dirName, fname))
# delete empty folders in working dir
subprocess.call('find . -type d -empty -delete', shell=True)