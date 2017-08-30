#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex
import re
import funcReturn
import stringFunctions

#Chapter 2.6 Security & Privacy 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tSecurity")
	l.info( "\t\tFileVault")
	retDict = getFileVault ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	
	l.info( "\t\tsetGatekeeperOn")
	retDict = setGatekeeperOn ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + str(comment) )
	
	l.info( "\t\tsetFilewallOn")
	retDict = setFilewallOn ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )

	l.info( "\t\tgetInfrared")
	retDict = getInfrared ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )

	l.info( "\t\tgetSecureKeyboard")
	retObj = getSecureKeyboard ()	
	retVal=retObj.getRetVal()
	comment=retObj.getComment()
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	
	l.info( "\t\tgetJava")
	retDict = getJava ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )

	l.info( "\t\tsetCore")
	retDict = setCore ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
	
def getCore ():
	#launchctl limit core
	dict = {'function' : 'getCore'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	appleCommand = ["launchctl", "limit", "core"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	match = re.search(r'\bcore\b\s+(\d+)\s+(\d+)', result)
	if match:
		dict['found'] = 0
		if 0 == int(match.group(1)) and 0 == int(match.group(2)):
			dict['retVal'] = 0
	dict['result'] = result
	dict['command'] = appleCommand
	return dict	
	
def setCore ():
	#launchctl limit core 0
	dict = {'function' : 'getCore'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	appleCommand = ["launchctl", "limit", "core", "0"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	
	#confirm changes have taken effect
	retDict = getCore()
	dict['retVal']= retDict['retVal']
	dict['comment'] = retDict['comment']
	return dict	
	
def getJava ():
	#java -version	
	dict = {'function' : 'getInfrared'}	
	dict['error'] = ""
	dict['comment'] = """run java -version in terminal window output should be greater than 
						Java version 1.6.0_x"""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	return dict	

def getSecureKeyboard ():
	#defaults read -app Terminal SecureKeyboardEntry
	appleCommand = ["defaults", "read", "-app ", "Terminal", "SecureKeyboardEntry"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getSecureKeyboard')
	error=retObj.getStderr()
	needle="The domain/default pair of"
	if stringFunctions.strFind (error.strip(), needle) != 0:
		comments = """run defaults read -app Terminal SecureKeyboardEntry in terminal window output should be 1
						1. Open Terminal
						2. Select the Terminal Tab from the menu
						3. Select Secure Keyboard Entry"""
	else:
		result = int(retObj.getStdout().strip())
		if result == 1:
			retObj.setRetVal(0)
			comments = ""
	return retObj	
	
def getInfrared ():
	#defaults read /Library/Preferences/com.apple.driver.AppleIRController
	dict = {'function' : 'getInfrared'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['remed'] = """1. Open System Preferences
						2. Select Security & Privacy 
						3. Select the General tab
						4. Select Advanced
						5. Check Disable remote control infrared receiver""" 
	filter = ""
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.driver.AppleIRController"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	for line in result.splitlines():
		dict['line']= line.strip()
		match = re.search(r'(\w+)\s+=\s+(\d+)', dict['line'])
		match2 = re.search(r'(\w+)\s+=\s+(\bnone\b)', dict['line'])
		if match:
			if str(match.group(1)).strip() == "DeviceEnabled":
				setting = int(match.group(2))
				dict['found'] = 0
		if match2:
			if str(match2.group(1)).strip() == "UIDFilter":
				filter = "none"
	if dict['found'] == 0:
		if setting == 0:
			dict['comment'] = "Remote control is disabled"	
			dict['retVal'] = 0
		if setting == 1 and filter == "none":
			dict['comment'] = "Remote control is set to " + str(dict['retVal']) + "filter set to none \n" + dict['remed']
			dict['retVal'] = 1
		else: 
			dict['comment'] = "Remote control is set to " + str(dict['retVal'])
			dict['retVal'] = 0
	else:
		dict['comment'] = "no match found"
	return dict	
	
def getFilewall ():
	#defaults read /Library/Preferences/com.apple.alf globalstate
	dict = {'function' : 'getFilewall'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.alf", "globalstate"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = int(stdout.strip())
	dict['result'] = result
	dict['command'] = appleCommand
	if result == 1 or result == 2:
		dict['retVal']= 0
		dict['comment'] = "Firewall enabled"		
	else:
		dict['retVal']= 1
		dict['comment'] = "Firewall disabled"	
	return dict	

def setFilewallOn ():
	#defaults write /Library/Preferences/com.apple.alf globalstate int 
	dict = {'function' : 'setFilewallOn'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	appleCommand = ["defaults", "write", "/Library/Preferences/com.apple.alf", "globalstate", "2"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	
	#confirm changes have taken effect
	retDict = getFilewall()
	dict['retVal']= retDict['retVal']
	dict['comment'] = retDict['comment']
	return dict	
		
def getFileVault ():
	#diskutil cs list | grep -i encryption
	dict = {'function' : 'getFileVault'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['remed'] = """1. Open System Preferences
						2. Select Security & Privacy
						3. Select FileVault
						4. Select Turn on FileVault"""
	appleCommand = ["diskutil", "cs", "list"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	dict['command'] = appleCommand
	searchString = "ncryption"
	check = result.find(searchString)
	if check == -1:
		dict['retVal']= 1
		dict['comment'] = "No encryption \n \t\t\t\t\t\t" + dict['remed']	
	else:
		dict['retVal']= 0
		dict['comment'] = result
	return dict	

			
def getGatekeeper ():
	#sudo spctl --status
	dict = {'function' : 'getGatekeeper'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	appleCommand = ["sudo", "spctl", "--status"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	dict['command'] = appleCommand
	searchString = "enabled"
	check = result.find(searchString)
	if check == -1:
		dict['retVal']= 1
		dict['comment'] = "assessments not enabled"		
	else:
		dict['retVal']= 0
		dict['comment'] = result
	return dict	
	
def setGatekeeperOn ():
	#sudo spctl --master-enable
	#set getkeeper
	dict = {'function' : 'setGatekeeperOn'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	appleCommand = ["sudo", "spctl", "--master-enable"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	
	#confirm changes have taken effect
	retDict = getGatekeeper()
	dict['retVal']= retDict['retVal']
	dict['comment'] = retDict['retVal']
	return dict	