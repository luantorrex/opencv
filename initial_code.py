import cv2 as cv

# Reading images
# img = cv.imread('images/snake.jpg', cv.IMREAD_GRAYSCALE)
# cv.imshow('snake', img)



# Reading videos
# capture = cv.VideoCapture('videos/animation.mp4')
# 
# while True:
#     isTrue, frame=capture.read()
#     cv.imshow('Video', frame)
# 
#     if cv.waitKey(20) and 0xFF == ord('d'):
#         break
# 
# capture.release()



# Resizing an image
# img = cv.imread('images/snake.jpg', cv.IMREAD_UNCHANGED)
# print('Original Dimensions:', img.shape)
# 
# scale_percent = 60
# 
# width = int(img.shape[1] * scale_percent / 100)
# heigth = int(img.shape[0] * scale_percent / 100)
# dimension = (width, heigth)
# 
# img_resized = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
# print('Resized dimensions: ', img_resized.shape)
# 
# cv.imshow('Resized image', img_resized)
# cv.waitKey(0)
# cv.destroyAllWindows()


# Resizing videos
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('videos/animation.mp4')

while True:
    isTrue, frame=capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('VideoResized', frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()