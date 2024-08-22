import numpy as np

def read_orbcoef(file):
    '''Read MO coefficients from a Molcas (Ras)Orb file.'''
    
    orbitals=[]
    with open(file,"r") as stream:
        readorbitals=False
        anchor="pre-start"
        while not readorbitals and anchor!="":
            anchor=stream.readline()
            if "#INFO" in anchor and "orbitals" in stream.readline():
                stream.readline()
                norbitals=int(stream.readline())
                if (norbitals%5)!=0:
                    block=norbitals//5+1
                else:
                    block=norbitals//5
            elif "#ORB" in anchor:
                for orb in range(1,norbitals+1):
                    stream.readline()
                    coef_st=""
                    for row in range(block):
                        coef_st=coef_st+stream.readline()
                    orbitals.append(np.array(coef_st.split(),dtype="float"))
                readorbitals=True
                
    return np.array(orbitals)