# -*- coding: utf-8 -*-
import numpy as np
#Here matrixdimension should be the square root of the matrix total size, or the size of either the x or y dimension
def phase_correct(file, matrixdimension):
  #Load the file pre-correction
  correction = np.load(file)
  #Assign reference for phase correction
  reference = correction[0]
  #Phase correct
  for i in range(1,1000):
    for j in range(matrixdimension):
      matrix = correction[i][j]
      if np.dot(reference[j], matrix) < 0:
        correction[i][j] = correction[i][j]*-1
  np.save('phase_corrected.npy', correction)
