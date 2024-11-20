import cv2
import pickle

drawing = False  # Flag to indicate drawing in progress
start_point = None  # Starting corner of the rectangle
posList = []    # List to store parking space positions

# Load existing parking positions if available
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)

    # Remove rectangles with very small dimensions (e.g., width or height < 10 pixels)
    posList = [pos for pos in posList if pos[2] > 10 and pos[3] > 10]

    # Save the cleaned positions
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)
        
except FileNotFoundError:
    posList = [] # user defines parking spot by selecting rectangles then stored in empty list []

# Function to handle mouse events for selecting or removing parking spaces
def mouseClick(events, x, y, *_): #*_accept any additional positional arguments and treat them as unused.
    global drawing, start_point, posList

    if events == cv2.EVENT_LBUTTONDOWN: # Start drawing a rectangle
        start_point = (x, y)
        drawing = True

    elif events == cv2.EVENT_MOUSEMOVE and drawing: # Draw a temporary rectangle as the user drags the mouse
        temp_img = img.copy()
        cv2.rectangle(temp_img, start_point, (x, y), (255, 0, 255), 2)
        cv2.imshow("Image", temp_img)

    elif events == cv2.EVENT_LBUTTONUP: # Finish drawing the rectangle and save its position
        end_point = (x, y)
        width = abs(end_point[0] - start_point[0])
        height = abs(end_point[1] - start_point[1])
        posList.append((start_point[0], start_point[1], width, height))
        drawing = False

        # Save the updated positions
        with open("CarParkPos", "wb") as f:
            pickle.dump(posList, f)

    elif events == cv2.EVENT_RBUTTONDOWN:   # Remove a rectangle if the right mouse button is clicked
        for i, pos in enumerate(posList):
            x1, y1, w, h = pos
            if x1 < x < x1 + w and y1 < y < y1 + h:
                posList.pop(i)
                break

        # Save the updated positions
        with open("CarParkPos", "wb") as f:
            pickle.dump(posList, f)

# Main loop to display the image and handle user interaction
while True:
    img = cv2.imread("carParkImg.png")  # Load the parking lot image
    for pos in posList:
        x, y, w, h = pos
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)    # Draw saved rectangles

    cv2.imshow("Image", img)    # Show the image
    cv2.setMouseCallback("Image", mouseClick)   # Set up mouse callbacks
        
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Exit when 'q' is pressed
        print("Exiting...")
        break
