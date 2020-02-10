#Python module add functions here to import on main

import numpy as np
import cv2
import math

def rotation_create (image,route):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    #45 degrees clockwise
    rot_mat = cv2.getRotationMatrix2D(image_center, 45, 1.0)
    resultCW = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    cv2.imwrite(resultCW,route)
    
    
    
    #45 degrees counterclokwise
    rot_mat = cv2.getRotationMatrix2D(image_center, -45, 1.0)
    resultCCW = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    cv2.imwrite('test_data/asta_ascendente/l', resultCCW)

    print("Rotadito")

def warp_create (img):
    #Here to receive one image and create with a vertical wrapping
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    rows, cols = img.shape

    #####################
    # Vertical wave

    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
            offset_y = 0
            if j+offset_x < rows:
                img_output[i,j] = img[i,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0

    cv2.imshow('Input', img)
    cv2.imshow('Vertical wave', img_output)
    
    print("Warppeadito")

