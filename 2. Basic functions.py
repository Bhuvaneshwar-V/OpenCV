# Gray Image

import cv2

img = cv2.imread('Images\dog.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray_image', gray_img)


# Blur Image
blur_img = cv2.GaussianBlur(gray_img, (3,3), 0)

cv2.imshow('blur_image', blur_img)


# Edge detector
canny_img = cv2.Canny(img, 100, 150)

cv2.imshow('canny_image', canny_img)


# Dilation - increase the thickness of the canny image 
import numpy as np

kernel = np.ones((3, 3), np.uint8)
dilate_img = cv2.dilate(canny_img, kernel, iterations = 1)

cv2.imshow('dilate_image', dilate_img)


# Erosion
eroded_img = cv2.erode(dilate_img, kernel, iterations = 1)

cv2.imshow('eroded_image', eroded_img)
cv2.waitKey(0)