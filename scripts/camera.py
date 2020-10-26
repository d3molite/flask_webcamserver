# import the necessary packages
import imutils
import cv2

class Camera:

	def __init__(self, resolution, framerate, device):

		self.w = resolution[0]
		self.h = resolution[1]

		# initialize the camera module
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