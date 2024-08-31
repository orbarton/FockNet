# -*- coding: utf-8 -*-
def getC(result, S, num):
  from scipy.linalg import eigh
  import numpy as np
  Cmatrices = []
  for i in range(num):
    eigenvalues, C = eigh(result[i].reshape(32,32), S[i].reshape(32,32))
    Cmatrices.append(C)
  return np.array(Cmatrices)
