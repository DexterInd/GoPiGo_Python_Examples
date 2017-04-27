#!/usr/bin/env python
from flask import Flask, render_template, Response

# Robot Video Streaming Example with a USB camera.
# This example will show you how to stream video from your robot.  In this example we use
# Python, a USB webcam, and a Flask server on the GoPiGo.  

# To Start: 
#       In the command line, type "sudo python stream_usb_camera.py"  You can include the "&" symbol at the end to run in the background.
#       Open a new broswer window and type in                   "http://<gopigo address>:5000" 
#       If you are using DexOS, the address is                  "http://gopigo.com:5000"
#       If you are using Raspbian for robots, the address is    "http://dex.local:5000"

from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
    # Video streaming home page.
    # This should serve up your USB Webcam video.
    url = "10.10.10.10"
    # url = "192.168.0.103"   # You should change this to your Raspberry Pi IP address.
                            # Hint: you can find the address by running "ifconfig" on the command line.
                            # If you are running DexOS you can replace this with "10.10.10.10"
    return render_template('usb_camera_index.html', url_address = url)

if __name__ == '__main__':
    print "Starting USB Camera camera!"
    print "To see the output of your camera, do the following: "
    print " Open a new broswer window and type in                   'http://<gopigo address>:5000' "
    print " If you are using DexOS, the address is                  'http://gopigo.com:5000'"
    print " If you are using Raspbian for robots, the address is    'http://dex.local:5000' "
    app.run(host='0.0.0.0', debug=True, threaded=True)