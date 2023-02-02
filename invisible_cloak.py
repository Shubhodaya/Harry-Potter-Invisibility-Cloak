import cv2 as cv
import numpy as np

cap= cv.VideoCapture(0)
background= cv.imread('./image.jpg')


while cap.isOpened():

    ret, current_frame = cap.read()
    if ret:
        hsv_frame = cv.cvtColor(current_frame, cv.COLOR_BGR2HSV)

        l_red = np.array([0,120,70])
        u_red = np.array([10,255,255])
        mask1 = cv.inRange(hsv_frame,l_red,u_red)

        l_red = np.array([170,120,70])
        u_red = np.array([180,255,255])
        mask2 = cv.inRange(hsv_frame,l_red,u_red)

        red_mask= mask1+mask2

        red_mask=cv.morphologyEx(red_mask, cv.MORPH_OPEN, np.ones((3,3),np.uint8), iterations=10)
        red_mask=cv.morphologyEx(red_mask, cv.MORPH_DILATE, np.ones((3,3),np.uint8), iterations=1)


        part1 = cv.bitwise_and(background,background, mask= red_mask)

        red_free = cv.bitwise_not(red_mask)

        part2= cv.bitwise_and(current_frame,current_frame,mask=red_free)


        cv.imshow("red mask",part1+part2)
        if cv.waitKey(5)==ord('q'):
            break

cap.release()
cv.destroyAllWindows()