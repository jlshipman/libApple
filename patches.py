#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import commandwrapper
import platform
import funcReturn

#Chapter 1 Install Updates, Patches and Additional Security Software  10.11 CIS Benchmark 
def run (l, TEMP):
	l.info( "\tPatches")
	l.info( "\t\tSystem Updates")
	retObj=systemUpdates (TEMP)
	retVal=retObj.getRetVal()
	comment = retObj.getComment()
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: _" + comment + "_")
	if retVal == 1:
		l.info( "\t\t\tNew Software available")
	else:
		l.info( "\t\t\tNo New Software available")
			
	l.info( "\t\tCheck Auto System Updates")
	retObj=getAutoUpdate ()
	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\tSet Auto System Updates")
		retObj=setAutoUpdate (TEMP)
		retVal=retObj.getRetVal()
		comment = retObj.getComment()
		l.info( "\t\t\tretVal: " + str(retVal) )
		l.info( "\t\t\tcomment: _" + comment + "_")
		if retVal == 1:
			l.info( "\t\t\tAuto System Updates are not set")
		else:
			l.info( "\t\t\tAuto System Updates are set")
	else:
		l.info( "\t\t\tAuto System Updates are set")
		

	l.info( "\t\tCheck Auto App Updates")
	retObj=getAppUpdate ()
	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\tSet Auto App Updates")
		retObj=setAppUpdate (TEMP)
		retVal=retObj.getRetVal()
		comment = retObj.getComment()
		l.info( "\t\t\tretVal: " + str(retVal) )
		l.info( "\t\t\tcomment: _" + comment + "_")
		if retVal == 1:
			l.info( "\t\t\tAuto App Updates are not set")
		else:
			l.info( "\t\t\tAuto App Updates are set")
	else:
		l.info( "\t\t\tAuto App Updates are set")
		
	l.info( "\t\tCheck Security Updates")
	retObj=getSecurityUdates ()
	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\tSet Security Updates")
		retObj=setSecurityUdates ()
		retVal=retObj.getRetVal()
		comment = retObj.getComment()
		l.info( "\t\t\tretVal: " + str(retVal) )
		l.info( "\t\t\tcomment: _" + comment + "_")
		if retVal == 1:
			l.info( "\t\t\tSecurity Updates are not set")
		else:
			l.info( "\t\t\tSecurity Updates are set")
	else:
		l.info( "\t\t\tSecurity Updates are set")
		
	l.info( "\t\tAuto Updates Restarts")
	retObj=getAutoUpdateRestartRequired ()
	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\t\tSet Auto Updates Restarts")
		retObj=setAutoUpdateRestartRequired ()
		retVal=retObj.getRetVal()
		comment = retObj.getComment()
		l.info( "\t\t\t\tretVal: " + str(retVal) )
		l.info( "\t\t\t\tcomment: _" + comment + "_")
		if retVal == 1:
			l.info( "\t\t\t\tAuto Updates restart are not set")
		else:
			l.info( "\t\t\t\tAuto Updates restart are set")
	else:
		l.info( "\t\t\tAuto Updates restart are set")		

#1.1 Verify all Apple provided software is current
#alternative solution to using softwareupdate -l
def systemUpdates (tempDir):
	retObj = funcReturn.funcReturn('systemUpdates')
	tempFile = tempDir + "systemUpdates.txt"
	appleCommand = ["sudo", "softwareupdate", "-l",  ">",  " + tempFile + " , "2>&1 "]
	retObj = comWrap.comWrapRetObj(appleCommand)  
	retObj.setName('systemUpdates')
	result = retObj.getStdout().strip()
	f = open (tempFile, "r")
	resultString = f.read()
	f.close ()
	retObj.setResult (resultString.strip())
	searchString = "No new software available"
	check = resultString.find(searchString)
	if check == -1:
		retObj.setRetVal(1)
		retObj.setResult ("new software available")
	else:
		retObj.setRetVal(0)
		retObj.setResult (searchString)
	return retObj

#1.2 Enable Auto Update
def getAutoUpdate ():
	#defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled
	retObj = funcReturn.funcReturn('getAutoUpdate')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.SoftwareUpdate", "AutomaticCheckEnabled"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getAutoUpdate')
	result = retObj.getStdout().strip()
	if int(result) == 1:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj	

