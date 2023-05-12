import cv2
import numpy as np

img = cv2.imread('Images/cards.jpg')

# width & height of the card
width, height = 138, 195

# co-ordinate points of particular card
pts1 = np.float32([[289, 48], [427, 86], [235, 241], [376, 281]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('image', img)
cv2.imshow('image_output', img_output)
cv2.waitKey(0)