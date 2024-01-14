import cv2 as cv
import numpy as np

# img = cv.imread('images/snake.jpg')
blank = np.zeros((512, 512, 3), dtype='uint8')

blank = cv.rectangle(blank, (200, 150), (400, 350), (255,255,255), thickness=cv.FILLED)
blank[200:220, 350:380] = 200,200,0

blank[200:220, 220:250] = 200,200,0


cv.imshow('Blue', blank)

cv.waitKey(0)