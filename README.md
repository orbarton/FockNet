# FockNet

This repository details the code used for the FockNet project

The code detailed here will only work for the case where we have a 100 sized dataset, for the sake of brevity.

These instructions are for use in a Jupyter Notebook, but can be easily adapted for command line usage.

Another note is that generating the data is not possible without using a Unix-Bash environment, for which the organisation's HPC cluster was used, however, no tests have been done on a local system, but instructions will still be given in the tutorial notebook.

For this case, all data is going to be provided that is necessary. On top of this, if any user of this code is curious about completing the calculations (the only part completed on the HPC cluster) then they are welcome to contact me for further information at obarton.chemistry@gmail.com

The instructions also help to follow along with the tutorial notebook on Google Colab here:

As an alternative option, here is a Jupyter Notebook with all the code shown:

**First Step - Setup** :
- !git clone https://github.com/orbarton/FockNet.git
- !pip install -r requirements.txt

If installing the requirements doesn't work, which it does not on Colab due to issues with installing packages, try instead

- !pip install h5py
- !pip install schnetpack
- !pip install ase
- !pip install TensorBoard

**Second Step - Splitting Files**
- %cd /content/FockNet/Splitting Files/
- from write_5fold_splitting_files import make_5_fold_split_files
- %cd /content
- make_5_fold_split_files(100)

**Third Step - Import Modules**

- %cd /content/FockNet/Model
- from model_prequisites import model_prereqs
- from create_database_model import create_ase_db
- from custom_atomistic_task import AtomisticTask
- from datafortraining import modeldata
- from make_predictions import make_predictions
- from model_hyperparameters import modelandhyperparameters
- from model_loss import custom_loss
- from modeltraining import training
- from output_module import OutFock
- %cd /content/FockNet/Data Analysis
- from get_event_files import get_event_files
- %cd /content

**Fourth Step - Run the Model for the Fock Matrix**
- fockmatrixtutone = model_prereqs()
- flat = np.load('FockNet/Data for Tutorial/fock_matrices_reactant.npy')
- position = np.load('FockNet/Data for Tutorial/positions.npy')
- num = np.load('FockNet/Data for Tutorial/atomic_numbers.npy')
- create_ase_db(flat, position, num, 'flat.db')
- data=100
- mdimension = 32
- n_out = 32**2
- batch_size = 16
- cutoff = 5.
- n_atom_basis = 30
- n_interactions = 3
- n_out = 32**2
- initial_lr = 1e-4
- lr_factor = 0.8
- lr_patience = 3
- lr_threshold = 1e-3
- task = modelandhyperparameters(cutoff, n_atom_basis,
                                  n_interactions, n_out, initial_lr, lr_factor,
                                  lr_patience, lr_threshold, OutFock, AtomisticTask,
                                  custom_loss, mdimension, batch_size)
- custom_data_one = modeldata('flat.db', 'splittingfold1.npz', data, fockmatrixtutone)
- training(custom_data_one, 'best_inference_model_alphafoldone', 'alphaone', fockmatrixtutone, task, custom_loss)

**Fifth Step - Using the Trained Model to Make Predictions**

- resultsone = make_predictions("best_inference_model_alphafoldone", custom_data_one.test_dataset, fockmatrixtutone)
- actualone = custom_data_one.test_dataset
- np.save('results_firstfoldone.npy', resultsone)
- np.save('actualone.npy', actualone)

**Sixth Step - Save Hyperparameters and Logged Training Data**
- get_event_files('fockmatrixtutone/alphaone/version_0', 'trvalparams', parameters)

**Seventh Step - Repeat Steps for Prediction and Logging of S Matrix**
- ess = np.load('FockNet/Data for Tutorial/overlap_matrices_reactant.npy')
- create_ase_db(ess, position, num, 'ess.db')
- custom_data_s = modeldata('ess.db', 'splittingfold1.npz', data, fockmatrixtutone)
- training(custom_data_s, 'best_inference_model_alphafoldess', 'alphaess', fockmatrixtutone, task, custom_loss)
- get_event_files('fockmatrixtutone/alphaess/version_1', 'strvalparams.npz', parameters)
- resultsess = make_predictions("best_inference_model_alphafoldess", custom_data_s.test_dataset, fockmatrixtutone)
- actualess = custom_data_s.test_dataset
- np.save('results_essone.npy', resultsess)
- np.save('actualess.npy', actualess)

**Eighth Step - Analysing the Data**

This step is best referred to on the Google Colab notebooks, as there are more in-depth instructions owing to the more verbose nature of a notebook.

**Ninth Step - Preparing for the Calculations**

- %cd /content/FockNet/CASCI Energy Calculations
- from calculate_c_matrix import getC
- from retrieve_s_matrix import retrieveSmatrix
- from generate_rasorb import generate_rasorb_file
- from rasorb import write_rasorb_files
- %cd
- ff1S = np.load('/content/results_essone.npy')
- eses = [ff1S]
- ff1Cs = getC(resultfirstone, ff1S, 10)
- generate_rasorb_file(filenames[0], ff1Cs[0])
- write_rasorb_file(ff1Cs, 'ff1C', 10)

**Tenth Step - Complete the calculation and analysis of CASCI Energies**
 This step requires to use the HPC cluster, so for the tutorial data I have generated the results and these can also be found in the Data for Tutorial section.
 To see the analysis of the data, it works more efficiently to use the Google Colab tutorial.

 That is the end of the workflow, feel free to email me with any questions!


