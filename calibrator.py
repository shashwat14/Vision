# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:01:56 2016

@author: Shashwat
"""

import cv2
import numpy as np

WIDTH = 8
HEIGHT = 6
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((WIDTH*HEIGHT,3), np.float32)
objp[:,:2] = np.mgrid[0:WIDTH,0:HEIGHT].T.reshape(-1,2)

objpoints = []
imgpoints = []


cap = cv2.VideoCapture(0)

idx = 1
while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (8,6),None)
    try:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        img = cv2.drawChessboardCorners(img, (8,6), corners2,ret)
    except:
        checkers = img
            
    
    cv2.imshow("frame",img)  
    ch = cv2.waitKey(30)
    
    if ch == ord('q'):
        break
    elif ch == ord('c'):
        if ret:
            objpoints.append(objp)
            
            imgpoints.append(corners2)
            print idx
            idx+=1
        else:
            print "Chessboard not found. Select more images."
            
            
try:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
except:
    print "something went wrong.."


cv2.destroyAllWindows()
cap.release()