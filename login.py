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

#Chapter 5.5 Disable automatic login 10.9 CIS Benchmark  
#Chapter 5.8 Disable ability to login to another user's active and locked session

def run (l, TEMP):
	l.info( "\tlogin")
	l.info( "\t\tgetLoginInfo")
	retObj = getLoginInfo ()
	comment = retObj.getComment()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tcomment: " + comment)
	if retVal == 1:
		l.info( "\t\tsetLoginInfo")
		retObj = setLoginInfo ()

	l.info( "\t\tgetAbilityLoginAnother")
	retObj = getAbilityLoginAnother ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
		
	if retVal == 1:
		l.info( "\t\tsetAdminPreferenceStatus")
		retObj = setAbilityLoginAnother ()	
		remed=retObj.getRemed()
		l.info( "\t\t\tremeditiion: " + remed )
		
def getLoginInfo ():
	#defaults read /Library/Preferences/com.apple.loginwindow | grep autoLoginUser
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.loginwindow"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getLoginInfo')
	result = retObj.getStderr().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	needle = "autoLoginUser"
	for r in resultList:
		if r.strip() != "":
			if stringFunctions.strFind (r.strip(), needle) != 0:
				resultListMod.append(r.strip())	
	retObj.setResult(resultListMod)
	if len(resultListMod) == 0:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj

def setLoginInfo():
	#defaults delete /Library/Preferences/com.apple.loginwindow autoLoginUser
	retObj = funcReturn.funcReturn('setLoginInfo')
	appleCommand = ["defaults", "delete", "/Library/Preferences/com.apple.loginwindow", "autoLoginUser"]
	retObj.setName('setLoginInfo')
	retObj = comWrap.comWrapRetObj(appleCommand)
	result = retObj.getStderr().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	etObj.setRetVal(0)
	return retObj

def setAbilityLoginAnother():
	#5.8 Disable ability to login to another user's active and locked session
	retObj = funcReturn.funcReturn('setAbilityLoginAnother')
	remedy= """\t1. sudo vi /etc/pam.d/screensaver
\t\t\t\t\t\t\t\t2. Locate account required pam_group.so no_warn group=admin,wheel fail_safe
\t\t\t\t\t\t\t\t3. Remove "admin,"
\t\t\t\t\t\t\t\t4. Save"""
	retObj.setRemed(remedy)
	return retObj
	
	
def getAbilityLoginAnother():
	#5.8 Disable ability to login to another user's active and locked session
	#grep -i "group=admin,wheel fail_safe" /etc/pam.d/screensaver		
	retObj = funcReturn.funcReturn('getAbilityLoginAnother')
	appleCommand = ["grep", "-i", "group=admin,wheel fail_safe", "/etc/pam.d/screensaver" ]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setResult(retObj.getStdout())
	result = retObj.getResult()
	stdOut=retObj.getStdout().strip() 
	retObj.setStdout(stdOut)
	stdErr=retObj.getStderr().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	if len(resultList) == 0:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj

