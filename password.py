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
import getpass
import plistlib
import stringFunctions

#Chapter 5.6 Require a password to wake the computer from sleep or screen saver 
#Chapter 5.7 Require an administrator password to access system-wide preferences
#Chapter 5.9 Complex passwords must contain an Alphabetic Character
#Chapter 5.10 Complex passwords must contain an Numeric Character
#Chapter 5.11 Complex passwords must contain an Symbol Character
#Chapter 5.12 Set a minimum password length
#Chapter 5.13 Configure account lockout threshold
#Chapter 5.15 Do not enter a password-related hint

def run (l, TEMP):
	l.info( "\tPassword")
	l.info( "\t\tgetLoginInfo")
	retObj = getScreenSaverPasswordStatus ()
	comment = retObj.getComment()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tcomment: " + comment)
	if retVal == 1:
		l.info( "\t\tsetLoginInfo")
		retObj = setScreenSaverPasswordStatus ()
		
	l.info( "\t\tgetAdminPreferenceStatus")
	retObj = getAdminPreferenceStatus ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	
	if retVal == 1:
		l.info( "\t\tgetAdminPreferenceStatus")
		retObj = getAdminPreferenceStatus ()	
	
	l.info( "\t\tgetPaswordPolicyAlphabetic")	
	retObj = getPaswordPolicyAlphabetic ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetPaswordPolicy")
		retObj = setPaswordPolicy ()	

	l.info( "\t\tgetPaswordPolicyNumeric")	
	retObj = getPaswordPolicyNumeric ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetPaswordPolicy")
		retObj = setPaswordPolicy ()

	l.info( "\t\tgetPaswordPolicySymbol")	
	retObj = getPaswordPolicySymbol ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetPaswordPolicy")
		retObj = setPaswordPolicy ()

	l.info( "\t\tgetPaswordPolicyLength")	
	retObj = getPaswordPolicyLength ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetPaswordPolicy")
		retObj = setPaswordPolicy ()
	
	l.info( "\t\tgetPaswordPolicyLockout")	
	retObj = getPaswordPolicyLockout ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetPaswordPolicy")
		retObj = setPaswordPolicy ()

	l.info( "\t\tpasswordHint")	
	retObj = passwordHint ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
		
