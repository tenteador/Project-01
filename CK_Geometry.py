#CK_Geometry
# -*- coding: utf-8 -*-

# There are CK_NNodes nodes and (CK_NNodes+1) myelinated segments
# M[0] (0-1) N[0] (0-1) M[1] (0-1) N[1] (0-1) ... N[CK_NNodes-1] M[CK_NNodes]

from neuron import h
from CK_Python.CK_Parameter import CK_GetParam 


def CK_CreateSoma():
    soma=h.Section(name = "soma")
    soma.L=CK_GetParam("CK_L",0)
    soma.diam=CK_GetParam("CK_diam",0)
    soma.Ra=CK_GetParam("CK_Ra",0)
    soma.nseg=CK_GetParam("CK_nseg",1)
    
    return soma
 
