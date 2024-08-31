def custom_test_loss(pred, targets, mdimension):
  import numpy as np
  pred = np.reshape(pred, (-1, mdimension, mdimension))
  targets = np.reshape(targets, (-1, mdimension, mdimension))

  loss = 0
  for i in range(pred.shape[0]):
        squared_diff = np.square(targets[i] - pred[i])
        loss += np.sum(squared_diff) / (mdimension * mdimension)
  return loss/pred.shape[0]
