# import the necessary packages
import imutils
import cv2


class Camera:

	def __init__(self, resolution, framerate, device):

		self.w = resolution[0]
		self.h = resolution[1]

		# initialize the camera module
		try:
			self.cap = cv2.VideoCapture(device-1)
		except:
			self.cap = cv2.VideoCapture(device-1)

		# make video 1080p
		self.cap.set(3, self.w)
		self.cap.set(4, self.h)
		self.cap.set(5, framerate)

		self.stopped = False
		self.grabbed = None
		self.eFrame = None
		self.vFrame = None

	# function to push back a jpeg frame to the streaming server
	def getFrame(self):

		while True:
			ret, frame = self.cap.read()
			if ret:
				ret, self.eFrame = cv2.imencode('.jpg',frame)
				self.vFrame = self.eFrame.tobytes()

	def get(self):

		return self.vFrame

	def __del__(self):

		self.cap.release()

	