#1.2 Enable Auto Update
def setAutoUpdate (tempDir):
	#sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled -int 1
	retObj = funcReturn.funcReturn('setAutoUpdate')
	tempFile = tempDir + "schedule.txt"
	appleCommand = ["sudo", "softwareupdate", "--schedule",  ">",  " + tempFile + " , "2>&1 "]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setAutoUpdate')
	f = open (tempFile, "r")
	resultString = f.read()
	f.close ()
	retObj.setResult (resultString.strip())
	retObj.setCommand (appleCommand)
	searchString = "Automatic check is off"
	check = resultString.find(searchString)
	if check == -1:
		retObj.setRetVal(0)
		retObj.setResult ("Automatic check is on")
	else:
		retObj.setRetVal(1)
		retObj.setResult (searchString)
	return retObj

#1.3 Enable app update installs
def getAppUpdate ():
	#defaults read /Library/Preferences/com.apple.commerce AutoUpdate
	retObj = funcReturn.funcReturn('getAppUpdate')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.commerce", "AutoUpdate"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getAppUpdate')
	result = retObj.getStdout().strip()
	if int(result) == 1:
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj

def setAppUpdate ():
	#sudo defaults write /Library/Preferences/com.apple.commerce AutoUpdate -bool TRUE
	retObj = funcReturn.funcReturn('setAppUpdate')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.commerce", "AutoUpdate", "-bool", "TRUE"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setAppUpdate')
	result = retObj.getStdout().strip()
	if result == "":
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj

#1.4 Enable system data files and security update installs		
def getSecurityUdates():
	#defaults read /Library/Preferences/com.apple.SoftwareUpdate | egrep '(ConfigDataInstall|CriticalUpdateInstall)'
	retObj = funcReturn.funcReturn('getSecurityUdates')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.SoftwareUpdate"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getSecurityUdates')
	result=retObj.getStdout ()
	retObj.setCommand (appleCommand)
	searchString1 = "ConfigDataInstall = 1"
	check1 = result.find(searchString1)
	searchString2 = "CriticalUpdateInstall = 1"
	check2 = result.find(searchString2)
	if check1 == -1 and check2 == -1:
		retObj.setRetVal(1)
		retObj.setResult ("System Updates are not set")
	else:
		retObj.setRetVal(0)
		retObj.setResult ("System Updates are set")
		
	return retObj

def setSecurityUdates ():
	#sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate ConfigDataInstall -bool true 
	#sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall -bool true					
	retObj = funcReturn.funcReturn('setSecurityUdates')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "ConfigDataInstall", "-bool", "TRUE"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setAppUpdate')
	result1 = retObj.getStdout().strip()
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.SoftwareUpdate", "CriticalUpdateInstall", "-bool", "TRUE"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setAppUpdate')
	result2 = retObj.getStdout().strip()	
	if result1 == "" and result2 == "":
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj	

#1.5 Enable OS X update installs (Scored)
def getAutoUpdateRestartRequired ():
	#defaults read /Library/Preferences/com.apple.commerce AutoUpdateRestartRequired
	retObj = funcReturn.funcReturn('getAutoUpdateRestartRequired')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.commerce", "AutoUpdateRestartRequired"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getAutoUpdateRestartRequired')
	result = retObj.getStdout().strip()
	if result == "1":
		retObj.setRetVal(0)
	else:
		retObj.setRetVal(1)
	return retObj	

#1.5 Enable OS X update installs (Scored)
def setAutoUpdateRestartRequired ():
	#sudo defaults write /Library/Preferences/com.apple.commerce AutoUpdateRestartRequired -bool TRUE
	retObj = funcReturn.funcReturn('setAutoUpdateRestartRequired')
	appleCommand = ["sudo", "defaults", "read", "/Library/Preferences/com.apple.commerce", "AutoUpdateRestartRequired", "-bool", "TRUE"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setAutoUpdateRestartRequired')
	retObj.setRetVal(0)
	return retObj	
		
def appleVersion ():
	retObj = funcReturn.funcReturn('appleVersion')
	retObj.setRetVal(0)
	v, _, _ = platform.mac_ver()
	retObj.setResult (v)
	pieces=v.split('.')
	retObj.setComment(pieces[1])
	return retObj


