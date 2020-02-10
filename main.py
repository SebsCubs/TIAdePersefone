#Main routine execution for latin handwritten text processing
#Técnicas de inteligencia artificial: 2019-2
#Universidad Nacional de Colombia

#How to import packages:
#   import data_enhancement.rotation_span
#   data_enhancement.rotation__span
#either
#   from data_enhancement import rotation__span
#   rotation__span
#either
#   import data_enhancement.rotation__span
#   data_enhancement.rotation__span.printPrueba(1)

import numpy as np
from matplotlib import pyplot as plt
import cv2
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
from data_enhancement import rotation__span
####################_Main routine_##################################

img = cv2.imread('test_data/asta_ascendente/l/0.tif')
rotation__span.rotation_create(img,'test_data/asta_ascendente/l')
rotation__span.warp_create(img)