def retrieveactual(actual, num):
  import numpy as np
  array = []
  for i in range(num):
    actually = np.array(np.load(actual, allow_pickle=True)[i]['fock_matrix'])
    array.append(actually)
  return np.array(array)
