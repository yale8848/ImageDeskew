#!/usr/bin/env python
# encoding: utf-8
'''
@author: Yale
@license: (C) Copyright Yale.
@contact: royal8848@163.com
@file: Test0.py
@time: 2018/1/15 10:03
@desc:
'''
import math
import cv2
import numpy as np

IMAGE_SRC="G:\\PIC\\dashu\\ff70c961987b4a03896d54ee8a506978.jpg"
IMAGE_DEST="G:\\PIC\\dashu\\b0.jpg"
IMAGE_ROT_DEST="G:\\PIC\\dashu\\_ff70c961987b4a03896d54ee8a506978.jpg"


def rotImage(srcImgOrg,angleD,path):
    print('angleD : %f' %angleD)
    size = srcImgOrg.shape
    centerPnt = (srcImgOrg.shape[1] / 2,srcImgOrg.shape[0] / 2)
    rotMat = cv2.getRotationMatrix2D(centerPnt,angleD,scale=1.);
    resultImg = cv2.warpAffine(srcImgOrg,rotMat,(size[1],size[0]),borderValue=(255,255,255));

    ret = cv2.imwrite(path,resultImg)

img = cv2.imread(IMAGE_SRC, 0)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
rotimg = img.copy()
img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 50, 150, apertureSize=3)#apertureSize between 3 and 7 in 边缘检测 其中较大的阈值2用于检测图像中明显的边缘，但一般情况下检测的效果不会那么完美，边缘检测出来是断断续续的。所以这时候用较小的第一个阈值用于将这些间断的边缘连接起来
count = 0
ctn = 0.0
angle = 0.0

positive=0.0
positive_count=0
negative=0.0
negative_count=0

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200,minLineLength=200,maxLineGap=20)

for x in range(0, len(lines)):
    for x1, y1, x2, y2 in lines[x]:
        print('(x1:%d,y1:%d)(x2:%d,y2:%d)' % (x1, y1, x2, y2))
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)
        xd = abs(x1 - x2)
        yd = abs(y1 - y2)
        if xd >= yd and yd != 0 and x1<500 and x2<500:
            print('@@(x1:%d,y1:%d)(x2:%d,y2:%d)' % (x1, y1, x2, y2))
            #cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)
            count += 1
            ant=np.arctan2(y2 - y1, x2 - x1)
            angle += ant
            print('angle tmp : %f' % ant)
            if ant > 0:
                positive_count += 1
                positive += angle
            else:
                negative += angle
                negative_count += 1




"""
lines1 = lines[:,0,:]#提取为二维

for x1,y1,x2,y2 in lines1[:]:
    xd = abs(x1-x2)
    yd = abs(y1-y2)

    if xd >= yd and yd!=0:
        print('@(x1:%d,y1:%d)(x2:%d,y2:%d)' % (x1,y1,x2,y2) )
       # td = (y2-y1) / (x2-x1)
       # tn = math.atan(td)
       # ctn+=tn
       # print('tn : %f' % tn)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 10)
        count+=1
        angle += np.arctan2(y2 - y1, x2 - x1)
        #print('angle : %f' % angle)

"""
print('(positive_count:%d,positive:%f)(negative_count:%d,negative:%f)' % (positive_count,positive,negative_count,negative) )
if positive_count>0 or negative_count>0:
    ag=0.0
    if positive_count>negative_count:
        ag = positive / positive_count
    else:
        ag = negative / negative_count

    rotImage(rotimg, ag, IMAGE_ROT_DEST)


"""
if count >0 :
    ag = angle/count
    rotImage(rotimg,ag,IMAGE_ROT_DEST)
    print('angle : %f' % ag)
"""


"""
lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)
if lines.size != 0:
    for line in lines[0]:
        rho = line[0]
        theta = line[1]
        print('theta : %f' % theta)
"""

cv2.imwrite(IMAGE_DEST,img)
#cv2.imshow('Canny', img)
#cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

