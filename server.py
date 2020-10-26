# main.py
# import the necessary packages
from flask import Flask, render_template, Response
import cv2
import imutils

from scripts import camera, processor

app = Flask(__name__)

# initialize a new camera
cam = processor.CameraProcess(resolution=[1280,720], framerate=30, device=0)


@app.route('/')
def index():
    return render_template('index.html')

def gen():
	while True:
		#get camera frame
		frame = cam.getFrame()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

	cam.start()

    # defining server ip address and port
	app.run(host='0.0.0.0',port='5000', debug=False, threaded=True)