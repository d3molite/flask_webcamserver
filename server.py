# main.py
# import the necessary packages
from flask import Flask, render_template, Response
from scripts import camera
import threading

app = Flask(__name__)

# initialize a new camera
cam = camera.Camera(resolution=[1920,1080], framerate=60, device=0)
thread = camera.Thread2()


@app.route('/')
def index():
    return render_template('index.html')

def gen(thread):
    while True:
        #get camera frame
        frame = cam.getFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

	# # start the thread for capturing the images
	thread.start(camera)

    # defining server ip address and port
	app.run(host='0.0.0.0',port='5000', debug=True, threaded=True)