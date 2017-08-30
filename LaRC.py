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

def run (l, TEMP):
	l.info( "\tLaRC")
	l.info( "\t\tcheckSplunk")
	retObj = checkSplunk ()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	
	l.info( "\t\tcheckKACE")
	retObj = checkKACE ()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))

	l.info( "\t\tgetFirewallStatus")
	retObj = getFirewallStatus ()
	retVal = retObj.getRetVal()
	l.info( "\t\t\tretVal: " + str(retVal))
	if retVal == 1:
		l.info( "\t\tsetFirewallLevel")
		retObj = setFirewallLevel ()

	l.info( "\t\tgetOpenPorts")
	retObj = getOpenPorts ()
	retVal = retObj.getRetVal()
	results = retObj.getResult()
	l.info("results:  " + results)
	
def getOpenPorts ():
	#lsof -i | grep LISTEN
	retObj = funcReturn.funcReturn('getOpenPorts')
	appleCommand = ["lsof", "-i"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getOpenPorts')
	resultAll = retObj.getStdout().strip()
	result = resultAll.split("\n")
	results = ""
	word = "LISTEN"
	for r in result:
		if word in r:
			results = results + r + "\n"
	retObj.setResult(results)
	retObj.setRetVal(0)
	return retObj		
	
def getFirewallStatus ():
	#defaults read /Library/Preferences/com.apple.alf globalstate 
	retObj = funcReturn.funcReturn('getFirewallStatus')
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.alf", "globalstate"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getFirewallStatus')
	result = int(retObj.getStdout().strip())
	if result > 0:
		retObj.setRetVal(0)
	return retObj	
	
def setFirewallLevel ():
	#sudo defaults write /Library/Preferences/com.apple.alf globalstate -int 2
	retObj = funcReturn.funcReturn('setFirewallLevel')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.alf", "globalstate", "-int", "2"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setFirewallLevel')
	retObj.setRetVal(0)
	return retObj	
				
def checkSplunk ():
	retObj = funcReturn.funcReturn('checkSplunk')
	appleCommand = ["ps", "-ef"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('checkSplunk')
	result = retObj.getStdout().strip()
	count = 0
	comment = ""
	if result != "":
		resultList=result.split("\n" )
		needle="splunkd"
		for r in resultList:
			if needle in r:
				count += 1
				comment += r.strip() + "\n"
	comment=comment.rstrip('\n')		
	retObj.setComment(comment)
	if count == 2:
		retObj.setRetVal(0)
	return retObj	

def checkKACE ():
	retObj = funcReturn.funcReturn('checkKACE')
	appleCommand = ["ps", "-ef"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('checkKACE')
	result = retObj.getStdout().strip()
	count = 0
	comment = ""
	if result != "":
		resultList=result.split("\n" )
		needle="AMPAgent"
		for r in resultList:
			if needle in r:
				count += 1
				comment += r.strip() + "\n"
	comment=comment.rstrip('\n')
	retObj.setComment(comment)
	if count == 2:
		retObj.setRetVal(0)
	return retObj	