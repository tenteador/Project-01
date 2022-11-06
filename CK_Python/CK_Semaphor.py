# -*- coding: utf-8 -*-

#Set here the complete pathname for the semaphor file
CK_SemaphorPathFileName=''
CK_SemaphorLockPathFileName=''

import time

CK_OddTimeToNotCoincideWithIgor=0.29

def CK_LockSemaphor():
    success=0
    while not success:
        try:
            f = open (CK_SemaphorLockPathFileName,'w')
            success=1
        except:
            print ("LockFile busy")
            time.sleep(CK_OddTimeToNotCoincideWithIgor)
    return f

def CK_UnLockSemaphor(f):
    f.close()
        
        
def CK_SetSemaphor(val):
    f1 = CK_LockSemaphor()
    f = open (CK_SemaphorPathFileName,'w')
    f.write(str(val))
    f.flush()
    f.close()
    CK_UnLockSemaphor(f1)


def CK_GetSemaphor():
    f1 = CK_LockSemaphor()
    f = open (CK_SemaphorPathFileName,'r')
    val = int(f.read())
    f.close()
    CK_UnLockSemaphor(f1)
    return val
  

def CK_WaitSemaphor(val,lim):
    j=0
    s=-1
    s = CK_GetSemaphor()
    while (s!=val) and (j<lim):
        print ("Waiting",j)
        time.sleep(CK_OddTimeToNotCoincideWithIgor)
        s = CK_GetSemaphor()
        j+=1
    if j<lim:
        return val
    else:
        return -1
        

 #%%
    i=0
    CK_SetSemaphor(0)
    val=0
    while(val<1000):
        val = CK_GetSemaphor()
        print (val)
        CK_SetSemaphor(val+1)
        i+=1
#%%
        
  
#%%
    while (1):
        f=CK_LockSemaphor()
        time.sleep(0.05)
        CK_UnLockSemaphor(f)
#%%
        
