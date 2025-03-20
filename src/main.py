import cv2
from camera import Camera
from face_recognition import FaceRecognizer

def main():
    # Initialize the camera
    cam = Camera()
    cam.start()

    # Initialize the face recognizer
    recognizer = FaceRecognizer()

    try:
        while True:
            # Capture a frame from the camera
            frame = cam.capture_frame()

            # Perform face recognition
            recognized_frame = recognizer.recognize_faces(frame)

            # Display the resulting frame
            cv2.imshow('Face Recognition', recognized_frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the camera and close windows
        cam.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()