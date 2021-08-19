import cv2 as cv

# # Reading images
# img = cv.imread(r'C:\Users\monta\Desktop\Opencv\photos\ax7.jpg')
# cv.imshow('ali', img)
# cv.waitKey(0)


def rescaleFrame(Frame, scale=0.25):

    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)

    dimensions = (width, height)
    return cv.resize(Frame, dimensions, interpolation=cv.INTER_AREA)

# change Resolution
#!!! only works with live Videos


# Reading videos
capture = cv.VideoCapture(r'C:\Users\monta\Desktop\Opencv\videos\v1.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
