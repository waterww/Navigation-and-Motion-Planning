#! /usr/bin/env python
# wumiao, 2019-3-4

import numpy as np

def get_distance(data):
    """ transform unit16 data type to int32, and transform decimal to binary number,
    get the last 11 digit number to decimal number, which represents the depth of
    each pixel"""
    [rows,cols] = data.shape
    distance = np.ones((rows,cols))
    data = data.astype(np.int32)
    
    for i in range(rows):
        for j in range(cols):
            element = data[i,j]

            bin_element = '{:016b}'.format(element)
            bin_distance = bin_element[-11:]
            distance[i,j] = int(bin_distance,2)
    
    return distance
    
def coor_trans(matrix):
    """transform camera coordinates to real world coordinates"""
    camera_factor = 1000
    camera_cx = 314.864
    camera_cy = 242.652
    camera_fx = 621.202
    camera_fy = 620.866
    [rows,cols] = matrix.shape
    print rows,cols
    coor = np.ones((rows, cols, 3))
    for i in np.arange(rows):
        for j in np.arange(cols):
            z = matrix[i,j]/camera_factor
            coor[i,j,0] = z
            x = (j-camera_cx)*z/camera_fx
            coor[i,j,1] = x
            y = (i-camera_cy)*z/camera_fy
            coor[i,j,2] = y
    
    return coor
            
            

    
 

