import cv2
import time
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp

from keras.models import load_model

# Key dictionary from validation generator, used to get true labels from preds
key_dict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

model = load_model("./EfficientNetB3_26012023.h5")


class Analyse(object):
    def __init__(self, image, user_name, folder_upload):
        # self.path = './uploads/'
        self.path = folder_upload
        self.userName = user_name
        self.landmarks = ""
        self.letter_predict = ""
        self.percent = ""
        self.imgUpload = image
        path = self.path + "/" + image

        self.src = cv2.imread(path)

        self.mp_holistic = mp.solutions.holistic  # Holistic model
        self.mp_drawing = mp.solutions.drawing_utils  # Drawing utilities

    def get_frame(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_hands = mp.solutions.hands

        ########################################################################"
        target_size = (400, 400)
        # Background image to draw hand landmarks on
        # create a black image
        img = np.zeros((350, 700, 3), dtype=np.uint8)

        # background_img = cv2.imread("mod_background_black.jpg")
        background_img = img
        ######################################################################""

        #############################################################################
        # Empty background image
        background_img = cv2.resize(background_img.copy(), target_size)
        ###########################################################################"
        with mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        ) as hands:

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            # self.image.flags.writeable = True
            image = cv2.cvtColor(self.src, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                annotated_image = cv2.resize(background_img.copy(), target_size)
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        annotated_image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style(),
                    )

                    #############################################################

                    # Crop edges of webcam view to make square
                    (h, w, c) = annotated_image.shape
                    margin = (int(w) - int(h)) / 2
                    square_feed = [0, int(h), int(0 + margin), int(int(w) - margin)]
                    #                 y1            y2                x1            x2
                    square_roi = image[
                        square_feed[0] : square_feed[1], square_feed[2] : square_feed[3]
                    ]
                    # Resize for model input
                    input_size = 200
                    resized = cv2.resize(square_roi, (input_size, input_size))
                    # Flip horizontally for easier user interpretability
                    flip = cv2.flip(resized, 1)
                    # Copy image for model input
                    model_in = flip.copy()

                    # Format for model prediction
                    model_in = np.expand_dims(model_in, axis=0)
                    # Classify and print class to original (shown) image

                    # Predicting the image
                    predicted_class = model.predict(model_in)

                    # Get the index of the prediction
                    output = np.argmax(predicted_class)
                    self.letter_predict = list(key_dict.keys())[
                        list(key_dict.values()).index(output)
                    ]

                    self.calcul_percent(predicted_class, output)

                    ################################################################################
                    # Save the processed image
                    curr_time = round(time.time() * 1000)

                    self.landmarks = self.userName + str(curr_time) + ".jpg"
                    l = self.path + "/" + self.landmarks
                    cv2.imwrite(l, cv2.flip(annotated_image, 1))

                return True

    def calcul_percent(self, predicted_class, index):
        # Convert list of predictions to float at 2 decimal places
        predicted_probabilities = list(map("{:.2f}".format, predicted_class[0] * 100))

        self.percent = predicted_probabilities[index]

    def get_landmarks(self):
        return self.landmarks

    def get_percent(self):
        return self.percent

    def get_letterPredict(self):
        return self.letter_predict

    def get_imageUpload(self):
        return self.imgUpload
