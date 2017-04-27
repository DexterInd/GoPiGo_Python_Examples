#!/usr/bin/env python
from flask import Flask, render_template, Response

# Robot Video Streaming Example with the Raspberry Pi Camera
# This example will show you how to stream video from your robot.  In this example we use
# Python, the Raspberry Pi Camera, and a Flask server on the GoPiGo.  

# To Start: 
#       In the command line, type "sudo python stream_pi_camera.py"  You can include the "&" symbol at the end to run in the background.
#       Open a new broswer window and type in                   "http://<gopigo address>:5000" 
#       If you are using DexOS, the address is                  "http://gopigo.com:5000"
#       If you are using Raspbian for robots, the address is    "http://dex.local:5000"

from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
    # Video streaming home page.
    # This should serve up your Raspberry Pi Camera video.
    return render_template('pi_camera_index.html')


def gen(camera):
    # Video streaming generator function.  For more on generator functions see Miguel Gringberg's beautiful post here:  https://blog.miguelgrinberg.com/post/video-streaming-with-flask
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag.
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    print "Starting Raspberry Pi video camera!"
    print "To see the output of your camera, do the following: "
    print " Open a new broswer window and type in                   'http://<gopigo address>:5000' "
    print " If you are using DexOS, the address is                  'http://gopigo.com:5000'"
    print " If you are using Raspbian for robots, the address is    'http://dex.local:5000' "
    app.run(host='0.0.0.0', debug=True, threaded=True)