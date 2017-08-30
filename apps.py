#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex
import re
import funcReturn
import listFunctions
import stringFunctions

#6.3 Disable the automatic run of safe files in Safari 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tApps")
	l.info( "\t\tgetSafariSafeFiles")
	retObj = getSafariSafeFiles ()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetSafariSafeFiles")
		retObj = setSafariSafeFiles ()

		
#6.3 Disable the automatic run of safe files in Safari 10.9 CIS Benchmark  		
def getSafariSafeFiles ():
	#defaults read com.apple.Safari AutoOpenSafeDownloads
	retObj = funcReturn.funcReturn('getSafariSafeFiles')
	appleCommand = ["defaults", "read", "com.apple.Safari", "AutoOpenSafeDownloads"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getSafariSafeFiles')
	result = retObj.getStdout().strip()
	resultError = retObj.getStderr().strip() 
	needle="The domain/default pair of (/Users/ladmin/Library/Preferences/com.apple.Safari, AutoOpenSafeDownloads) does not exist"
	if stringFunctions.strFind (resultError.strip(), needle) != 0:
		retObj.setRetVal(0)
	elif result == 0:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj	
	
#6.3 Disable the automatic run of safe files in Safari 10.9 CIS Benchmark  		
def setSafariSafeFiles ():
	#defaults write com.apple.Safari AutoOpenSafeDownloads -boolean no
	retObj = funcReturn.funcReturn('setSafariSafeFiles')
	appleCommand = ["sudo", "defaults", "write", "com.apple.Safari", "com.apple.Safari AutoOpenSafeDownload", "-bool", "no"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setSafariSafeFiles')
	retObj.setRetVal(0)
	return retObj				