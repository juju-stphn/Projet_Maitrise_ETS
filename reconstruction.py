import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import sys

# Point 1 : Calcul des cartes de profondeur individuelles pour chaque paire d'images
def calculate_depth_maps():
    images = []
    for i in range(10):
        img = cv2.imread('/home/pi/Projet/3.2.2/image_transfert{}_undistorted.png'.format(i), 0)
        images.append(img)

    # Détection des keypoints et calcul des descripteurs
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints = []
    descriptors = []
    for img in images:
        kp, des = sift.detectAndCompute(img, None)
        keypoints.append(kp)
        descriptors.append(des)

    # Calcul des correspondances entre paires d'images
    matcher = cv2.BFMatcher()
    matches = []
    for i in range(9):
        matches.append(matcher.match(descriptors[i], descriptors[i+1]))


    # Calcul des cartes de profondeur par paires de photographie
    depth_maps = []
    for i in range(9):
        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=5)
        disp = stereo.compute(images[i], images[i+1]).astype(np.float32)/16.0
        disp = stereo.compute(matches[i], matches[i+1]).astype(np.float32)/16.0

        depth_maps.append(disp)
        
    return depth_maps


# Point 2 : Alignement des cartes de profondeur
def align_depth_maps(depth_maps, displacement):

    num_images = len(depth_maps)
    height, width = depth_maps[0].shape

    # Initialisation de la carte de profondeur fusionnée
    merged_depth_map = np.zeros((height, width), dtype=np.float32)

    # Calcul du le décalage en pixels
    displacement_pixels = int(displacement / (width / num_images))

    # Fusion des cartes de profondeur en fonction du decalage en pixels
    for i in range(num_images):
        depth_map = depth_maps[i]
        shifted_depth_map = np.roll(depth_map, displacement_pixels * i, axis=1)
        merged_depth_map += shifted_depth_map

    return merged_depth_map




