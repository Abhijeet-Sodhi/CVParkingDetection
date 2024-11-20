# CVParkingDetection

This project detects parking space availability in video footage. Users mark parking spaces manually, which are saved. The system then processes each video frame, checks parking occupancy, and displays the status with color-coded spaces (green for free, red for occupied) along with a count of available spaces.

## Credits
[![Parking Space Counter using OpenCV Python | Computer Vision](https://img.youtube.com/vi/caKnQlCMIYI&list=LL/0.jpg)](https://www.youtube.com/watch?v=caKnQlCMIYI&list=LL) Murtaza's Workshop - Robotics and AI 

## Demo
https://github.com/user-attachments/assets/50507aa6-d0a8-4447-93a2-8eee15d905f2

## Functionality
The system works as a parking space monitoring solution that processes video footage to detect the availability of parking spaces in a parking lot. Here's how it functions theoretically:

**Video Processing:**
The system captures frames from a video showing the parking lot. Each frame is analyzed in sequence to track the status of parking spaces in real time.

**Image Preprocessing:**
The frames are converted to grayscale, blurred, and thresholded to create a binary image (black and white). This helps reduce noise and makes it easier to detect changes in the scene (like cars entering or leaving parking spaces).

**Parking Space Detection:**
The parking spaces are predefined by the user, who manually selects the areas in the video where the parking spaces are located. These areas are stored and used to check whether a car is occupying a space.
The system counts the number of non-black pixels in each parking space. If the count is low, the space is considered empty (free); if it's high, it indicates the space is occupied by a vehicle.

**User Input for Parking Space Setup:**
Users can dynamically define or remove parking spaces by drawing rectangles on the parking lot image. These positions are saved for future use, allowing the system to adapt to different parking lot layouts.

**Real-Time Feedback:**
As the video is processed, rectangles are drawn around the predefined parking spaces. Each rectangle is color-coded: green for free spaces and red for occupied ones.
The system continuously updates and displays the number of available spaces in the parking lot.

**Persistence:**
The positions of parking spaces are stored in a file, so even if the system is restarted, the user-defined spaces persist and don't need to be redefined.

**Exit Control:**
The system runs in a loop until the user decides to stop it, typically by pressing a key, allowing for manual interruption of the process.

## The Whys:
**OpenCV** is the go-to library for computer vision, providing efficient tools for video capture, image processing, and object detection (e.g., thresholding, drawing rectangles), making it ideal for this task over alternatives like Pillow or scikit-image.\
**pickle** serializes Python objects (like parking space positions) to store and reload them easily without the need for complex databases.\
**cvzone** A higher-level OpenCV wrapper that simplifies tasks like text overlays and drawing rectangles which reduces code complexity and enhances visual output without writing custom OpenCV code for each annotation.\
**numpy** Essential for array manipulation in image processing, enabling efficient operations like dilation integrating seamlessly with OpenCV.\
**Why Grayscale & Thresholding:** Simplifies image data for detecting occupancy by reducing unnecessary color information and improving contrast.\
**Why Pixel Count:** A simple, fast method to determine if a parking space is free based on pixel activity, avoiding the complexity of object detection.\
**Why Rectangle detection:** using predefined coordinates is more efficient than dynamic detection and avoids the complexity of training a machine learning model, offering a simpler, manually defined solution.\
