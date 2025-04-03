import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import speech_recognition as sr

def initialize_webcam(width=1280, height=720):
    """Initialize webcam and set resolution."""
    cap = cv2.VideoCapture(0)
    cap.set(3, width)  # Set width
    cap.set(4, height)  # Set height
    if not cap.isOpened():
        raise Exception("Webcam could not be opened.")
    return cap

def load_overlay_image(image_path):
    """Load the overlay image with enhanced error handling."""
    print(f"Attempting to load image from: {image_path}")
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: '{image_path}' not found or could not be loaded.")
        print("Tip: Ensure the file exists and is a valid image format (e.g., .png or .jpg).")
        raise FileNotFoundError(f"Error: '{image_path}' not found or could not be loaded.")
    else:
        print("Image loaded successfully!")
    return img

def resize_and_overlay(base_img, overlay_img, center, scale):
    """Resize and overlay the image."""
    h1, w1, _ = overlay_img.shape
    newH, newW = max(1, (h1 + scale) // 2 * 2), max(1, (w1 + scale) // 2 * 2)  # Ensure even dimensions
    overlay_resized = cv2.resize(overlay_img, (newW, newH))

    cx, cy = center
    h, w, _ = base_img.shape
    x1, x2 = max(0, cx - newW // 2), min(w, cx + newW // 2)
    y1, y2 = max(0, cy - newH // 2), min(h, cy + newH // 2)

    if x1 < x2 and y1 < y2:  # Ensure overlay region is valid
        base_img[y1:y2, x1:x2] = overlay_resized[:y2 - y1, :x2 - x1]
    return base_img

def get_voice_command():
    """Capture voice command using the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice command (e.g., 'zoom in', 'zoom out', or 'reset')...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Voice Command: {command}")
            return command
        except sr.WaitTimeoutError:
            print("Voice command timeout. No input detected.")
        except sr.UnknownValueError:
            print("Could not understand the voice command.")
        except sr.RequestError as e:
            print(f"Error with the voice recognition service: {e}")
    return None

def main():
    try:
        # Suppress log warnings
        os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # TensorFlow warnings suppressed
        os.environ["GLOG_minloglevel"] = "2"  # MediaPipe log warnings suppressed

        cap = initialize_webcam()
        detector = HandDetector(detectionCon=0.8)

        image_path = r"C:\Users\vikas\OneDrive\Documents\Desktop\Pictures\download.png"
        overlay_img = load_overlay_image(image_path)

        scale, center = 0, (500, 500)

        while True:
            success, frame = cap.read()
            if not success:
                print("Failed to read from the webcam.")
                break

            hands, frame = detector.findHands(frame)

            if len(hands) == 1:  # Single hand detected
                fingers = detector.fingersUp(hands[0])

                if fingers == [0, 1, 0, 0, 0]:  # Move functionality
                    center = hands[0]["lmList"][8][:2]

            # Check for voice commands
            command = get_voice_command()
            if command:
                if "zoom in" in command:
                    scale += 10
                elif "zoom out" in command:
                    scale -= 10
                elif "reset" in command:
                    scale = 0
                    center = (500, 500)

            frame = resize_and_overlay(frame, overlay_img, center, scale)
            cv2.imshow("Image", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key
                break

    except FileNotFoundError as fnf_error:
        print(f"File Error: {fnf_error}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()