# -*- coding: utf-8 -*-
"""epoch_learning_curve.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CIJ9LeKYWqP8gEidHXDTSqiwcgxQ8IGu
"""

first = 'firstfoldone.npz'
second = 'secondfoldone.npz'
third = 'thirdfoldone.npz'
fourth = 'fourthfoldone.npz'
fifth = 'fifthfoldone.npz'
runs = [first, second, third, fourth, fifth]

validations = []
trains = []
for run in runs:
  validation = (np.load(run)['validation_arrays']).flatten()
  validations.append(validation)
  train = (np.load(run)['train_arrays']).flatten()
  trains.append(train)

def test_overfitting(index, upper, title):
  epochs = np.arange(0,len(trains[index]))
  plt.figure(figsize=(10, 6))
  plt.plot(epochs, trains[index], label='Train')
  plt.plot(epochs, validations[index], label='Validation')
  plt.xlabel('Epochs')
  plt.ylabel('Loss')
  plt.title(title)
  plt.ylim(0, upper)

  min_val_idx = np.argmin(validations[index])
  min_train_idx = np.argmin(trains[index])
  min_val_epoch = epochs[min_val_idx]
  min_train_epoch = epochs[min_train_idx]
  min_val_loss = validations[index][min_val_idx]
  min_train_loss = trains[index][min_train_idx]

  print(f"Validation - Min Index: {min_val_idx}, Epoch: {min_val_epoch}, Loss: {min_val_loss}")
  print(f"Training - Min Index: {min_train_idx}, Epoch: {min_train_epoch}, Loss: {min_train_loss}")

  plt.annotate(f'Min Val:{min_val_loss:.2e}',
               xy = (min_val_epoch, min_val_loss),
               xytext = (min_val_epoch - 6, min_val_loss - 3e-4),
               arrowprops = dict(facecolor = 'red', shrink = 0.05)
               )

  plt.annotate(f'Min Train:{min_train_loss:.2e}',
               xy = (min_train_epoch, min_train_loss),
               xytext = (min_train_epoch - 6, min_train_loss + 3e-4),
               arrowprops = dict(facecolor = 'red', shrink = 0.05)
               )

  plt.legend()

  plt.show()