import os

# root dir
rootDir = './folder/'

# loop through each directory in the tree
for dirName, subdirList, fileList in os.walk(rootDir):
    # loop through each file
    for fname in fileList:
        # if the file is a certain type, keep it
        if fname.endswith('.txt'):
            continue
        # otherwise, delete it
        os.remove(os.path.join(dirName, fname))