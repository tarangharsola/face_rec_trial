from camera import Camera
import cv2

def main():
    camera = Camera()

    try:
        # Start the camera
        camera.start()
        print("Camera started. Press 'q' to quit.")

        while True:
            # Capture a frame
            frame = camera.capture_frame()

            # Display the frame
            cv2.imshow("Camera Feed", frame)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        # Stop the camera and release resources
        camera.stop()
        cv2.destroyAllWindows()
        print("Camera stopped.")

if __name__ == "__main__":
    main()