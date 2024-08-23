# -*- coding: utf-8 -*-
"""model_hyperparameters.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pg7gZNtErhMR7JHyBnxxXveoBfurtUOs
"""

def modelandhyperparameters(cutoff, n_atom_basis, n_interactions, n_out):
  cutoff = 5.
  n_atom_basis = 30

  pairwise_distance = spk.atomistic.PairwiseDistances() # calculates pairwise distances between atoms
  radial_basis = spk.nn.GaussianRBF(n_rbf=20, cutoff=cutoff)
  schnet = spk.representation.PaiNN(
    n_atom_basis=n_atom_basis,n_interactions=3,
    radial_basis=radial_basis,

    cutoff_fn=spk.nn.CosineCutoff(cutoff)
  )

  predfock = OutFock(n_in=schnet.n_atom_basis, n_out=1024, output_key='fock_matrix',n_layers=2)

  nnpot = spk.model.NeuralNetworkPotential(
    representation=schnet,
    input_modules=[pairwise_distance],
    output_modules=[predfock]
  )