# 1. 홍승로
import cv2
import sys
import mediapipe as mp
import math
import time

# 얼굴 검출을 위한 Haar Cascade 분류기 초기화
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 두 점 사이의 거리 계산 함수
def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))

# Mediapipe 초기화
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(max_num_hands=5)
# 2. 최서윤
# 카메라 영상 가져오기
cap = cv2.VideoCapture(0)

# 카메라가 열렸는지 확인
if not cap.isOpened():
    print("Error: Camera is not opened")
    sys.exit(1)

frame_number = 0
while True:
    res, frame = cap.read()

    if not res:
        print("Error: camera error")
        break

    # 그레이스케일로 변환하여 얼굴 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Mediapipe를 이용한 손 검출
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    v_count = 0
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                mp.solutions.drawing_styles.get_default_hand_connections_style(),
            )

            points = hand_landmarks.landmark

            fingers = 0

            if distance(points[4], points[9]) > distance(points[3], points[9]):
                fingers += 1

            for i in range(8, 21, 4):
                if distance(points[i], points[0]) > distance(points[i - 1], points[0]):
                    fingers += 1
