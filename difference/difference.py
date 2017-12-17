import cv2 
import numpy as np 


image1 = cv2.imread("image-horizontal.jpg", 0)
# image1_grey = 

image2 = cv2.imread("image-vertical.jpg", 0)

result = cv2.absdiff(image1, image2)

print result.sum()
result = cv2.resize(result, (500, 500))
cv2.imshow("R", result)
cv2.waitKey(0)
cv2.destroyAllWindows()