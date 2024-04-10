import cv2
import mediapipe as mp

def detect_hand_landmarks(image):
    # Initialize MediaPipe Hands model
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image
    results = hands.process(image_rgb)

    # Check if hands were detected
    if results.multi_hand_landmarks:
        # Get landmarks for the first hand (assuming only one hand is present)
        hand_landmarks = results.multi_hand_landmarks[0]

        # Convert landmarks to coordinates
        hand_coordinates = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]

        return hand_coordinates

    return None

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect hand landmarks
        hand_coordinates = detect_hand_landmarks(frame)

        # Draw landmarks on the frame
        if hand_coordinates:
            for coord in hand_coordinates:
                x, y, _ = coord
                x_pixel, y_pixel = int(x * frame.shape[1]), int(y * frame.shape[0])
                cv2.circle(frame, (x_pixel, y_pixel), 5, (0, 255, 0), -1)

        # Display the frame
        cv2.imshow('Hand Landmarks', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
