#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex
import re
import funcReturn

def run (l, TEMP):
	l.info( "\tApple Setup")
	l.info( "\t\tComputer Name")
	retObj = getComputerName ()	
	retVal=retObj.getRetVal()
	comment = retObj.getComment()
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: _" + comment + "_")
	
	l.info( "\t\tHost Name")
	retObj = getHostName ()	
	retVal=retObj.getRetVal()
	comment = retObj.getComment()
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: _" + comment + "_")
	
	l.info( "\t\tLocal Host Name")
	retObj = getLocalHostName ()	
	retVal=retObj.getRetVal()
	comment = retObj.getComment()
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: _" + comment + "_")


def getComputerName():
	#scutil --get ComputerName 
	retObj = funcReturn.funcReturn('getComputerName')
	appleCommand = ["scutil", "--get", "ComputerName"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getComputerName')
	result = retObj.getStdout().strip()
	if result != "":
		retObj.setRetVal(0)
		retObj.setComment ("Computer Name is set to: " + result)
	else:
		retObj.setRetVal(1)
		retObj.setComment ( """Computer Name is not set
							necessary for Active Directory Binding
		""")
	retObj.setResult (result)
	return retObj	
	
def getHostName():
	#scutil --get HostName 
	retObj = funcReturn.funcReturn('getHostName')
	appleCommand = ["scutil", "--get", "HostName"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getHostName')
	result = retObj.getStdout().strip()
	if result != "":
		retObj.setRetVal(0)
		retObj.setComment ("Host Name is set to: " + result)
	else:
		retObj.setRetVal(1)
		retObj.setComment ( """Host Name is not set
						necessary for Active Directory Binding
		""")
	retObj.setResult (result)
	return retObj	
	
def getLocalHostName():
	#scutil --get LocalHostName 
	retObj = funcReturn.funcReturn('LocalHostName')
	appleCommand = ["scutil", "--get", "LocalHostName"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('LocalHostName')
	result = retObj.getStdout().strip()
	if result != "":
		retObj.setRetVal(0)
		retObj.setComment ("Local Host Name is set to: " + result)
	else:
		retObj.setRetVal(1)
		retObj.setComment ( """Local Host Name is not set
						necessary for Active Directory Binding
		""")
	retObj.setResult (result)
	return retObj

	
