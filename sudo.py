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

#Chapter 5.2 Reduce the sudo timeout period 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tSudo")
	l.info( "\t\tgetSudoLogTime")
	retObj = getSudoLogOutTime ()
	comment = retObj.getComment()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tcomment: " + comment)
	if retVal == 1:
		l.info("\t\t\tremedy:  " + retObj.getRemed())
		
def getSudoLogOutTime ():
	#sudo cat /etc/sudoers | grep timestamp
	retObj = funcReturn.funcReturn('getSudoLogOutTime')
	appleCommand = ["cat", "/etc/sudoers"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getSudoLogOutTime')
	result = retObj.getStdout().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	needle = "timestamp_timeout=0"
	for r in resultList:
		if r.strip() != "":
			if stringFunctions.strFind (r.strip(), needle) == 0:
				resultListMod.append(r.strip())	
	retObj.setResult(resultListMod)
	if len(resultListMod) == 1:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
		remedy= """\t1. Run the following command in Terminal:
\t\t\t\t\t\t\t\t\tsudo visudo
\t\t\t\t\t\t\t\t2. In the "# Defaults specification" section, add the line:
\t\t\t\t\t\t\t\t\tDefaults timestamp_timeout=0"""
	retObj.setRemed(remedy)
	return retObj	
		
