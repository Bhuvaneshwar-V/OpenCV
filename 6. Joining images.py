import cv2
import numpy as np

img = cv2.imread('Images\dog.jpg')

# horizontal stack
hor_img = np.hstack((img, img))

# vertical stack
ver_img = np.vstack((img, img))

cv2.imshow('horizontal_image', hor_img)
cv2.imshow('vertical_image', ver_img)

cv2.waitKey(0)