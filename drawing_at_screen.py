import cv2 as cv
import numpy as np

# Writing an image
# blank = np.zeros((512, 512, 3), dtype='uint8')
# 
# blank = cv.rectangle(blank, (200, 150), (400, 350), (255,255,255), thickness=cv.FILLED)
# blank[200:220, 350:380] = 200,200,0
# 
# blank[200:220, 220:250] = 200,200,0
# 
# 
# cv.imshow('Blue', blank)
# 
# cv.waitKey(0)



# Writing edges
img = cv.imread('images/snake.jpg')

# Bluring didn't worked
# img = cv.GaussianBlur(img, ksize=1, borderType=1, sigmaX=1.0)

# Edge worked
edge = cv.Canny(img, 125, 175)

# Dilate worked
dilate = cv.dilate(edge, (5,5), iterations=2)

cv.imshow('Dilated', dilate)

cv.waitKey(0)