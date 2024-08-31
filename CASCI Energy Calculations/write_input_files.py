def write_input_file(directory, filename, rasorbname, fileroot,bashdir):

    os.makedirs(directory, exist_ok=True)

    os.makedirs(fileroot, exist_ok=True)

    # Construct the full file path
    filepath = os.path.join(fileroot, filename)
    with open(filepath, 'w') as f:
        f.write('&GATEWAY\n')
        f.write(f'	coord={bashdir}/structure.xyz\n')
        f.write('	basis=ANO-L-VDZP\n')
        f.write('	group=NoSym\n')
        f.write(' &SEWARD\n')
        f.write(' &RASSCF\n')
        f.write('	fileorb=' + rasorbname + '\n')
        f.write('	spin=1\n')
        f.write('	nactel=6 0 0\n')
        f.write('	ras2=5\n')
        f.write('	inactive=16\n')
        f.write('	ciroot=3 3 1\n')
        f.write('	OutOrbitals=Canonical\n')
        f.write('	Order=0\n')
        f.write('	CIONly\n')
        f.write(' &GRID_IT\n')
        f.write('	fileorb=$Project.RasOrb\n')
        f.write('	Sparse\n')
