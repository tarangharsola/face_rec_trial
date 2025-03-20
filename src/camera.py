import cv2

class Camera:
    def __init__(self):
        self.capture = None

    def start(self):
        """
        Start the camera capture.
        """
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            raise RuntimeError("Unable to access the camera.")

    def stop(self):
        """
        Stop the camera capture and release resources.
        """
        if self.capture is not None and self.capture.isOpened():
            self.capture.release()
            self.capture = None

    def capture_frame(self):
        """
        Capture a single frame from the camera.
        """
        if self.capture is not None:
            ret, frame = self.capture.read()
            if ret:
                return frame
            else:
                raise RuntimeError("Failed to capture frame from the camera.")
        raise RuntimeError("Camera is not started.")