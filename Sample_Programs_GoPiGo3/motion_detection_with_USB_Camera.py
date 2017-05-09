import glob
import os
import time

# The motion program, running in the background of DexterOS is constantly taking pictures
# and putting them into the /var/lib/motion folder.  Here, every 5 seconds we check for
# the latest picture in the directory and load it up as binary data.
# Then we compare the binary data of the last picture to the latest picture.  
# If we see a change in the binary data, we our camera has detected motion!

# This function checks the motion directory where webcam photos are stored.
# Returns the file name and directory of the latest picture file stored.
def get_latest_file():
    list_of_files = glob.glob('/var/lib/motion/*.jpg')
    latest_file = max(list_of_files, key=os.path.getctime)
    print "Latest File: " + str(latest_file)
    return latest_file

latest_file_name = get_latest_file()            # Get the latest file name in the motion directory.
picture_file = open(latest_file_name, 'rb')     # Open the file for reading.
last_picture_data = picture_file.read()         # Load the picture file up as binary data.
picture_file.close()                            # Good housekeeping: close the file.

while True:

    time.sleep(5)                               # Check every 5 seconds.
    latest_file = get_latest_file()             # Get the latest file in the directory.
    picture_file = open(latest_file, 'rb')      # Open the latest file.
    new_picture_data = picture_file.read()      # Load the latest file to binary data.
    picture_file.close()                        # Close the file.
    
    if (new_picture_data != last_picture_data): # Compare the last picture to the current picture.
        print("Found motion!")                  # If the picture has changed, alert!  
        last_picture_data = new_picture_data    # Make the last picture the current picture data.
    else:
        print("No motion!")                     # If nothing has changed, nothing has changed!
