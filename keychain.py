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

#Chapter 5.3 Automatically lock the login keychain after 15 minutes of inactivity and when sleeping 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tKeychain")
	l.info( "\t\tgetKeychainInfo")
	retObj = getKeychainInfo ()
	comment = retObj.getComment()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tcomment: " + comment)
	if retVal == 1:
		l.info("\t\t\tremedy:  " + retObj.getRemed())
		
def getKeychainInfo ():
	#security show-keychain-info
	retObj = funcReturn.funcReturn('getKeychainInfo')
	appleCommand = ["security", "show-keychain-info"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getKeychainInfo')
	result = retObj.getStdout().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	needle = "timeout=900s"
	for r in resultList:
		if r.strip() != "":
			if stringFunctions.strFind (r.strip(), needle) == 0:
				resultListMod.append(r.strip())	
				
	result = retObj.getStderr().strip()
	resultList = listFunctions.stringToList(result, "\n")
	for r in resultList:
		if r.strip() != "":
			if stringFunctions.strFind (r.strip(), needle) == 0:
				resultListMod.append(r.strip())	

 
	retObj.setResult(resultListMod)
	if len(resultListMod) == 0:
		retObj.setRetVal(1)
		remedy= """\t1. Open Utilities
\t\t\t\t\t\t\t\t2. Select Keychain Access
\t\t\t\t\t\t\t\t3. Select a keychain
\t\t\t\t\t\t\t\t4. Select Edit
\t\t\t\t\t\t\t\t5. Select Change Settings for keychain <keychain_name>
\t\t\t\t\t\t\t\t6. Authenticate, if requested.
\t\t\t\t\t\t\t\t7. Select Lock when sleeping setting
\t\t\t\t\t\t\t\t8. Change the Lock after # minutes of inactivity setting for the Login Keychain to 15
\t\t\t\t\t\t\t\t\tminutes or based on the access frequency of the security credentials included in the
\t\t\t\t\t\t\t\t\tkeychain for other keychains."""
		retObj.setRemed(remedy)
	else:
		retObj.setRetVal(0)

	return retObj	
		
