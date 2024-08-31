def getfockmatrices(overlap_matrix, nrgmat, orbcoeff, ranges):
  Fock = []
  for i in range(ranges):
    S = overlap_matrix[i]
    e = nrgmat[i]
    C = orbcoeff[i]
    C = C.T
    C1 = np.linalg.inv(C)
    F = S@C@e@C1
    Fock.append(np.array(F))
  np.save('fockmatrices_fixed.npy', Fock)
