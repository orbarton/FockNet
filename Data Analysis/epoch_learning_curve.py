def test_overfitting(index, upper, title, validations, trains):
  import numpy as np
  import matplotlib.pyplot as plt
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
