from multiprocessing import Process
import multiprocessing, time

from multiprocessing.managers import BaseManager

from . import camera

# define a custom process manager and register the bot class as a launchable process
class MyManager(BaseManager):
    pass

MyManager.register("camera", camera.Camera)


def Manager():

    m = MyManager()
    m.start()
    return m

class CameraProcess:
	def __init__(self, resolution, framerate, device):

		self.resolution = resolution
		self.framerate = framerate
		self.device = device

		self.name = "Camera"

		self.camera = None
		self.manager = None
		self.process = None

		pass

	def setup(self):

		self.manager = Manager()
		self.camera = self.manager.camera(
			resolution=self.resolution,
			framerate = self.framerate,
			device=self.device
		)

	def start(self):
		if self.process is not None:
			if self.process.is_alive():
				print("--------------------")
				print("CAMERA ALREADY RUNNING")
				print("--------------------")
		else:
			self.setup()
			print("--------------------")
			print("STARTING CAMERA")
			print("--------------------")
			self.process = Process(target=self.camera.getFrame, name=self.name, daemon=True)
			self.process.start()

	def getFrame(self):

		if self.process is not None and self.process.is_alive():

			return self.camera.get()