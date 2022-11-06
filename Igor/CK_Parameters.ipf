#pragma TextEncoding = "UTF-8"
#pragma rtGlobals=3		// Use modern global access method and strict wave access.



function CK_MakeFinalParameterList(ParamNames, Paramvalues)
	wave /t ParamNames
	wave Paramvalues
	make /o/t/n=0 CK_FinalParamNames
	make /o/n=0 CK_FinalParamvalues
	wave /t fpn=CK_FinalParamNames
	wave fpv=CK_FinalParamvalues

	variable i,j
	
	for (i=0; i<numpnts(ParamNames); i+=1)
		if (numtype(Paramvalues[i])!=1)
			InsertPoints numpnts(fpn), 1, fpn,fpv
			fpn[numpnts(fpn)-1]=ParamNames[i]
			fpv[numpnts(fpn)-1]=Paramvalues[i]
		else
			wave /t ParamNames1 = $ParamNames[i]+":ParamNames"
			wave    Paramvalues1 = $ParamNames[i]+":ParamValues"
			for (j=0; j<numpnts(ParamNames1); j+=1)
				if (numtype(Paramvalues1[j])!=1)
					InsertPoints numpnts(fpn), 1, fpn,fpv
					fpn[numpnts(fpn)-1]=ParamNames1[j]
					fpv[numpnts(fpn)-1]=Paramvalues1[j]
				endif
			endfor
		endif
	endfor
end


function CK_WriteParametersToNeuron(ParamNames, Paramvalues)
	wave /T ParamNames
	wave Paramvalues
	variable myRef

	PathInfo LoadVecs
	if (!V_Flag)	
		PathInfo home
		if (!V_Flag)
			NewPath /O/Q/Z LoadVecs "C:"
		else
			NewPath /O/Q/Z LoadVecs s_path
		endif
	endif
	myRef = CK_LockSemaphor()
	Open/Z/A/P=$CK_SemaphorPathName myRef as CK_SemaphorLockFileName
	Save  /O/P=LoadVecs/G/M="\r\n" ParamNames as "CK_FromIgorParamNames.dat"
	Save  /O/P=LoadVecs/G/M="\r\n" Paramvalues as "CK_FromIgorParamValues.dat"
	CK_UnLockSemaphor(myRef)
	NewPath /O/Q/Z LoadVecs s_path
end




Function CK_GetParam(i,n,pw)
	variable i,n
	wave pw
	if (!numtype(n))
		pw[i]=n
	endif
	return pw[i]
end


Function CK_GetParam2(name,val,pn,pv)
	string name 
	variable val
	wave/t   pn
	wave pv
	variable i=-1, found=0
	do
		i+=1
		found=!cmpstr(name,pn[i])
	while (!found && i<numpnts(pn)-1)
	if (found)
		return CK_GetParam(i,val,pv)
	else
		print "Parameter not found:", name
		return -inf
	endif
end


function /wave CK_LoadFromNeuron()
	variable myRef
	
	PathInfo LoadVecs
	if (!V_Flag)
		PathInfo home
		if (!V_Flag)
			NewPath /O/Q/Z LoadVecs "C:"
		else
			NewPath /O/Q/Z LoadVecs s_path
		endif
	endif
//	myRef = CK_LockSemaphor()
	LoadWave  /P=LoadVecs/D /G /J /N=CK_NeuronImport /O  /Q  /W "CK_Neuron.dat"
//	CK_UnLockSemaphor(myRef)
	NewPath /O/Q/Z LoadVecs s_path
	
	Wave nw = CK_NeuronImport0
	duplicate /free nw returnwave
	return returnwave
	

end
