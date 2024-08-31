def write_job(index, rasorbname, directory, filename, folder):
    import os

    os.makedirs(directory, exist_ok=True)

    filepath = os.path.join(directory, filename)

    with open(filepath, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('\n')
        f.write('#PBS -lwalltime=00:30:00\n')
        f.write('#PBS -lselect=1:ncpus=1:mem=2GB\n')
        f.write('\n')
        f.write('module load tools/prod\n')
        f.write('module load OpenMolcas/22.10-intel-2022a\n')
        f.write('\n')
        f.write(f'cd $HOME/{folder}')
        f.write('\n')
        f.write(f'pymolcas {rasorbname}in.input > {rasorbname}in.log')
