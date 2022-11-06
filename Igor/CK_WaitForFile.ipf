#pragma rtGlobals=1		// Use modern global access method.
#pragma version = 1.01


Function CK_WaitForWriteAccessToFile(path, filename, timeout, checkPeriod)
	String path, filename
	Variable timeout		// seconds to wait before giving up (0 means wait forever)
	Variable checkPeriod	// seconds to wait between tries
	
	Variable myRef
	Variable startTime

	Variable returnValue = 0
	
	timeout *= 60
	startTime = Ticks
	do
		Open/Z/R/P=$path myRef as filename	
		if (V_flag == 0)
			close myRef
			Open/Z/A/P=$path myRef as filename
				if (V_flag == 0)
					close myRef
				break
			endif
		endif
		if ( (timeout > 0) && (Ticks - startTime > timeout) )
			returnValue = V_flag
			break
		endif
		Sleep/S checkPeriod
	while(1)
	
	return returnValue
end

