# -*- coding: utf-8 -*-
#Use for setting the model output size, along with other hyperparameters
def modelandhyperparameters(cutoff,
                            n_atom_basis,
                            n_interactions,
                            n_out,
                            initial_lr,
                            lr_factor,
                            lr_patience,
                            lr_threshold,
                            OutFock,
                            AtomisticTask,
                            custom_loss):
  import torch.nn as nn
  import schnetpack as spk
  import torch
  cutoff = cutoff
  n_atom_basis = n_atom_basis

  pairwise_distance = spk.atomistic.PairwiseDistances() # calculates pairwise distances between atoms
  radial_basis = spk.nn.GaussianRBF(n_rbf=20, cutoff=cutoff)
  schnet = spk.representation.PaiNN(
    n_atom_basis=n_atom_basis,n_interactions=n_interactions,
    radial_basis=radial_basis,

    cutoff_fn=spk.nn.CosineCutoff(cutoff)
  )

  predfock = OutFock(n_in=schnet.n_atom_basis, n_out=n_out, output_key='fock_matrix',n_layers=2)

  nnpot = spk.model.NeuralNetworkPotential(
    representation=schnet,
    input_modules=[pairwise_distance],
    output_modules=[predfock]
  )
  output_fock = spk.task.ModelOutput(
    name='fock_matrix',
    loss_fn=lambda pred, targets: custom_loss(pred, targets, mdimension, batch_size),
    loss_weight=1.,
    metrics={}
 )
  task = AtomisticTask(
    model=nnpot,
    outputs=[output_fock],
    optimizer_cls=torch.optim.Adam,
    optimizer_args={"lr": initial_lr},
    scheduler_cls=torch.optim.lr_scheduler.ReduceLROnPlateau,
    scheduler_args={"threshold":lr_threshold,"patience": lr_patience, "factor":lr_factor},
    scheduler_monitor="val_loss"
  )
  return task
