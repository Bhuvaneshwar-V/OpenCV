import cv2
import numpy as np

# creating black image using numpy
img = np.zeros((512,512, 3), np.uint8)
print(img.shape)


# drawing a line on the image
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]),(0, 255, 0), 3)


# drawing an rectangle on the image
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)


# drawing the circle on the image
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)


# Adding text in the image
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_ITALIC, 1, (255, 0 , 0), 2)


cv2.imshow('line_image', img)
cv2.waitKey(0)