#CK_Biophysics
# -*- coding: utf-8 -*-

from neuron import h
from CK_Python.CK_Parameter import CK_GetParam 

def CK_Addfuscurr(soma):
    soma.insert('fuscurr')
    h.gnabar_fuscurr = CK_GetParam("CK_gnabar",0)
    h.gkbar_fuscurr = CK_GetParam("CK_gkbar",0)
    h.ghbar_fuscurr = CK_GetParam("CK_ghbar",0)
    h.gnapbar_fuscurr = CK_GetParam("CK_gnapbar",0)
    h.gkirbar_fuscurr = CK_GetParam("CK_gkirbar",0)
    h.gl_fuscurr = CK_GetParam("CK_gl",0)
    soma.ekir = CK_GetParam("CK_ekir",0)
    soma.eh = CK_GetParam("CK_eh",0)
    soma.enap = CK_GetParam("CK_enap",0)
    soma.ek = CK_GetParam("CK_ek",0)
    return soma

def CK_Modfuscurr(channelnum,gbar):
    if channelnum==0:
            h.gnabar_fuscurr=gbar
    elif channelnum==1:
            h.gkbar_fuscurr=gbar
    elif channelnum==2:
            h.ghbar_fuscurr=gbar
    elif channelnum==3:
            h.gnapbar_fuscurr=gbar
    elif channelnum==4:
            h.gkirbar_fuscurr=gbar
    elif channelnum==5:
            h.gl_fuscurr=
    else:        
            print ("CK_Modfuscurr: unknown current, ",channelnum)

def CK_test():
    print (__name__)
    
    
