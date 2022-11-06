# -*- coding: utf-8 -*-


from CK_Python.CK_Semaphor import CK_LockSemaphor, CK_UnLockSemaphor

#Set here the complete pathname for the parameter files
CK_ParamsPath = 'c:\\users\\lenovo\\IgorNeuronTemp\\SemaphorFolder\\'
CK_FromIgorParamNamesFileName='CK_FromIgorParamNames.dat'
CK_FromIgorParamValuesFileName='CK_FromIgorParamValues.dat'


CK_ParamNames = []
CK_ParamValuesStr = []
CK_ParamValues = []

def CK_LoadParams():
    CK_ParamNames.clear()
    CK_ParamValuesStr.clear()
    CK_ParamValues.clear()

    f=CK_LockSemaphor()
    
    with open(CK_ParamsPath+CK_FromIgorParamNamesFileName,"r") as f:
        ParamNames=f.readlines()
    f.close()

    CK_UnLockSemaphor(f)

    for ParamName in ParamNames:    
       CK_ParamNames.append(ParamName.strip('\n'))    
    with open(CK_ParamsPath+CK_FromIgorParamValuesFileName,"r") as f:
        ParamValuesStr=f.readlines()
    f.close()
    for ValueStr in ParamValuesStr:    
        CK_ParamValues.append(float(ValueStr.strip('\n')))    

def CK_GetParam(name, asInt):
    if asInt:
        return int(CK_ParamValues[CK_ParamNames.index(name)])
    else:
        return CK_ParamValues[CK_ParamNames.index(name)]

def CK_SetParam(name, val, asInt):
    if asInt:
        CK_ParamValues[CK_ParamNames.index(name)]=int(val)
    else:
        CK_ParamValues[CK_ParamNames.index(name)]=val
