# -*- coding: utf-8 -*-
"""initialise_output.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1usMqa8OtX5p8lOHEu_mZBzWwOpCWi2Kz
"""

def initialise_modeloutput():
 output_fock = spk.task.ModelOutput(
    name='fock_matrix',
    loss_fn=lambda pred, targets: custom_loss(pred, targets, mdimension, batch_size),
    loss_weight=1.,
    metrics={}
 )