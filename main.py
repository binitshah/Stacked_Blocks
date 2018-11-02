import cv2
import numpy as np
import matplotlib.pyplot as plt

def displayImage(image, title="Untitled"):
    plt.imshow(image)
    plt.show()

def main():
    pic = "stacked_blocks.png"
    image = cv2.imread(pic)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    displayImage(image, "Raw")
    
    green_lower = (36, 0, 0)
    green_upper = (70, 255,255)
    image_green_mask = cv2.inRange(hsv_image, green_lower, green_upper)
    green_image = cv2.bitwise_and(image, image, mask=image_green_mask)
    displayImage(green_image, "Green")

    yellow_lower = (15, 0, 0)
    yellow_upper = (36, 255, 255)
    image_yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    yellow_image = cv2.bitwise_and(image, image, mask=image_yellow_mask)
    displayImage(yellow_image, "Yellow")

    blue_lower = (105, 0, 0)
    blue_upper = (132, 255, 255)
    image_blue_mask = cv2.inRange(hsv_image, blue_lower, blue_upper)
    blue_image = cv2.bitwise_and(image, image, mask=image_blue_mask)
    displayImage(blue_image, "Blue")

    purple_lower = (138, 0, 0)
    purple_upper = (160, 255, 255)
    image_purple_mask = cv2.inRange(hsv_image, purple_lower, purple_upper)
    purple_image = cv2.bitwise_and(image, image, mask=image_purple_mask)
    displayImage(purple_image, "Purple")

    # red_lower = (1, 0, 0)
    # red_upper = (10, 255, 255)
    # image_red_mask = cv2.inRange(hsv_image, red_lower, red_upper)
    # red_image = cv2.bitwise_and(image, image, mask=image_red_mask)
    # displayImage(red_image, "Red")

    # all_image = cv2.bitwise_or(cv2.bitwise_or(green_image, yellow_image), cv2.bitwise_or(cv2.bitwise_or(blue_image, purple_image), red_image))
    # displayImage(all_image, "All")

    # # gaussian_image = cv2.GaussianBlur(green_image, (5, 5), 0)
    # squares = []
    # eroded_image = cv2.erode(green_image, None)
    # displayImage(eroded_image, "Eroded")
    # canny_image = cv2.Canny(eroded_image, 100, 200, apertureSize=5)
    # displayImage(canny_image, "Canny")
    # contour_image, contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contour_draw_image = cv2.drawContours(eroded_image, contours, -1, (255,255,255), 1)
    # displayImage(contour_draw_image, "Contour")

    # new_contours = []
    # for contour in contours:
    #     contour_length = cv2.arcLength(contour, True)
    #     print(contour_length)
    #     new_contour = cv2.approxPolyDP(contour, 0.02 * contour_length, True)
    #     new_contours.append(new_contour)

    # new_contour_draw_image = cv2.drawContours(eroded_image, new_contours, -1, (255,255,255), 1)
    # displayImage(new_contour_draw_image, "New Contour")

    # # for gray in cv2.split(green_image):
    # #     for threshold in range(0, 255, 26):
    # #         if threshold == 0:

    # # for gray in cv2.split(green_image):
    # #     for thrs in range(0, 255, 26):
    # #         if thrs == 0:
    # #             bin = cv2.Canny(gray, 0, 50, apertureSize=5)
    # #             displayImage(bin, "1st")
    # #             bin = cv2.dilate(bin, None)
    # #             displayImage(bin, "2st")
    # #         else:
    # #             _retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)

    # #         bin, contours, _hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # #         for cnt in contours:
    # #             cnt_len = cv2.arcLength(cnt, True)
    # #             cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
    # #             if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
    # #                 cnt = cnt.reshape(-1, 2)
    # #                 max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
    # #                 if max_cos < 0.1:
    # #                     squares.append(cnt)

    # cv2.destroyAllWindows()

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

if __name__ == '__main__':
    main()