import cv2
import pickle
import cvzone
import numpy as np

# Load the video file of the parking lot
cap = cv2.VideoCapture("carPark.mp4")

# Load parking space positions from the file
with open('CarParkPos', 'rb') as f:
     posList = pickle.load(f)

def checkParkingSpace(imgPro):
    spaceCounter = 0    # Keeps track of free spaces

    for i, pos in enumerate(posList):
        x, y, w, h = pos    # Get coordinates and dimensions of the parking space

        imgCrop = imgPro[y:y+h, x:x+w]  # Crop the area of interest from the processed image
        count = cv2.countNonZero(imgCrop)   # Count the number of white pixels

        if count < 950:
            color = (0, 255, 0)  # Green for free spaces
            thickness = 3
            spaceCounter += 1
        else:
            color = (0, 0, 255)  # Red for occupied spaces
            thickness = 2

        # Draw the rectangle
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)

        # Display the parking space number at the center
        cv2.putText(img, str(i + 1), (x + w // 2 - 10, y + h // 2 + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)    # Cyan color

        # Display the pixel count for each parking spot            
        cvzone.putTextRect(img, str(count), (x, y+h - 3), scale = 1, 
                           thickness = 2, offset = 0, colorR = color)            

    # Display total free spaces
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                       thickness=5, offset=20, colorR=(0, 200, 0))

while True:
    # Restart the video if it ends
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()   # Read a frame from the video
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)  # Apply Gaussian blur
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                         cv2.THRESH_BINARY_INV, 25, 16) # Thresholding
    
    imgMedian = cv2.medianBlur(imgThreshold, 5) # Reduce noise using median blur
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1) # Dilate the image
    
    checkParkingSpace(imgDilate)    # Check the parking spaces in the processed image

    cv2.imshow("Image", img)    # Show the current frame with parking status
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThres", imgMedian)
    cv2.waitKey(10)

    # Exit the program when 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Exit when 'q' is pressed
        print("Exiting...")
        break
