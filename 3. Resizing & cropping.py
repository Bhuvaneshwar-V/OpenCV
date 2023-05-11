# Resizing the image
import cv2

img = cv2.imread('Images/dog.jpg')
print(img.shape)

resize_img = cv2.resize(img, (150, 125))
print(resize_img.shape)

cv2.imshow('image', img)
cv2.imshow('resized_image', resize_img)


# Cropping the image
cropped_img = img[0:130, 50:200]

cv2.imshow('cropped_image', cropped_img)
cv2.waitKey(0)