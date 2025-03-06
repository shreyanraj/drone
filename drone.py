from codrone_edu.drone import *
import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

drone = Drone()
drone.pair()

cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    count = sum(1 for tip in tips if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y)
    return count

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                fingers = count_fingers(hand_landmarks)
                
                if fingers == 5:
                    print("Takeoff")
                    drone.takeoff()
                elif fingers == 0:
                    print("Landing")
                    drone.land()
                elif fingers == 2 and hand_landmarks.landmark[8].x < hand_landmarks.landmark[6].x:
                    print("Moving Left")
                    drone.set_pitch(10)
                elif fingers == 3 and hand_landmarks.landmark[8].x > hand_landmarks.landmark[6].x:
                    print("Moving Right")
                    drone.set_pitch(-10)
                
        cv2.imshow("Hand Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
drone.close()
