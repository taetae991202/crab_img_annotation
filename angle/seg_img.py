import sys

import cv2
import glob

import numpy as np

path = '../../data/output'
seg_file_list = glob.glob(path + '/*.png')
print(seg_file_list)

dst = cv2.imread(seg_file_list[0], cv2.IMREAD_GRAYSCALE)

np.set_printoptions(threshold=sys.maxsize)
print(np.where(dst == 3))
print(dst[564, 1152])
print(dst.shape)
print(type(dst))
