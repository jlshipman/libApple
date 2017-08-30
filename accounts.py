#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex
import re
import plistlib
import pwd, grp
import listFunctions
import stringFunctions
import funcReturn
import getpass

#6.1.1 Display login window as name and password 	 10.9 CIS Benchmark  
#6.1.2 Disable "Show password hints"
#6.1.3 Disable guest account login 
#6.1.4 Disable "Allow guests to connect to shared folders"
#6.3 Disable the automatic run of safe files in Safari 
#6.4 Use parental controls for systems that are not centrally managed
def run (l, TEMP):
	l.info( "\tAccounts")
	
	l.info( "\t\tgetLoginWindow")
	retObj = getLoginWindow ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetLoginWindow")
		retObj = setLoginWindow ()	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))

	l.info( "\t\tgetDisableHints")
	retObj = getDisableHints ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetDisableHints")
		retObj = setDisableHints ()	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))
	
	l.info( "\t\tgetDisableGuestAFP")
	retObj = getDisableGuestAFP ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetDisableGuestAFP")
		retObj = setDisableGuestAFP ()	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))
		
	l.info( "\t\tgetDisableGuestSMB")
	retObj = getDisableGuestSMB ()	
	retVal=retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetDisableGuestSMB")
		retObj = setDisableGuestSMB ()	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))
				
def getLoginWindow():
	#6.1.1 Display login window as name and password
	#defaults read /Library/Preferences/com.apple.loginwindow SHOWFULLNAME
	retObj = funcReturn.funcReturn('getLoginWindow')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.loginwindow", "SHOWFULLNAME"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getLoginWindow')
	result = int(retObj.getStdout().strip() )
	if result == 1:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj	

def setLoginWindow():
	#6.1.1 Display login window as name and password
	#sudo defaults write /Library/Preferences/com.apple.loginwindow SHOWFULLNAME -bool yes
	retObj = funcReturn.funcReturn('setLoginWindow')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.loginwindow", "SHOWFULLNAME", "-bool", "yes"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setLoginWindow')
	result = retObj.getStdout().strip() 
	retObj.setRetVal(0)
	return retObj	

def getDisableHints():
	#6.1.2 Disable "Show password hints"
	#defaults read /Library/Preferences/com.apple.loginwindow RetriesUntilHint
	retObj = funcReturn.funcReturn('getDisableHints')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.loginwindow", "RetriesUntilHint"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getDisableHints')
	result = retObj.getStdout().strip()
	resultError = retObj.getStderr().strip() 
	needle="The domain/default pair of (/Library/Preferences/com.apple.loginwindow, RetriesUntilHint) does not exist"
	if stringFunctions.strFind (resultError.strip(), needle) != 0:
		retObj.setRetVal(0)
	elif result == 0:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj	

def setDisableHints():
	#6.1.2 Disable "Show password hints"
	#sudo defaults write /Library/Preferences/com.apple.loginwindow GuestEnabled -bool NO
	retObj = funcReturn.funcReturn('setLoginWindow')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.loginwindow", "RetriesUntilHint", "-int", "0"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getLoginWindow')
	result = retObj.getStdout().strip() 
	retObj.setRetVal(0)
	return retObj	

def getDisableGuest():
	#6.1.3 Disable guest account login 
	#defaults read /Library/Preferences/com.apple.loginwindow GuestEnabled
	retObj = funcReturn.funcReturn('getDisableGuest')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.loginwindow", "GuestEnabled"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getDisableGuest')
	result = int(retObj.getStdout().strip())
	if result == 0:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj	

def setDisableGuest():
	#6.1.3 Disable guest account login 
	#sudo defaults write /Library/Preferences/com.apple.loginwindow GuestEnabled -bool NO
	retObj = funcReturn.funcReturn('setLoginWindow')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.loginwindow", "GuestEnabled", "-bool", "NO"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getLoginWindow')
	result = retObj.getStdout().strip() 
	retObj.setRetVal(0)
	return retObj	
	
def getDisableGuestAFP():
	#6.1.4 Disable "Allow guests to connect to shared folders"
	#defaults read /Library/Preferences/com.apple.AppleFileServer | grep -i guest
	retObj = funcReturn.funcReturn('getDisableGuestAFP')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.AppleFileServer"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getDisableGuestAFP')
	result = retObj.getStdout().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	for r in resultList:
		if r != "":
			rList = r.split("=")
			if rList[0].strip() == "guestAccess":
				val = int(rList[1].strip().replace(';',''))
				if rList[1] == 0:
					retObj.setRetVal(0)
	return retObj	
	
def setDisableGuestAFP():
	#6.1.4 Disable "Allow guests to connect to shared folders"
	#sudo defaults write /Library/Preferences/com.apple.AppleFileServer guestAccess -bool no
	retObj = funcReturn.funcReturn('setDisableGuestAFP')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.AppleFileServer", "guestAccess", "-bool", "no"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setDisableGuestAFP')
	result = retObj.getStdout().strip() 
	retObj.setRetVal(0)
	return retObj	
		
def getDisableGuestSMB():
	#6.1.4 Disable "Allow guests to connect to shared folders"
	#defaults read /Library/Preferences/com.getDisableGuestSMB.AppleFileServer | grep -i guest
	retObj = funcReturn.funcReturn('getDisableGuestAFP')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.smb.server"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getDisableGuestSMB')
	needle="Domain /Library/Preferences/com.apple.smb.server does not exist"
	resultError = retObj.getStderr().strip() 
	if stringFunctions.strFind (resultError.strip(), needle) != 0:
		retObj.setRetVal(0)
	else:
		result = retObj.getStdout().strip() 
		resultList = listFunctions.stringToList(result, "\n")
		for r in resultList:
			if r != "":
				rList = r.split("=")
				if rList[0].strip() == "guest":
					val = int(rList[1].strip().replace(';',''))
					if rList[1] == 0:
						retObj.setRetVal(0)
	return retObj
	
def setDisableGuestSMB():
	#6.1.4 Disable "Allow guests to connect to shared folders"
	#sudo defaults write /Library/Preferences/com.apple.AppleFileServer guestAccess -bool no
	retObj = funcReturn.funcReturn('setDisableGuestSMB')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.smb.server", "AllowGuestAccess", "-bool", "no"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setDisableGuestSMB')
	result = retObj.getStdout().strip() 
	retObj.setRetVal(0)
	return retObj		