def getScreenSaverPasswordStatus ():
	#5.6 Require a password to wake the computer from sleep or screen saver
	#sudo -u ladmin defaults read com.apple.screensaver askForPassword
	retObj = funcReturn.funcReturn('getScreenSaverPasswordStatus')
	curUser = getpass.getuser ()
	appleCommand = ["sudo", "-u", curUser, "defaults", "read", "com.apple.screensaver", "askForPassword"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	result = retObj.getStdout().strip() 
	retObj.setStdout(result)
	if stringFunctions.isInt(result):
		result = int(retObj.getStdout().strip())
		retObj.setResult(result)
		if result == 1:
			retObj.setRetVal(0)
		else:
			retObj.setRetVal(1)
	else:
		retObj.setRetVal(1)
	return retObj

def setScreenSaverPasswordStatus ():
	#Chapter 5.6 Require a password to wake the computer from sleep or screen saver 
	#sudo -u ladmin defaults write com.apple.screensaver askForPassword -int 1
	retObj = funcReturn.funcReturn('setScreenSaverPasswordStatus')
	curUser = getpass.getuser ()
	appleCommand = ["sudo", "-u", curUser, "defaults", "write", "com.apple.screensaver", "askForPassword", "-int", "1"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	return retObj

def getAdminPreferenceStatus ():
	#5.7 Require an administrator password to access system-wide preferences
	#security authorizationdb read system.preferences 
	appleCommand = ["security", "authorizationdb", "read", "system.preferences"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getAdminPreferenceStatus')
	stdOut=retObj.getStdout().strip() 
	retObj.setStdout(stdOut)
	stdErr=retObj.getStderr().strip() 
	retObj.setStderr(stdErr)
	p1 = plistlib.readPlistFromString(stdOut)
	if isinstance(p1,dict):
		key = "rule"
		if key in p1:
			item = p1["rule"][0]
			if item == "authenticate-admin":
				retObj.setRetVal(0)		
	return retObj

def setAdminPreferenceStatus ():
	#5.7 Require an administrator password to access system-wide preferences
	#security authorizationdb write system.preferences authenticate-admin
	appleCommand = ["security", "authorizationdb", "write", "system.preferences", "authenticate-admin"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setAdminPreferenceStatus')
	return retObj
	
def getPaswordPolicyAlphabetic ():
	#Chapter 5.9 Complex passwords must contain an Alphabetic Character
	#pwpolicy -getglobalpolicy | tr " " "\n" | grep requiresAlpha
	appleCommand = ["pwpolicy", "-getglobalpolicy"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getPaswordPolicy')
	result = retObj.getStdout().strip() 
	if result != "":
		resultList=result.split( )
		for r in resultList:
			rList = r.split("=")
			if rList[0].strip() == "requiresAlpha":
				if rList[1] > 0:
					retObj.setRetVal(0)
	return retObj

def getPaswordPolicyNumeric ():
	#Chapter 5.10 Complex passwords must contain an Numeric Character
	#pwpolicy -getglobalpolicy | tr " " "\n" | grep requiresNumeric
	appleCommand = ["pwpolicy", "-getglobalpolicy"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getPaswordPolicy')
	result = retObj.getStdout().strip() 
	if result != "":
		resultList=result.split( )
		for r in resultList:
			rList = r.split("=")
			if rList[0].strip() == "requiresNumeric":
				if rList[1] > 0:
					retObj.setRetVal(0)
	return retObj

def getPaswordPolicySymbol ():
	#Chapter 5.11 Complex passwords must contain an Symbol Character
	#pwpolicy -getglobalpolicy | tr " " "\n" | grep requiresSymbol
	appleCommand = ["pwpolicy", "-getglobalpolicy"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getPaswordPolicy')
	result = retObj.getStdout().strip() 
	if result != "":
		resultList=result.split( )
		for r in resultList:
			rList = r.split("=")
			if rList[0].strip() == "requiresSymbol":
				if rList[1] > 0:
					retObj.setRetVal(0)
	return retObj
	
def getPaswordPolicyLength ():
	#Chapter 5.12 Set a minimum password length
	#pwpolicy -getglobalpolicy | tr " " "\n" | grep minChars
	appleCommand = ["pwpolicy", "-getglobalpolicy"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getPaswordPolicy')
	result = retObj.getStdout().strip() 
	if result != "":
		resultList=result.split( )
		for r in resultList:
			rList = r.split("=")
			if rList[0].strip() == "minChars":
				if rList[1] > 14:
					retObj.setRetVal(0)
	return retObj
	
def getPaswordPolicyLockout ():
	#Chapter 5.13 Configure account lockout threshold 
	#pwpolicy -getglobalpolicy | tr " " "\n" | grep "maxFailedLoginAttempts
	appleCommand = ["pwpolicy", "-getglobalpolicy"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getPaswordPolicy')
	result = retObj.getStdout().strip() 
	if result != "":
		resultList=result.split( )
		for r in resultList:
			rList = r.split("=")
			if rList[0].strip() == "maxFailedLoginAttempts":
				if rList[1] > 5:
					retObj.setRetVal(0)
	return retObj
	
def setPaswordPolicy ():
	#Chapter 5.9 Complex passwords must contain an Alphabetic Character
	#sudo pwpolicy -setglobalpolicy "maxFailedLoginAttempts=5 minChars=15 requiresNumeric=1 requiresAlpha=1 requiresSymbol=1"
	appleCommand = ["sudo", "pwpolicy", "-setglobalpolicy", '"maxFailedLoginAttempts=5 minChars=15 requiresNumeric=1 requiresAlpha=1 requiresSymbol=1"']
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setPaswordPolicy')
	result = retObj.getStdout().strip() 
	return retObj
	
def passwordHint ():
	#Chapter 5.15 Do not enter a password-related hint
	retObj = funcReturn.funcReturn('passwordHint')
	remedy= """\t1. Open System Preferences
\t\t\t\t\t\t\t\t2. Select Uses & Groups
\t\t\t\t\t\t\t\t3. Highlight the user
\t\t\t\t\t\t\t\t4. Select Change Password
\t\t\t\t\t\t\t\t5. Verify that no text is entered in the Password hint box"""
	retObj.setRemed(remedy)
	return retObj		