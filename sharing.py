#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex


#Chapter 2.4 Sharing 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tSharing")
	l.info( "\t\tRemote Apple Events")
	retDict = getRemoteAppleEvents()
	retVal=retDict['retVal']
	l.info( "\t\t\tretVal: " + str(retVal) )
	if retVal == 1:
		l.info( "\t\Remote Apple Events Turned On")
		retDict=setRemoteAppleEventsOff()
		retVal=retDict['retVal']
		l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\tInternet Sharing")
	retDict = getInternetSharing()
	retVal=retDict['retVal']
	l.info( "\t\t\tretVal: " + str(retVal) )
	if retVal == 1:
		l.info( "\t\tInternet Sharing Turned On")
		retDict=setInternetSharingOff()
		retVal=retDict['retVal']
		l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\tPrinter Sharing")
	retDict = getInternetSharing()
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	if retVal == 1:
		l.info( "\t\t\tSA must go to system prefences and set it to OFF")
	l.info( "\t\tRemote Login")
	retDict = getRemoteLogin()
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	l.info( "\t\tDVD Sharing")
	retDict = getDVDsharing()
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	l.info( "\t\tFile Sharing")
	retDict = getFileSharing()
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	l.info( "\t\tRemote Management")
	retDict = getRemoteManagement ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	
def getRemoteAppleEvents ():
	dict = {'function' : 'getRemoteAppleEvents'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "systemsetup", "-getremoteappleevents"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	desiredAnswer = "Remote Apple Events: Off"
	if result != desiredAnswer:
		dict['retVal'] = 1
	return dict
		
def setRemoteAppleEventsOff ():
	dict = {'function' : 'setRemoteAppleEventsOff'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "systemsetup", "-setremoteappleevents", "off"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	wrongAnswer = "setremoteappleevents: On"
	if result == wrongAnswer:
		dict['retVal'] = 1
		dict['error'] = result
	return dict
	
def getInternetSharing ():
	#sudo defaults read /Library/Preferences/SystemConfiguration/com.apple.nat | grep -i Enabled
	dict = {'function' : 'getInternetSharing'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "defaults", "read", "/Library/Preferences/SystemConfiguration/com.apple.nat"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stderr.strip()
	dict['result'] = result
	searchString = "nabled"
	check = result.find(searchString)
	if check == -1:
		dict['retVal']= 0
		dict['comment'] = "Internet sharing is disabled"		
	else:
		dict['retVal']= 1
		dict['comment'] = "Internet sharing is enabled"
	return dict
	
def setInternetSharingOff ():
	#sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.nat NAT -dict Enabled -int 0
	#sudo launchctl unload -w /System/Library/LaunchDaemons/ com.apple.InternetSharing.plist
	dict = {'function' : 'setInternetSharingOff'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "systemsetup", "-setremoteappleevents", "off"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	wrongAnswer = "setremoteappleevents: On"
	if result == wrongAnswer:
		dict['retVal'] = 1
		dict['error'] = result
	return dict
	
def getPrinterSharing ():
	#sudo system_profiler SPPrintersDataType
	dict = {'function' : 'getPrinterSharing'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "system_profiler", "SPPrintersDataType"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	searchString = "The printers list is empty"
	check = result.find(searchString)
	if check == -1:
		dict['retVal']= 1
		dict['comment'] = "Printer sharing is enabled"		
	else:
		dict['retVal']= 0
		dict['comment'] = "Printer sharing is disabled"
	return dict
	
def getRemoteLogin ():
	#sudo systemsetup -getremotelogin
	dict = {'function' : 'getRemoteLogin'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "systemsetup", "getremotelogin"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	searchString = "Off"
	check = result.find(searchString)
	if check == -1:
		dict['retVal']= 1
		dict['comment'] = "Remote Login is enabled"		
	else:
		dict['retVal']= 0
		dict['comment'] = "Remote Login is disabled"
	return dict
	
def setRemoteLoginOff ():
	#sudo systemsetup -setremotelogin off
	dict = {'function' : 'setRemoteLoginOff'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "systemsetup", "-setremotelogin", "off"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	return dict

def getDVDsharing ():
	#sudo launchctl list | egrep ODSAgent
	dict = {'function' : 'getDVDsharing'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "launchctl", "list"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	result = stdout
	searchString = "ODSAgent"
	check = result.find(searchString)
	if check == -1:
		dict['retVal']= 0
		dict['comment'] = "DVD sharing is disabled"		
	else:
		dict['retVal']= 1
		dict['comment'] = "DVD sharing is enabled"
	return dict
	
def getFileSharing ():
	#sudo launchctl list | egrep '(ftp|nmdb|smdb|AppleFileServer)'
	dict = {'function' : 'getFilesharing'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["sudo", "launchctl", "list"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	result = stdout
	searchString = "ftp"	
	check = result.find(searchString)
	if check == -1:
		if dict['retVal']== 0:
			dict['retVal']= 0
		dict['comment'] = dict['comment'] + "ftp sharing is disabled \n"		
	else:
		dict['retVal']= 1
		dict['comment'] = dict['comment'] + "ftp sharing is enabled \n"
		
	searchString = "nmdb"
	check = result.find(searchString)
	if check == -1:
		if dict['retVal']== 0:
			dict['retVal']= 0
		dict['comment'] = dict['comment'] + "\t\t\t\t\t\t\tnmdb sharing is disabled \n"		
	else:
		dict['retVal']= 1
		dict['comment'] = dict['comment'] + "\t\t\t\t\t\t\tnmdb sharing is enabled \n"
		
	searchString = "smdb"
	check = result.find(searchString)
	if check == -1:
		if dict['retVal']== 0:
			dict['retVal']= 0
		dict['comment'] = dict['comment'] + "\t\t\t\t\t\t\tsmdb sharing is disabled \n"		
	else:
		dict['retVal']= 1
		dict['comment'] = dict['comment'] + "\t\t\t\t\t\t\tsmdb sharing is enabled \n"
		
	searchString = "AppleFileServer"
	check = result.find(searchString)
	if check == -1:
		if dict['retVal']== 0:
			dict['retVal']= 0
		dict['comment'] = dict['comment'] + "\t\t\t\t\t\t\tApple File Server is disabled \n"		
	else:
		dict['retVal']= 1
		dict['comment'] = dict['comment'] + "\t\t\t\t\t\t\tApple File Server is enabled \n"

	return dict
	
def getRemoteManagement ():
	#ps -ef | egrep ARDAgent
	dict = {'function' : 'getRemoteManagement'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 0
	appleCommand = ["ps", "-ef"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	result = stdout
	searchString = "ARDAgent"
	check = result.find(searchString)
	if check == -1:
		dict['retVal']= 0
		dict['comment'] = "Remote Management is disabled"		
	else:
		dict['retVal']= 1
		dict['comment'] = "Remote Management is enabled"
	return dict
