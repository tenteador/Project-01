# -*- coding: utf-8 -*-


from neuron import h

def CK_WriteNeuronVec(filename,v):
    CK_F= h.File()
    CK_F.wopen(filename)
    v.printf(CK_F, " %.10g\n")
    CK_F.close()
    