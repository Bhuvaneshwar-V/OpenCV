import cv2

img = cv2.imread('Images\dog.jpg')

cv2.imshow('image', img)
cv2.waitKey(0)