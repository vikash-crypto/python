import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)  # Use '0' for the default webcam
cap.set(3, 1280)  # Set width
cap.set(4, 720)  # Set height

# Initialize Hand Detector
detector = HandDetector(detectionCon=0.8)

# Load overlay image with improved error handling
image_path = r"C:\Users\vikas\OneDrive\Documents\Desktop\Pictures\download.png"
img1 = cv2.imread(image_path)

if img1 is None:
    print(f"Error: '{image_path}' not found or could not be loaded. Please check the file path.")
    exit()

scale = 0         # Scaling factor for resizing the image
cx, cy = 500, 500  # Center position for overlay image

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from the webcam.")
        break

    # Detect hands
    hands, img = detector.findHands(img)

    # Zoom functionality with two hands
    if len(hands) == 2:
        fingers1 = detector.fingersUp(hands[0])
        fingers2 = detector.fingersUp(hands[1])

        if fingers1 == [1, 1, 0, 0, 0] and fingers2 == [1, 1, 0, 0, 0]:  # Index and middle fingers up
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]

            if len(lmList1) > 8 and len(lmList2) > 8:
                p1 = lmList1[8][:2]  # Index finger of hand 1
                p2 = lmList2[8][:2]  # Index finger of hand 2

                # Calculate distance between index fingertips
                length, info, img = detector.findDistance(p1, p2, img)

                # Adjust the scale dynamically based on the distance
                scale = int((length - 150) // 2)  # 150 is an arbitrary baseline distance
                cx, cy = info[4:]  # Center position between two fingers

    # Move functionality with one hand
    elif len(hands) == 1:
        fingers = detector.fingersUp(hands[0])

        if fingers == [0, 1, 0, 0, 0]:  # Only the index finger is up
            lmList = hands[0]["lmList"]

            if len(lmList) > 8:
                cx, cy = lmList[8][:2]  # Move the image to follow the index fingertip

    # Resize and overlay img1
    h1, w1, _ = img1.shape
    newH, newW = h1 + scale, w1 + scale
    newH = max(1, (newH // 2) * 2)  # Ensure height is an even number
    newW = max(1, (newW // 2) * 2)  # Ensure width is an even number

    img1_resized = cv2.resize(img1, (newW, newH))

    h, w, _ = img.shape
    x1, x2 = max(0, cx - newW // 2), min(w, cx + newW // 2)
    y1, y2 = max(0, cy - newH // 2), min(h, cy + newH // 2)

    # Ensure valid overlay region
    if x1 < x2 and y1 < y2:
        img[y1:y2, x1:x2] = img1_resized[:y2 - y1, :x2 - x1]

    cv2.imshow("Image", img)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
