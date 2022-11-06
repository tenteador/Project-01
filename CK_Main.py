# -*- coding: utf-8 -*-

from neuron import h
from neuron.units import ms, mV
h.load_file('stdrun.hoc')

import CK_Python.CK_Semaphor
from CK_Python.CK_Parameter import CK_GetParam, CK_LoadParams, CK_SetParam 
import CK_Python.CK_Util
import CK_Geometry
import CK_Biophysics
import msvcrt
from time import sleep

CK_WriteNeuronPathFileName='c:\\users\\lenovo\\IgorNeuronTemp\\SemaphorFolder\\CK_Neuron.dat'
 
#Standard simple program
# def CK_RunOneSimulation():
    
#     CK_LoadParams()
    
#     CK_dt = CK_GetParam("CK_dt",0)
#     CK_TStop=CK_GetParam("CK_tstop",0)
#     CK_vinit=CK_GetParam("CK_vinit",0)
    
#     soma=CK_Geometry.CK_CreateSoma()
#     CK_Biophysics.CK_Addfuscurr(soma)
#     CK_IClamp1 = h.IClamp(soma(0.5))
#     CK_IClamp1.delay=CK_GetParam("CK_IClamp1delay",0)
#     CK_IClamp1.dur=CK_GetParam("CK_IClamp1dur",0)
#     CK_IClamp1.amp=CK_GetParam("CK_IClamp1amp",0)

#     CK_IClamp2 = h.IClamp(soma(0.5))
#     CK_IClamp2.delay=CK_GetParam("CK_IClamp2delay",0)
#     CK_IClamp2.dur=CK_GetParam("CK_IClamp2dur",0)
#     CK_IClamp2.amp=CK_GetParam("CK_IClamp2amp",0)


#     v = h.Vector().record(soma(0.5)._ref_v,CK_dt)             # Membrane potential vector

#     h.finitialize(CK_vinit * V)
#     h.dt=CK_dt
    
#     h.continuerun(CK_TStop * ms)
#     CK_Python.CK_Util.CK_WriteNeuronVec("CK_Neuron.dat",v)
#     return v


#Vary one conductance, measure spontaneous freq
def CK_RunOneSimulation():
    
    CK_LoadParams()
    
    CK_dt = CK_GetParam("CK_dt",0)
    CK_TStop=CK_GetParam("CK_tstop",0)
    CK_vinit=CK_GetParam("CK_vinit",0)
    
    soma=CK_Geometry.CK_CreateSoma()
    CK_Biophysics.CK_Addfuscurr(soma)
    CK_IClamp1 = h.IClamp(soma(0.5))
    CK_IClamp1.delay=CK_GetParam("CK_IClamp1delay",0)
    CK_IClamp1.dur=CK_GetParam("CK_IClamp1dur",0)
    CK_IClamp1.amp=CK_GetParam("CK_IClamp1amp",0)

    CK_IClamp2 = h.IClamp(soma(0.5))
    CK_IClamp2.delay=CK_GetParam("CK_IClamp2delay",0)
    CK_IClamp2.dur=CK_GetParam("CK_IClamp2dur",0)
    CK_IClamp2.amp=CK_GetParam("CK_IClamp2amp",0)

    CK_ModChannelNum=CK_GetParam("CK_ModChannelNum",0)
    CK_ModChannelStart=CK_GetParam("CK_ModChannelStart",0)
    CK_ModChannelFinal=CK_GetParam("CK_ModChannelFinal",0)
    CK_ModChannelDelta=CK_GetParam("CK_ModChannelDelta",0)
 
    nsteps = int((CK_ModChannelFinal-CK_ModChannelStart)/CK_ModChannelDelta + 1.5)
    print ("Doing one, nsteps =", nsteps)
    
    v = h.Vector().record(soma(0.5)._ref_v,CK_dt)             # Membrane potential vector
    v2=h.Vector()
    h.dt=CK_dt

    for i in range(0,nsteps,1): 
        print (i)
        CK_Biophysics.CK_Modfuscurr(CK_ModChannelNum,CK_ModChannelStart+i*CK_ModChannelDelta) 
        h.finitialize(CK_vinit * mV)
        h.continuerun(CK_TStop * ms)
        v2.append(v)
 
    CK_Python.CK_Util.CK_WriteNeuronVec(CK_WriteNeuronPathFileName,v2)
    return v


# #Negative holding current, variable step currents, measure spontaneous freq
# def CK_RunOneSimulation():
    
#     CK_LoadParams()
    
#     CK_dt = CK_GetParam("CK_dt",0)
#     CK_tstop=CK_GetParam("CK_tstop",0)
#     CK_vinit=CK_GetParam("CK_vinit",0)
    
#     soma=CK_Geometry.CK_CreateSoma()
#     CK_Biophysics.CK_Addfuscurr(soma)
#     CK_IClamp1 = h.IClamp(soma(0.5))
#     CK_IClamp1.delay=CK_GetParam("CK_IClamp1delay",0)
#     CK_IClamp1.dur=CK_GetParam("CK_IClamp1dur",0)
#     CK_IClamp1.amp=CK_GetParam("CK_IClamp1amp",0)

#     CK_IClamp2 = h.IClamp(soma(0.5))
#     CK_IClamp2.delay=CK_GetParam("CK_IClamp2delay",0)
#     CK_IClamp2.dur=CK_GetParam("CK_IClamp2dur",0)
#     CK_IClamp2.amp=CK_GetParam("CK_IClamp2amp",0)

# #Not real IClamp attributes. Used for programming.
#     CK_IClamp2Step0=CK_GetParam("CK_IClamp2Step0",0)
#     CK_IClamp2StepDelta=CK_GetParam("CK_IClamp2StepDelta",0)
#     CK_IClamp2NSteps = CK_GetParam("CK_IClamp2NSteps",1)
   
#     print ("Doing one, nsteps =", CK_IClamp2NSteps)
    
#     v = h.Vector().record(soma(0.5)._ref_v,CK_dt)             # Membrane potential vector
#     # v = h.Vector().record(CK_IClamp2._ref_i,CK_dt)             # Membrane potential vector
#     v2=h.Vector()
#     h.dt=CK_dt

#     for i in range(0,CK_IClamp2NSteps,1): 
#         print (i)
#         CK_IClamp2.amp=CK_IClamp2Step0 + i * CK_IClamp2StepDelta  
#         h.finitialize(CK_vinit * mV)
#         h.continuerun(CK_tstop * ms)
#         v2.append(v)
 
#     CK_Python.CK_Util.CK_WriteNeuronVec(CK_WriteNeuronPathFileName,v2)
#     return v



def CK_CheckForEscape():
    return msvcrt.kbhit() and msvcrt.getch() == chr(27).encode()


#%%
done=0
while not done:
    Semaphor=CK_Python.CK_Semaphor.CK_WaitSemaphor(1,1000)
    if Semaphor==1:
        print ("Doing one")
        CK_Python.CK_Parameter.CK_LoadParams()
        returnvec=CK_RunOneSimulation()
        CK_Python.CK_Semaphor.CK_SetSemaphor(0)
        # done=1


#%%  
# i=0
# while i<100:
#     print (i)
#     CK_RunOneSimulation()
#     i+=1    
    

#%%
# while not CK_CheckForEscape():
#     Semaphor=CK_Python.CK_Semaphor.CK_WaitSemaphor(1,1000)
#     if Semaphor==1:
#         print ("Doing one")
#         CK_Python.CK_Parameter.CK_LoadParams()
#         CK_RunOneSimulation()
#         CK_Python.CK_Semaphor.CK_SetSemaphor(0)


#%% 