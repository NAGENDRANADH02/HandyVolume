import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import math
import time
 
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.85, min_tracking_confidence=0.85)
mp_draw = mp.solutions.drawing_utils

 
cap = cv2.VideoCapture(0)

 
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
 
min_vol, max_vol = volume.GetVolumeRange()[:2]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            landmarks = hand_landmarks.landmark
            thumb_tip = landmarks[4]   # Thumb tip
            index_tip = landmarks[8]   # Index finger tip

              
            h, w, _ = frame.shape
            x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
            x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

            # Draw circles & line
            cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

            # Calculate distance
            distance = math.hypot(x2 - x1, y2 - y1)

            # Force max volume when distance > 120
            if distance > 120:
                volume.SetMasterVolumeLevelScalar(1.0, None)  # 100% Volume
                print("🔊 Volume set to MAX (100%)!")
            else:
                # Normal volume control
                volume.SetMasterVolumeLevelScalar(np.interp(distance, [20, 120], [0.0, 1.0]), None)

            # Display current volume
            current_vol = volume.GetMasterVolumeLevelScalar() * 100
            print(f"Current System Volume: {int(current_vol)}%")

            cv2.putText(frame, f'Volume: {int(current_vol)}%', (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Volume Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
