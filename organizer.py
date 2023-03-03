import os
import shutil
import logging
import schedule
import time

# get working directory
dir = os.getcwd()
# Write status to log file
logging.basicConfig(filename='organizer.log', level=logging.INFO, format='%(asctime)s %(message)s')

def job():
    # set /movies as working dir and run
    rootDir = dir + '/movies/'
    organizer(rootDir)
    # set /tv as working dir and run
    rootDir = dir + '/tv/'
    organizer(rootDir)
    
def organizer(rootDir):
    # Command-line argument was provided
    for dirName, subdirList, fileList in os.walk(rootDir):
        # loop through each file
        for fname in fileList:
            # if the file is a certain type, keep it
            if fname.endswith('.mkv') or fname.endswith('.mp4') or fname.endswith('.srt') or fname.endswith('.!qB'):
                continue
            # otherwise, delete it
            os.remove(os.path.join(dirName, fname))
    logging.info('Files deleted' + rootDir)

    # Walk through subdirectories
    for root, dirs, files in os.walk(rootDir):
        # Check if there is a .mkV file
        if any(fname.endswith('.mkV') for fname in files):
            # Loop through all subdirectories
            for subdir in dirs:
                # Construct the path to the subdirectory
                subdir_path = os.path.join(root, subdir)
                # Check if there are .srt files in the subdirectory
                if any(fname.endswith('.srt') for fname in os.listdir(subdir_path)):
                    # Move the .srt files to the same directory as the .mkV file
                    for fname in os.listdir(subdir_path):
                        if fname.endswith('.srt'):
                            shutil.move(os.path.join(subdir_path, fname), root)
    logging.info('Sub files moved in' + rootDir)

    # list the files and folders in the working directory
    for filename in os.listdir(rootDir):
        # check if the file/folder is a directory
        if os.path.isdir(filename):
            # check if the directory is empty
            if not os.listdir(filename):
                # if it is empty, delete it
                os.rmdir(filename)
    logging.info('Empty folders deleted' + rootDir)

# Run every hour
schedule.every().hour.do(job)
while True:
    logging.debug('Running script')
    schedule.run_pending()
    logging.debug('Sleeping for 1h')
    time.sleep(1)