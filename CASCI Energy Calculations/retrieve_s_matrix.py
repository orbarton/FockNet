def retrieveSmatrix(index, upper):
  import numpy as np
  np.load('overlap_matrices_open.npy')
  array = []
  for i in index[0:upper]:
    S = np.load('overlap_matrices_open.npy')[i]
    array.append(S)
  return array
