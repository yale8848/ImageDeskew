import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('G:\\pic\\dashu\\0.jpg', cv2.IMREAD_GRAYSCALE)

def compute_skew(image):
    image = cv2.bitwise_not(image)
    height, width = image.shape

    edges = cv2.Canny(image, 150, 200, 3, 5)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 160,minLineLength=160,maxLineGap=5)
    lines1 = lines[:,0,:]#提取为二维
    llen=len(lines1)
    for x1,y1,x2,y2 in lines1[:]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imshow('Canny', img)
    return 20


def deskew(image, angle):
    image = cv2.bitwise_not(image)
    non_zero_pixels = cv2.findNonZero(image)
    center, wh, theta = cv2.minAreaRect(non_zero_pixels)

    root_mat = cv2.getRotationMatrix2D(center, angle, 1)
    rows, cols = image.shape
    rotated = cv2.warpAffine(image, root_mat, (cols, rows), flags=cv2.INTER_CUBIC)
    cv2.imwrite("G:\\pic\\dashu\\999.jpg", rotated)
    return cv2.getRectSubPix(rotated, (cols, rows), center)


deskewed_image = deskew(img.copy(), compute_skew(img))
cv2.waitKey(0)
cv2.destroyAllWindows()
