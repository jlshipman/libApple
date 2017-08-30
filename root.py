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

#Chapter 5.4 Do not enable the "root" account 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tRoot")
	l.info( "\t\tgetRootInfo")
	retObj = getRootInfo ()
	comment = retObj.getComment()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tcomment: " + comment)
	if retVal == 1:
		l.info("\t\t\tremedy:  " + retObj.getRemed())
		
def getRootInfo ():
	#dscl . -read /Users/root AuthenticationAuthority
	retObj = funcReturn.funcReturn('getRootInfo')
	appleCommand = ["dscl", ".", "-read", "/Users/root", "AuthenticationAuthority"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getRootInfo')
	result = retObj.getStderr().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	needle = "No such key: AuthenticationAuthority"
	for r in resultList:
		if r.strip() != "":
			if stringFunctions.strFind (r.strip(), needle) != 0:
				resultListMod.append(r.strip())	
	retObj.setResult(resultListMod)
	if len(resultListMod) == 1:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
		remedy= """\t1. Open System Preferences
\t\t\t\t\t\t\t\t2. Select Uses & Groups
\t\t\t\t\t\t\t\t3. Click the lock icon to unlock it
\t\t\t\t\t\t\t\t4. In the Network Account Server section, click Join or Edit
\t\t\t\t\t\t\t\t5. Click Open Directory Utility
\t\t\t\t\t\t\t\t6. Click the lock icon to unlock it.
\t\t\t\t\t\t\t\t7. Select the Edit menu > Disable Root User."""

		retObj.setRemed(remedy)
	return retObj		