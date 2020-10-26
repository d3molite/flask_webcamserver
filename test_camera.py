from scripts import camera

camera = camera.Camera(resolution=[1920,1080], framerate=60)

while(True): 
	# Capture frame-by-frame
	ret, frame = camera.cap.read()

	cv2.imshow("preview",frame)

	#Waits for a user input to quit the application

	if cv2.waitKey(1) & 0xFF == ord("q"):

		break