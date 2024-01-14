import cv2 as cv

img = cv.imread('images/snake.jpg', cv.IMREAD_GRAYSCALE)

cv.imshow('snake', img)

cv.waitKey(0)