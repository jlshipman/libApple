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

#5.1.1 Secure Home Folderpermissions 	 10.9 CIS Benchmark  
#5.1.2 Repair permissions regularly to ensure binaries and other System files have appropriate permissions
#5.1.3 Check System Wide Applications for appropriate permissions
#5.1.4 Check System folder for world writable files 
#5.1.5 Check Library folder for world writable files
#5.14 Create an access warning for the login window
#5.16 Disable Fast User Switching
#5.17 Secure individual keychain items 
#5.18 Create specialized keychains for different purposes
def run (l, TEMP):
	l.info( "\tAccess")
	
	l.info( "\t\tgetRepairPremissions")
	retObj = getRepairPremissions ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	
	if retVal == 1:
		l.info( "\t\tsetRepairPremissions")
		retObj = setRepairPremissions ()	
		retVal=retObj.getRetVal()
		remed=retObj.getRemed()
		l.info( "\t\t\tretVal: " + str(retVal))
		l.info( "\t\t\tremeditiion: " + remed )
	
	l.info( "\t\tgetPermissHome")
	retDict = getPermissHome ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	theList = retObj.getResult()
	
	if retVal == 1:
		l.info( "\t\tsetPermissHome")
		retObj = setPermissHome (theList)	
		retVal=retObj.getRetVal()
		remed=retObj.getRemed()
		l.info( "\t\t\tretVal: " + str(retVal))
		l.info( "\t\t\tremeditiion: " + remed )

	l.info( "\t\tgetSysWideApps")
	retObj = getSysWideApps ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	theList = retObj.getResult()
	
	if retVal == 1:
		l.info( "\t\tsetSysWideApps")
		retObj = setSysWideApps (theList)	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))

	l.info( "\t\tgetSystemDir")
	retObj = getSystemDir ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	theList = retObj.getResult()
	print theList
	
	if retVal == 1:
		l.info( "\t\tsetSystemDir")
		retObj = setSystemDir (theList)	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))
	
	l.info( "\t\tgetLibraryDir")
	retObj = getLibraryDir ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	theList = retObj.getResult()
	print theList
	
	if retVal == 1:
		l.info( "\t\tsetLibraryDir")
		retObj = setLibraryDir (theList)	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))

	l.info( "\t\tgetWarning")
	retObj = getWarning ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	warning="This US Government computer is for authorized users only. By accessing this system you are consenting to complete monitoring with no expectation of privacy. Unauthorized access or use may subject you to disciplinary action and criminal prosecution."
	l.info( "\t\t\tretVal: " + str(retVal))
	stdOut=retObj.getStdout()
	if stdOut != warning:
		l.info( "\t\tsetWarning")
		warning="This US Government computer is for authorized users only. By accessing this system you are consenting to complete monitoring with no expectation of privacy. Unauthorized access or use may subject you to disciplinary action and criminal prosecution."
		retObj = setWarning (warning)	
		retVal=retObj.getRetVal()
		l.info( "\t\t\tretVal: " + str(retVal))

	l.info( "\t\tfastSwitching")	
	retObj = fastSwitching ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	
	l.info( "\t\tsecureKeychain")	
	retObj = secureKeychain ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )		
	
	l.info( "\t\tspecializedKeychains")	
	retObj = specializedKeychains ()	
	retVal=retObj.getRetVal()
	remed=retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )	
			
