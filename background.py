import cv2 as cv

cap= cv.VideoCapture(0)


while cap.isOpened():
    ret, background = cap.read()
    if ret:
        cv.imshow("image",background)
        if cv.waitKey(5)==ord('q'):
            cv.imwrite("image.jpg",background)
            break

cap.release()
cv.destroyAllWindows()

