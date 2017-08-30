#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex
import re

#Chapter 2.5 Energy Saver 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tEnergy")
	l.info( "\t\tWake")
	retDict = setWakeOff ()
	comment = retDict['comment']
	retVal = retDict['retVal']
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tcomment: " + comment)

def getSleep ():
	#pmset -g | grep sleep
	dict = {'function' : 'getSleep'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['line'] = ""
	dict['text'] = ""
	dict['verbose'] = ""
	dict['found'] = 1
	dict['retVal'] = 1
	appleCommand = ["pmset", "-g"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	dict['command'] = appleCommand
	for line in result.splitlines():
		dict['line']= line.strip()
		match = re.search(r'(\w+)(\s+)(\d+)(.*)', dict['line'])
		if match:
# 			print "match.group(1):  " + str(match.group(1))
# 			print "match.group(2):  " + str(match.group(2))
# 			print "match.group(3):  " + str(match.group(3))
# 			print "match.group(4):  " + str(match.group(4))
			if str(match.group(1)).strip() == "sleep":
#				print "found sleep"
				dict['retVal'] = int(match.group(3))
				dict['found'] = 0
	if dict['found'] == 0:
		if dict['retVal'] == 0:
			dict['comment'] = "Sleep is set to never"	
		else:
			dict['comment'] = "Sleep is set to " + str(dict['retVal'] )
	else:
		dict['comment'] = "no match found"
	return dict	
		
def getWake ():
	#pmset -g
	dict = {'function' : 'getWake'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['line'] = ""
	dict['text'] = ""
	dict['found'] = 1
	dict['retVal'] = 1
	appleCommand = ["pmset", "-g"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	dict['result'] = result
	dict['command'] = appleCommand
	for line in result.splitlines():
		if "womp" in line:
			dict['line']= line.strip()
			(text, value) = line.strip().split()
			dict['retVal'] = int(value)
			dict['text'] = text
			dict['found'] = 0
	if dict['found'] == 0:
		if dict['retVal'] == 0:
			dict['comment'] = "Wake for network access is disabled"	
		else:
			dict['comment'] = "Wake for network access is enabled"
	else:
		dict['comment'] = "no match found"
	return dict	

def setWakeOff ():
	#sudo pmset -a womp 0
	dict = {'function' : 'setWake'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['line'] = ""
	dict['text'] = ""
	dict['found'] = 1
	dict['retVal'] = 1
	appleCommand = ["sudo", "pmset", "-a" "womp", "0"]
	retDict = getWake()
	dict['retVal'] = retDict['retVal']
	dict['comment'] = retDict['comment']
	return dict	
