# Hand Detection Using OpenCV & MediaPipe 

This repository contains a Python script for real-time hand detection using OpenCV and MediaPipe. The script detects hands in a webcam feed and captures the landmarks which are then converted into coordinates.

## Importing libraries

- OpenCV library (`pip install opencv-python`)
- MediaPipe framework (`pip install mediapipe`)

## Running the Script

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/shubhangi0301/hand-detection.git
   ```


2. Navigate to the directory containing the script:

   ```bash
   cd hand-detection
   ```

3. Run the script:

   ```bash
   python hands_detection.py
   ```
4. The script will open a window displaying the webcam feed with rectangles drawn around detected faces. Press the `q` key to exit the program.

## FAQs

1. What is MediaPipe? How is it used for hand detection?

        Google offers an open-source framework called MediaPipe that processes media data using pre-built models. This makes it simple to include complex features like object detection and hand tracking. By using taught patterns to identify locations that are likely to contain hands, MediaPipe's hand detection model examines video frames.

2. What is OpenCV?
    
        OpenCV is a free, open-source library for computer vision tasks.  It offers over 2500 algorithms for image processing, object detection, and real-time applications. Popular for its cross-platform compatibility and large developer community, OpenCV empowers creation of various computer vision projects.