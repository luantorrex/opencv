import cv2 as cv

# Reading images
# img = cv.imread('images/snake.jpg', cv.IMREAD_GRAYSCALE)
# cv.imshow('snake', img)



# Reading videos
capture = cv.VideoCapture('videos/animation.mp4')

while True:
    isTrue, frame=capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)