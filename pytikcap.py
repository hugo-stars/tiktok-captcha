import cv2
import numpy as np
capurl='https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/3d_2385_2f2ed69300f749a56dafee039590f28e80ad1fde_1.jpg~tplv-b4yrtqhy5a-2.jpeg'
image = cv2.imread(capurl)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, threshold1=30, threshold2=100)
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
shapes = []
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    if len(approx) == number_of_sides_of_shape_to_match:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            shapes.append({'x': cx, 'y': cy, 'relative_time': 0})
print(shapes)
