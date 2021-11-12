import cv2.cv2 as cv2

"""
    Resizing an image
"""

img = cv2.imread("images/fame1.jpg")
print(img.shape)
imgResize = cv2.resize(img, (224, 224))
imgResize2 = cv2.resize(img, (1024, 1024))
cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Increase Size", imgResize2)
print(imgResize.shape)
cv2.waitKey(0)

