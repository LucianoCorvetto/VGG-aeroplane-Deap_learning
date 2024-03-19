# import the necessary packages
from keras.utils import img_to_array
from keras.utils import load_img
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from numpy import expand_dims
from keras.applications.vgg16 import preprocess_input
from keras.models import Model

# from sklearn.linear_model import LogisticRegressions
# from sklearn.metrics import confusion_matrix
import mimetypes
import argparse
import imutils
import cv2
import os
# # define the base path to the input dataset and then use it to derive
# # the path to the images directory and annotation CSV file
# BASE_PATH = "dataset"
ImageAndGTPATH = "info/IOU.txt"
Test_IMAGES_PATH = "dataset/new_cropped_train_Images/10-27-2022 14-29-17-279.jpg"

# # Test_IMAGES_PATH = os.path.sep.join([BASE_PATH, "test_images"])
# print(Test_IMAGES_PATH,"kkkk")
# # Test_ANNOTS_PATH ="image10.xml"
# # Test_ANNOTS_PATH = os.path.sep.join([BASE_PATH, "test_annotations.csv"])
# # define the path to the base output directory
BASE_OUTPUT = "dataset"
TEST_IMAGES_PATH = os.path.sep.join([BASE_OUTPUT, "images"])
Ground_Truth_Path = os.path.sep.join([BASE_OUTPUT,"Airplanes.csv"])
BASE_OUTPUT = "output"
Output_test_path = os.path.sep.join([BASE_OUTPUT, "prediction_images"])
test_rows = open(Ground_Truth_Path).read().strip().split("\n")
dim = (224, 224)
for test_images in os.listdir(TEST_IMAGES_PATH):
    # print(test_images)
    test_images_pa = os.path.sep.join([TEST_IMAGES_PATH, test_images])

    for test_row in test_rows:
        test_row = test_row.split(",")
        (filename, startX, startY, endX, endY,label) = test_row
        # print(test_row)
        if test_images == filename:
            image = load_img(test_images_pa, target_size=(224, 224, 3))
            # image = img_to_array(image)
            # image = np.expand_dims(image, axis=0)
            # preds = model1.predict(image)[0]
            # (startX, startY, endX, endY) = preds
            # print(preds)
            image = cv2.imread(test_images_pa)
            image = imutils.resize(image )
            (h, w) = image.shape[:2]
            print(h,w)
            image = cv2.resize(image,dim)

            # print(startX,startY,endX,endY)
            if label == "Airplanes":
                xmin = int(int(endX) *(224/w))
                ymin = int(int(startX) * (224/h))
                xmax = int(int(endY) * (224/w))
                ymax = int(int(startY) * (224/h))
                print(xmin, ymin, xmax, ymax)
                cv2.rectangle(image, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 2)

            else:
                print("No Human")
        cv2.imwrite(Output_test_path + "/" + test_images, image)

        cv2.imwrite(Output_test_path + "/" + test_images, image)