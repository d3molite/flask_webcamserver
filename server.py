# main.py
# import the necessary packages
from flask import Flask, render_template, Response
import cv2
import imutils

app = Flask(__name__)

class Camera:

	def __init__(self, resolution, framerate, device):

		self.w = resolution[0]
		self.h = resolution[1]

		# initialize the camera module
		self.cap = cv2.VideoCapture(device)
		self.cap.release()
		self.cap = cv2.VideoCapture(device)

		# make video 1080p
		self.cap.set(3, self.w)
		self.cap.set(4, self.h)
		self.cap.set(5, framerate)

		self.stopped = False
		self.grabbed = None
		self.vFrame = None

		pass

	# function to push back a jpeg frame to the streaming server
	def getFrame(self):

		ret, frame = self.cap.read()
		ret, self.vFrame = cv2.imencode('.jpg',frame)

		return self.vFrame.tobytes()

	def __del__(self):

		self.cap.release()

# initialize a new camera
cam = Camera(resolution=[1920,1080], framerate=60, device=0)


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
    return Response(gen(cam),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

    # defining server ip address and port
	app.run(host='0.0.0.0',port='5000', debug=False, threaded=True)