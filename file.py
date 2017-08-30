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

#6.2 Turn on filename extensions 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tFile")
	l.info( "\t\tgetFileExt")
	retObj = getFileExt ()
	comment = retObj.getComment()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetFileExt")
		retObj = setFileExt ()
		l.info( "\t\t\tretVal: " + str(retVal))
		
#6.2 Turn on filename extensions 10.9 CIS Benchmark  		
def getFileExt ():
	#defaults read NSGlobalDomain AppleShowAllExtensions
	retObj = funcReturn.funcReturn('getFileExt')
	appleCommand = ["defaults", "read", "NSGlobalDomain", "AppleShowAllExtensions"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getFileExt')
	resultError = retObj.getStderr().strip() 
	needle="The domain/default pair of"
	findObj=stringFunctions.strFind (resultError, needle)
	findResult=findObj.getRetVal()
	if findResult != 0:
		result = int(retObj.getStdout().strip())
		retObj.setResult(result)
		if result == 1:
			retObj.setRetVal(0)
	return retObj	
	
#6.2 Turn on filename extensions 10.9 CIS Benchmark  		
def setFileExt ():
	#defaults write NSGlobalDomain AppleShowAllExtensions -bool true
	retObj = funcReturn.funcReturn('setFileExt')
	appleCommand = ["sudo", "defaults", "write", "NSGlobalDomain", "AppleShowAllExtensions", "-bool", "true"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setFileExt')
	retObj.setRetVal(0)
	return retObj				