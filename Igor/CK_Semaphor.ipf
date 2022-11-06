#pragma TextEncoding = "UTF-8"
#pragma rtGlobals=3		// Use modern global access method and strict wave access.


// Semaphor is written to the file defined below in the pathname defined below.
// The path must exist.


StrConstant CK_SemaphorPathName = "CK_Semaphor"
StrConstant CK_SemaphorFileName = "CK_Semaphor.dat"
StrConstant CK_SemaphorLockFileName = "CK_SemaphorLock.dat"
Constant		CK_OddTimeToNotCoincideWithPython = 0.21

function CK_TestSleep()
	variable i, myRef
	print "start"
	for (i=0; i<10; i+=1)
//		sleep /s CK_OddTimeToNotCoincideWithPython
		Open/Z/A/P=$CK_SemaphorPathName myRef as CK_SemaphorLockFileName
		if (V_flag == 0)
			close myRef
//			break
		endif
	endfor
	print "stop"
end

function CK_LockSemaphor()
	variable myRef
	do
		Open/Z/A/P=$CK_SemaphorPathName myRef as CK_SemaphorLockFileName
		if (V_flag == 0)
			return myRef
			break
		endif
		print "Waiting for lock file"
		Sleep/S CK_OddTimeToNotCoincideWithPython
	while(1)
end


function CK_unLockSemaphor(myRef)
	variable myRef
	close myRef
end




function CK_SetSemaphor(val)
	variable val
	variable myRef
	
	make /free/n=1/o temp = val
	
	myRef = CK_LockSemaphor()
	
	Save  /O/P=$CK_SemaphorPathName/G/M="\r\n" temp as CK_SemaphorFileName
	
	CK_UnLockSemaphor(myRef) 
end



function CK_GetSemaphor()

	variable myRef
	
	myRef = CK_LockSemaphor()

	LoadWave  /P=CK_Semaphor/D /G /J /N=CK_Semaphor /O  /Q  /W "CK_Semaphor.dat"
	
	CK_UnLockSemaphor(myRef)
	
	wave CK_Semaphor0
	return CK_Semaphor0[0]
end

function CK_WaitSemaphor (val,timeout)
	variable val, timeout
	variable lim=trunc(timeout/CK_OddTimeToNotCoincideWithPython)
	variable c=1, j=0
	for (;c;)
		c = ((CK_GetSemaphor()!=val)&&(j<lim))
		if (c)
			sleep /s CK_OddTimeToNotCoincideWithPython
			j+=1
//			print j
		endif
	endfor
	if (j<lim)
		return val
	else
		return -1
	endif
end


function CK_testLock()
	variable i
	for (i=0; i<10000; i+=1)
		if (!mod(i,100))
			print i
		endif
		variable myRef
		myRef = CK_LockSemaphor()
//		print myRef
		CK_UnLockSemaphor(myRef)
//		sleep /s 0.01
	endfor
end
	
	
	
function CK_TestSem()
	variable val
	do
		val=CK_GetSemaphor()
		val-= 1
		CK_SetSemaphor(val)
		sleep/s .1
		print val
	while (1)
end