def getLibraryDir():
	#5.1.5 Check Library folder for world writable files
	#sudo find /Library -type d -perm -2 -ls
	retObj = funcReturn.funcReturn('getLibraryDir')
	appleCommand = ["find", "/Library", "-type", "d", "-perm", "-2", "-ls"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getLibraryDir')
	result = retObj.getStdout().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	for r in resultList:
		if r.strip() != "":
			resultListMod.append(r.strip())	
	retObj.setResult(resultListMod)
	if len(resultListMod) > 0:
		retObj.setRetVal(1)
	else:
		retObj.setRetVal(0)
	return retObj	

def setLibraryDir(theList):
	#5.1.5 Check Library folder for world writable files 
	#sudo chmod -R o-w /Bad/Directory
	#repair permissions will reset to apple defaults
	retObj = funcReturn.funcReturn('setLibraryDir')
	for l in theList:
		resList = listFunctions.stringToList(l)
		if len(resList) > 0:
			pathApp =  "/" + l.split("/",1)[1]
			appleCommand = ["chmod", "-R", "o-w", pathApp ]
			retObj = comWrap.comWrapRetObj(appleCommand)
			retObj.setName('setLibraryDir')
	retObj = getLibraryDir()
	return retObj
			
def getSystemDir():
	#5.1.4 Check System folder for world writable files
	#sudo find /System -type d -perm -2 -ls
	retObj = funcReturn.funcReturn('getSystemDir')
	appleCommand = ["find", "/System", "-type", "d", "-perm", "-2", "-ls"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getSystemDir')
	result = retObj.getStdout().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	for r in resultList:
		if r.strip() != "":
			resultListMod.append(r.strip())	
	#retObj.setResult(resultListMod)
	if len(resultListMod) > 0:
		retObj.setRetVal(1)
	else:
		retObj.setRetVal(0)
	return retObj	

def setSystemDir(theList):
	#5.1.4 Check System folder for world writable files
	#sudo chmod -R o-w /Bad/Directory
	retObj = funcReturn.funcReturn('setSystemDir')
	for l in theList:
		resList = listFunctions.stringToList(l)
		if len(resList) > 0:
			pathApp =  "/" + l.split("/",1)[1]
			appleCommand = ["chmod", "-R", "o-w", pathApp ]
			retObj = comWrap.comWrapRetObj(appleCommand)
			retObj.setName('setSystemDir')
	retObj = getSystemDir()
	return retObj
	
def setSysWideApps(theList):
	#5.1.3 Check System Wide Applications for appropriate permissions
	#sudo chmod -R o-w /Applications/Bad\ Permissions.app/
	retObj = funcReturn.funcReturn('setSysWideApps')
	for l in theList:
		resList = listFunctions.stringToList(l)
		if len(resList) > 0:
			if resList[2].strip("+") != "drwxr-xr-x" and resList[0].strip("@") != "drwxr-xr-x":
				pathApp =  "/" + l.split("/",1)[1] +  "/"
				appleCommand = ["chmod", "-R", "o-w", pathApp ]
				retObj = comWrap.comWrapRetObj(appleCommand)
				retObj.setName('setSysWideApps')
	retObj = getSysWideApps()
	return retObj
	
def getSysWideApps():
	#5.1.3 Check System Wide Applications for appropriate permissions
	#sudo find /Applications -iname "*\.app" -type d -perm -2 -ls
	retObj = funcReturn.funcReturn('getSysWideApps')
	appleCommand = ["find", "/Applications", "-iname", "*\.app", "-type", "d", "-perm", "-2", "-ls"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getSysWideApps')
	result = retObj.getStdout().strip() 
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	for r in resultList:
		if r.strip() != "":
			resultListMod.append(r.strip())
		
	retObj.setResult(resultListMod)
	if len(resultListMod) > 0:
		retObj.setRetVal(1)
	else:
		retObj.setRetVal(0)
		
	return retObj	

#5.1.2 Repair permissions regularly to ensure binaries and other System files have appropriate permissions 
def setRepairPremissions ():
	#diskutil repairPermissions /
	#takes several minutes
	#script needs to run daily to work properly
	retObj = funcReturn.funcReturn('setRepairPremissions')
	appleCommand = ["diskutil", "repairPermissions", "/"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setRepairPremissions')
	return retObj	

#5.1.2 Repair permissions regularly to ensure binaries and other System files have appropriate permissions 	
def getRepairPremissions ():
	#cat /var/log/system.log* | grep RepairPermissions
	#script needs to run daily to work properly
	retObj = funcReturn.funcReturn('getRepairPremissions')
	retObj.setRemed("run repair premissions")
	appleCommand = ["cat", "/var/log/system.log"]
	retObjCommand = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getRepairPremissions')
	stdout = retObjCommand.getStdout().strip() 
	stderr = retObjCommand.getStderr().strip() 
	result = retObjCommand.getResult()
	retObj.setStderr(stderr)
	retObj.setStdout(stdout)
	resultList = listFunctions.stringToList(result, "\n")
	needle ="RepairPermissions"
# 	print "\t\tresultList"
	found = retObj.getFound()
 	for r in resultList:
  		retObjStr = stringFunctions.strFind( r, needle )
 		Name = retObjStr.getName()
 		Comment = retObjStr.getComment()
 		retVal = retObjStr.getRetVal()
		if retVal == 0:
			found = 0
		
	retObj.setFound(found)
	if found == 0:
		retObj.setRetVal(0)
	return retObj	

#5.1.1 Secure Home Folderpermissions 					
def setPermissHome(list):
	#ls -l /Users/
	retObj = funcReturn.funcReturn('setPermissHome')
		
	for l in list:
		if l[2] == 1:
			userPath = "/Users/" + l[1]
			appleCommand = ["sudo", "chmod", "-R", "og-rwx", userPath]
			retObjCommand = comWrap.comWrapRetObj(appleCommand)
			retObj.setName('setPermissHome')
			stdout = retObjCommand.getStdout.strip() 
			stderr = retObjCommand.getStderr.strip()
			retObj.setStderr(stderr)
			retObj.setStdout(stdout)
			
	retObjGet=getPermissHome()
	retVal=retObjGet.getRetVal()
	if retVal == 1:
		retObj.setRemed("set permission did not work correctly")
	else:
		retObj.setRetVal(0)
		retObj.setComment("permission are set correctly for user accounts")
	return retObj	

#5.1.1 Secure Home Folderpermissions 	
def getPermissHome():
	#ls -l /Users/
	retObj = funcReturn.funcReturn('getPermissHome')
	retObj.setRemed("run setPermissHome")
	appleCommand = ["ls", "-l", "/Users/"]
	retObjCommand = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getPermissHome')
	stdout = retObjCommand.getStdout()
	stderr = retObjCommand.getStderr()
#	print "\t\tstdout" + 	stdout
#	print "\t\tstderr" + 	stderr 
	result = stdout
#	print "\t\tresult" + 	result
	resultList = listFunctions.stringToList(result, "\n")
	resultListMod = []
	found = 0
# 	print "\t\tresultList"
	for r in resultList:
		resList = listFunctions.stringToList(r)
		sizeOfList = len(resList)
		if sizeOfList == 9 and ( "Shared" != resList[8] and ".localized" != resList[8]):
#  			print "\t\t\t r:           " +  r
#  			print "\t\t\t sizeOfList:  " + str(sizeOfList)
#  			print "\t\t\t resList[0]:  " + resList[0].strip("+")
#  			print "\t\t\t resList[8]:  " + resList[8]
 			if resList[0].strip("+") != "drwx------" and resList[0].strip("+") != "drwx--x--x":
				resultListMod.append([resList[0].strip("+"), resList[8], 1])
				found = found + 1
			else:
				resultListMod.append([resList[0].strip("+"), resList[8], 0])
# 	print "\t\tresultListMod"
	if found == 0:
		retObj.setRetVal(0)
	retObj.setResult(resultListMod)
	return retObj

#5.14 Create an access warning for the login window
def getWarning():
	#defaults read /Library/Preferences/com.apple.loginwindow.plist LoginwindowText	
	retObj = funcReturn.funcReturn('getWarning')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.loginwindow.plist","LoginwindowText"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getWarning')
	stdout = retObj.getStdout()
	stderr = retObj.getStderr()
	return retObj

#5.14 Create an access warning for the login window	
def setWarning(warning):
	#sudo defaults write /Library/Preferences/com.apple.loginwindow \ LoginwindowText "your text here"
	retObj = funcReturn.funcReturn('setWarning')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.loginwindow","LoginwindowText", warning]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setWarning')
	stdout = retObj.getStdout()
	stderr = retObj.getStderr()
	return retObj

#5.16 Disable Fast User Switching	
def fastSwitching():
	retObj = funcReturn.funcReturn('fastSwitching')
	remedy= """\t1. Open System Preferences
\t\t\t\t\t\t\t\t2. Select Accounts
\t\t\t\t\t\t\t\t3. Select Login Options
\t\t\t\t\t\t\t\t4. make sure the "Enable fast user switching" checkbox is off."""
	retObj.setRemed(remedy)
	return retObj
	
#5.17 Secure individual keychain items 
def secureKeychain():
	retObj = funcReturn.funcReturn('secureKeychain')
	remedy= """\t1. Open Utilities
\t\t\t\t\t\t\t\t2. Select Keychain Access
\t\t\t\t\t\t\t\t3. Double-click keychain
\t\t\t\t\t\t\t\t4. Select Access Control
\t\t\t\t\t\t\t\t5. Check box next to "Ask for Keychain Password"""
	retObj.setRemed(remedy)
	return retObj
	
#5.18 Create specialized keychains for different purposes
def specializedKeychains():
	retObj = funcReturn.funcReturn('specializedKeychains')
	remedy= """\t1. Open Utilities
\t\t\t\t\t\t\t\t2. Select Keychain Access
\t\t\t\t\t\t\t\t3. Select File
\t\t\t\t\t\t\t\t4. Select New Keychain
\t\t\t\t\t\t\t\t5. Input name of new keychain next to Save As
\t\t\t\t\t\t\t\t6. Select Create
\t\t\t\t\t\t\t\t7. Drag and drop desired keychain items into new keychain from login keychain"""
	retObj.setRemed(remedy)
	return retObj