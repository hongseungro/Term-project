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
