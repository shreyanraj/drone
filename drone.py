from codrone_edu.drone import Drone
import cv2
import mediapipe as mp
import threading

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize CoDrone EDU
drone = Drone()
drone.pair()

# Set up camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Track drone state
is_flying = False  
frame = None
lock = threading.Lock()

# Count the number of extended fingers
def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]  # Finger tip landmarks
    count = sum(1 for tip in tips if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y)
    return count

# Drone control function (multi-threaded)
def control_drone(command):
    global is_flying

    if command == "TAKEOFF" and not is_flying:
        print("Takeoff")
        drone.takeoff()
        is_flying = True

    elif command == "LAND" and is_flying:
        print("Landing")
        drone.land()
        is_flying = False

    elif command == "MOVE RIGHT":
        print("Moving Right")
        drone.set_roll(20) 
        drone.move(1) 

    elif command == "MOVE LEFT":
        print("Moving Left")
        drone.set_roll(-20)  
        drone.move(1)

    elif command == "HOVER":
        print("Hover")
        drone.hover(1)

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for natural orientation
    frame = cv2.flip(frame, 1)

    # Convert to RGB for MediaPipe processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    command = "UNKNOWN"

    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Count the number of extended fingers
            num_fingers = count_fingers(landmarks)

            # Determine drone command based on number of fingers
            if num_fingers == 5:  # All fingers extended (Takeoff)
                command = "TAKEOFF"
            elif num_fingers == 0:  # No fingers extended (Landing)
                command = "LAND"
            elif num_fingers == 2:  # Two fingers extended (Move Right)
                command = "MOVE RIGHT"
            elif num_fingers == 3:  # Three fingers extended (Move Left)
                command = "MOVE LEFT"
            else:
                command = "HOVER"  # Default to hover if none of the conditions match

            # Run drone commands in a separate thread
            threading.Thread(target=control_drone, args=(command,)).start()

            # Display current command on frame
            cv2.putText(frame, command, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Hand Gesture Drone Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
drone.land()
drone.close()
