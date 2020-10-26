# import the necessary packages
import numpy as np
import imutils
import cv2

from threading import Thread

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


class Thread2:

	def __init__(self):

		self.stopped = False
		self.frame = None

	def start(self, camera):

		Thread(target=self.get, args=(camera)).start()
			
		return self

	def get(self, camera):
		while not self.stopped:
			self.frame = camera.getFrame()

	def stop(self):
		self.stopped = True