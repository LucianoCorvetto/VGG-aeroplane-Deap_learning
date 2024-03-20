import cv2
from PIL import ImageOps, Image
from keras import img_to_array
from keras import load_img
import os
BASE_PATH = 'dataset'
Train_IMAGES_PATH = os.path.sep.join([BASE_PATH, "images"])
resized_Image_PATH = os.path.sep.join([BASE_PATH, "resize_images"])
for image in os.listdir(Train_IMAGES_PATH):
# print(image)
    train_imagePath = os.path.sep.join([Train_IMAGES_PATH, image])
# to resize all the images to same size
    cropped_img =cv2.imread(train_imagePath)
    cropped_img =cv2.resize(cropped_img,(224,224))
    cv2.imwrite(resized_Image_PATH +"/"+ image ,cropped_img)