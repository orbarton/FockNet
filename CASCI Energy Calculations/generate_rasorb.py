def generate_rasorb_file(filename, matrix):
    import numpy as np
    matrix = matrix.T
    with open(filename, 'w') as f:
        # Write the header
        f.write("#INPORB 2.2\n")
        f.write("#INFO\n")
        f.write("* RASSCF canonical orbitals for CASPT2\n")
        f.write("       0       1       0\n")
        f.write("      32\n")  # Example number of orbitals; adjust as needed
        f.write("      32\n")
        f.write("#ORB\n")

        # Write the orbital data
        for i in range(32):
            f.write(f'* ORBITAL    1    {i + 1}\n')
            for j in range(0, len(matrix[i]), 5):
                f.write(' ')
                line = ' '.join(f'{element: .14E}' if element < 0 else f' {element:.14E}' for element in matrix[i][j:j+5])
                f.write(line + '\n')

        f.write('#OCC\n')
        f.write('* OCCUPATION NUMBERS\n')
        f.write('  ')
        f.write('1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00\n')
        f.write('  ')
        f.write('1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00\n')
        f.write('  ')
        f.write('1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00\n')
        f.write('  ')
        f.write('1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00\n')
        f.write('  ')
        f.write('1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00\n')
        f.write('  ')
        f.write('1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00\n')
        f.write('  ')
        f.write('1.00000000000000E+00  1.00000000000000E+00\n')
        f.write('#OCHR\n')
        f.write('* OCCUPATION NUMBERS (HUMAN-READABLE)\n')
        f.write('  ')
        f.write('1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000\n')
        f.write('  ')
        f.write('1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000\n')
        f.write('  ')
        f.write('1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000  1.0000\n')
        f.write('  ')
        f.write('1.0000  1.0000\n')
        f.write('#INDEX\n')
        f.write('* 1234567890\n')
        f.write('0 iiiiiiiiii\n')
        f.write('1 iiiiii2222\n')
        f.write('2 2sssssssss\n')
        f.write('3 ss\n')
