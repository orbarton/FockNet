# FockNet

This repository details the code used for the FockNet project

The code detailed here will only work for the case where we have a 100 sized dataset, for the sake of brevity.

These instructions are for use in a Jupyter Notebook, but can be easily adapted for command line usage.

Another note is that generating the data is not possible without using a Unix-Bash environment, for which the organisation's HPC cluster was used, however, no tests have been done on a local system, but instructions will still be given in the tutorial notebook.

For this case, all data is going to be provided that is necessary. On top of this, if any user of this code is curious about completing the calculations (the only part completed on the HPC cluster) then they are welcome to contact me for further information at obarton.chemistry@gmail.com

The instructions also help to follow along with the tutorial notebook on Google Colab here:

As an alternative option, here is a Jupyter Notebook with all the code shown:

**First Step - Setup** :
*!git clone https://github.com/orbarton/FockNet.git
*!pip install -r requirements.txt

If installing the requirements doesn't work, which it does not on Colab due to issues with installing packages, try instead

*!pip install h5py
*!pip install schnetpack
*!pip install ase
*!pip install TensorBoard

**Second Step - Splitting Files**
*%cd /content/FockNet/Splitting Files/
*from write_5fold_splitting_files import make_5_fold_split_files
*%cd /content
*make_5_fold_split_files(100)


