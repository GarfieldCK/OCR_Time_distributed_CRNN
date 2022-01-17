import cv2
import numpy as np

#im_path = "C:/Users/acer/Desktop/Mini_hackathon_workingspace/SUPERAI2_HACK1_datasets/train_data/0123456789/"


image = cv2.imread("C:/Users/acer/Desktop/Mini_hackathon_workingspace/SUPERAI2_HACK1_datasets/train_data_5digits_9476/51691.jpg") 

# Image preprocessing : 
#image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

res,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) #threshold 
#kernel = cv2.getStructuringElement(cv2.MORPH_OPEN,(3,3)) 

#dilated = cv2.dilate(thresh,kernel,iterations = 3) 

#print(dilated.shape)

cv2.imshow('windows', ~thresh)
cv2.waitKey(0)
