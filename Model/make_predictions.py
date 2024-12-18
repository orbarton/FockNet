# -*- coding: utf-8 -*-
"""make_predictions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dei40yzhMAOBFDEHOsQ4GWf0qC-fnUT0
"""

def make_predictions(model, dataloader, fockmatrixtutone):
  from ase import Atoms
  import torch
  import os
  import schnetpack as spk
  import schnetpack.transform as trn
  import numpy as np

  # Set device
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

  # Load model
  model_path = os.path.join(fockmatrixtutone, model)
  best_model = torch.load(model_path, map_location=device)
  best_model.eval()  # Set the model to evaluation mode

  # Set up converter
  converter = spk.interfaces.AtomsConverter(
      neighbor_list=trn.ASENeighborList(cutoff=5.0), dtype=torch.float32, device=device
  )

  # Prepare dataset (replace 'custom_data.test_dataset' with your actual dataset)
  dataset = dataloader
  # Container for results
  all_results = []

  # Loop over all data points in the dataset
  for structure in dataset:
      # Create an Atoms object from the dataset
      atoms = Atoms(
        numbers=structure[spk.properties.Z],
        positions=structure[spk.properties.R]
      )

      # Convert atoms to SchNetPack inputs and perform prediction
      inputs = converter(atoms)
      with torch.no_grad():  # Disable gradient calculation for inference
        results = best_model(inputs)

      # Collect results
      all_results.append(results['fock_matrix'].cpu().numpy())

      # Convert list of results to a numpy array for further processing
  all_results = np.array(all_results)
  return all_results
