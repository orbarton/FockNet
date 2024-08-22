#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
def read_nrg(file):
    '''Read MO energies.'''
    
    nrg_orbitals=[]
    with open(file,"r") as stream:
        readorbitals=False
        anchor="pre-start"
        while not readorbitals and anchor!="":
            anchor=stream.readline()
            if "#INFO" in anchor and "orbitals" in stream.readline():
                stream.readline()
                norbitals=int(stream.readline())
                if (norbitals%10)!=0:
                    block=norbitals//10+1
                else:
                    block=norbitals//10
            elif "#ONE" in anchor:
                stream.readline()
                for nrgee in range(block):
                    nrg_new=stream.readline()
                    nrg_orbitals.extend(nrg_new.split())
                readorbitals=True           
    return np.array(nrg_orbitals, dtype=float)

