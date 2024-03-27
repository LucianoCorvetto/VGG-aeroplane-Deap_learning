# import the necessary packages
import tensorflow as tf
from tensorflow import keras
from keras.utils import img_to_array
from keras.utils import load_img
from keras.models import load_model
import numpy as np
import mimetypes

import argparse
import imutils
import cv2
import os
IMAGES_PATH ="airplane.jpeg"
FILE_PATH = "output/tet_predict.txt"
# MODEL = open( "output/detector.h5").read()
ANNOTS_PATH = "dataset/Airplanes.csv"
dim = (224, 224)

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image/text file of image filenames")
# args = vars(ap.parse_args())
# determine the input file type, but assume that we're working with
# single input image
filetype = mimetypes.guess_type(FILE_PATH)[0]
imagePaths = open(ANNOTS_PATH).read().strip().split("\n")
# if the file type is a text file, then we need to process *multiple*
# images
# if "text/plain" == filetype:
	# load the filenames in our testing file and initialize our list
	# of image paths
	# filenames = open(ANNOTS_PATH).read().strip().split("\n")
	# imagePaths = []
	# loop over the filenames
	# for f in filenames:
		# construct the full path to the image filename and then
		# update our image paths list
		# p = os.path.sep.join([IMAGES_PATH, f])
		# imagePaths.append(p)
# load our trained bounding box regressor from disk
# print("[INFO] loading object detector...")
model = load_model( "output/detector.h5")
# loop over the images that we'll be testing using our bounding box
# regression model
for imagePath in imagePaths:
    # load the input image (in Keras format) from disk and preprocess
    # it, scaling the pixel intensities to the range [0, 1]
    image = load_img(imagePath, target_size=(224, 224))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    # make bounding box predictions on the input image
    preds = model.predict(image)[0]
    (startX, startY, endX, endY) = preds
    print(preds)
    # load the input image (in OpenCV format), resize it such that it
    # fits on our screen, and grab its dimensions
    image = cv2.imread(imagePath)
    image = imutils.resize(image)
    (h, w) = image.shape[:2]
    print(h,w)
    # image = cv2.resize(image, dim)
    # scale the predicted bounding box coordinates based on the image
    # dimensions
    startX = int(startX*w)
    startY = int(startY*h)
    endX = int(endX *w)
    endY = int(endY *h)
    print(startX,startY,endX,endY)
    # draw the predicted bounding box on the image
    cv2.rectangle(image, (startX, startY), (endX, endY),
                  (0, 255, 0), 2)
    # show the output image
    cv2.imshow("Output", image)
    cv2.waitKey(0)