from __future__ import print_function

import cv2
import numpy as np
import os
import glob

# Calibration des images prises par la camera en fonction de leur taille
def calibration(nb_pics):
    for i in range (nb_pics):
        img_test = cv2.imread(f'/home/pi/Projet/3.2.2/image_transfert{i}.png')
        size = img_test.shape
    
        # Pour des images de 800 x 600        
        if size == (600, 800, 3):
            with open("settings/mtx_800x600.txt") as f:
                mtx = np.array(list((map(lambda x:list(map(lambda x:float(x), x.strip().split(' '))),f.read().split('\n')))))
                
            with open("settings/dist_800x600.txt") as f:
                dist = np.array(list((map(lambda x:list(map(lambda x:float(x), x.strip().split(' '))),f.read().split('\n')))))

            h,w = img_test.shape[:2]
            newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
            
        # Pour des images de 1280 x 720
        elif size == (720, 1280, 3):
            with open("settings/mtx_1280x720.txt") as f:
                mtx = np.array(list((map(lambda x:list(map(lambda x:float(x), x.strip().split(' '))),f.read().split('\n')))))
                
            with open("settings/dist_1280x720.txt") as f:
                dist = np.array(list((map(lambda x:list(map(lambda x:float(x), x.strip().split(' '))),f.read().split('\n')))))
        
            h,w = img_test.shape[:2]
            newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        # Pour des images de 1920 x 1080
        elif size == (1080, 1920, 3):
            with open("settings/mtx_1920x1080.txt") as f:
                mtx = np.array(list((map(lambda x:list(map(lambda x:float(x), x.strip().split(' '))),f.read().split('\n')))))
                
            with open("settings/dist_1920x1080.txt") as f:
                dist = np.array(list((map(lambda x:list(map(lambda x:float(x), x.strip().split(' '))),f.read().split('\n')))))

            h,w = img_test.shape[:2]
            newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))                    
                
        # Calibration et sauvegarde des images
        outfile = os.path.join("/home/pi/Projet/3.2.2/", f'image_transfert{i}' + '_undistorted.png')
        dst = cv2.undistort(img_test, mtx, dist, None, newcameramtx)

        x, y, w, h = roi
        
        dst = dst[y:y+h, x:x+w]

        print('Undistorted image written to: %s' % outfile)
        cv2.imwrite(outfile, dst)

