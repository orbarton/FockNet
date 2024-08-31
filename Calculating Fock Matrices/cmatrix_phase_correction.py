from google.colab import files
uploaded = files.upload()

import numpy as np
def phase_correct(file, matrixdimension):

  correction = np.load(file)

  reference = correction[0]

  for i in range(1,1000):
    for j in range(105):
      matrix = correction[i][j]
      if np.dot(reference[j], matrix) < 0:
        correction[i][j] = correction[i][j]*-1
  np.save('phase_corrected.npy', correction)
