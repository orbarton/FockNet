def create_ase_db(flat, position, num, ase_db_path):
  import numpy as np
  from ase import Atoms
  from schnetpack.data import ASEAtomsData

  positions = position
  atomic_numbers = num
  fock_matrices = flat
  property_list = [{'fock_matrix': fock_matrix} for fock_matrix in fock_matrices]

  # Create list of Atoms objects
  atoms_list = []
  for pos, nums in zip(positions, atomic_numbers):
    atoms = Atoms(positions=pos, numbers=nums)
    atoms_list.append(atoms)

  # Create ASEAtomsData database
  ase_db_path = ase_db_path
  new_dataset_one = ASEAtomsData.create(
    ase_db_path,
    distance_unit='Ang',
    property_unit_dict={'fock_matrix': 'unknown'}
  )

  # Add systems to the database
  new_dataset_one.add_systems(property_list, atoms_list)
