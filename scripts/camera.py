# import the necessary packages
import numpy as np
import imutils
import cv2

from threading import Thread

class Camera:

	def __init__(self, resolution, framerate):

		self.w = resolution[0]
		self.h = resolution[1]

		# initialize the camera module
		self.cap = cv2.VideoCapture(0)

		# make video 1080p
		self.cap.set(3, self.w)
		self.cap.set(4, self.h)
		self.cap.set(5, framerate)

		self.stopped = False
		self.grabbed = None
		self.vFrame = None

		

		pass

	def start(self):

		Thread(target=self.get, args=()).start()
		
		return self

	def get(self):
		while not self.stopped:
			if not self.grabbed:
				self.stop()
			else:
				self.grabbed, self.frame = self.cap.read()
				self.vFrame = cv2.imencode('.jpg',self.frame)

	def stop(self):
		self.stopped = True

	# function to push back a jpeg frame to the streaming server
	def getFrame(self):

		self.grabbed, self.frame = self.cap.read()
		self.vFrame = cv2.imencode('.jpg',self.frame)
		return self.vFrame.tobytes()

	def __del__(self):

		self.cap.release()