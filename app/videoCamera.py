import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

        self.mp_holistic = mp.solutions.holistic  # Holistic model
        self.mp_drawing = mp.solutions.drawing_utils  # Drawing utilities

    def __del__(self):
        self.video.releast()

    def get_frame(self):
        ret, frame = self.video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            break

        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def draw_landmarks(self, image, results):
        self.mp_drawing.draw_landmarks(
            image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS
        )  # Draw left hand connections
        self.mp_drawing.draw_landmarks(
            image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS
        )  # Draw right hand connections

    def draw_styled_landmarks(self, image, results):
        # Draw left hand connections
        self.mp_drawing.draw_landmarks(
            image,
            results.left_hand_landmarks,
            self.mp_holistic.HAND_CONNECTIONS,
            self.mp_drawing.DrawingSpec(
                color=(121, 22, 76), thickness=2, circle_radius=4
            ),
            self.mp_drawing.DrawingSpec(
                color=(121, 44, 250), thickness=2, circle_radius=2
            ),
        )
        # Draw right hand connections
        self.mp_drawing.draw_landmarks(
            image,
            results.right_hand_landmarks,
            self.mp_holistic.HAND_CONNECTIONS,
            self.mp_drawing.DrawingSpec(
                color=(245, 117, 66), thickness=2, circle_radius=4
            ),
            self.mp_drawing.DrawingSpec(
                color=(245, 66, 230), thickness=2, circle_radius=2
            ),
        )

    def get_frame_hand(self):
        ret, frame = self.video.read()
        with self.mp_holistic.Holistic(
            min_detection_confidence=0.5, min_tracking_confidence=0.5
        ) as holistic:
            # Make detections
            image, results = mediapipe_detection(frame, holistic)
            print("image :", image)
            print("result :", results)

            # Draw landmarks
            self.draw_styled_landmarks(image, results)

        ret, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False  # Image is no longer writeable
    results = model.process(image)  # Make prediction
    image.flags.writeable = True  # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
    return image, results