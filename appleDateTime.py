#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import re
import funcReturn

#Chapter 2.2 Date & Time    10.11 CIS Benchmark
def run (l, TEMP, timeserver):
	l.info( "\tDate Time")
	l.info( "\t\tTime Server")
	retObj=getTimeServer (timeserver)
	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\t\tTime server NOT set")
		retObj=setTimeServer (timeserver)
		if retVal == 1:
			l.info( "\t\t\t\tTime server NOT set")
		else:
			l.info( "\t\t\t\tTime server set")
	else:
		l.info( "\t\t\tTime server set")
		
	l.info( "\t\tTime Server Automactic Settings")
	retObj=getAutomatically ()
	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\t\tTime server is NOT automatically set")
		retObj=setAutomatically ()
		retVal=retObj.getRetVal()
		if retVal == 1:
			l.info( "\t\t\t\tTime server is NOT automatically set")
		else:
			l.info( "\t\t\t\tTime server is automatically set")
	else:
		l.info( "\t\t\tTime server is automatically set")
			
#2.2.1 Enable "Set time and date automatically" (Not Scored)
def getAutomatically ():
	#sudo systemsetup -getusingnetworktime
	appleCommand = ["sudo", "systemsetup",  "-getusingnetworktime"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getAutomatically')
	stdout=retObj.getStdout().strip()
	if stdout == "Network Time: On":
		retObj.setRetVal(0)
		retObj.setResult ("Network Time: On")
	else:
		retObj.setResult ("Network Time: Off")
	return retObj

#2.2.1 Enable "Set time and date automatically" (Not Scored)				
def setTimeServer (timeserver):
	#sudo systemsetup -setnetworktimeserver <timeserver>
	appleCommand = ["sudo", "systemsetup",  "setnetworktimeserver", timeserver.strip()]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setTimeServer')
	stdout=retObj.getStdout().strip()
	stderr=retObj.getStderr().strip()
	if stdout == "setNetworkTimeServer: " + timeserver.strip():
		retObj.setRetVal(0)
		retObj.setResult ("Network Time is set to " + timeserver)
	else:
		retObj.setResult ("Network Time is not set to " + timeserver)
	return retObj

#2.2.1 Enable "Set time and date automatically" (Not Scored)	
def setAutomatically ():
	#sudo systemsetup -setnetworktimeserver on
	appleCommand = ["sudo", "systemsetup",  "-setnetworktimeserver", "on"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setAutomatically')
	stdout=retObj.getStdout().strip()
	if stdout == "setNetworkTimeServer: on":
		retObj.setRetVal(0)
		retObj.setResult ("Network time automatically set")
	else:
		retObj.setResult ("Network time NOT automatically set")
	return retObj
	
#2.2.2 Ensure time set is within appropriate limits (Scored)
def getTimeServer (timeserver):
	#sudo systemsetup -getnetworktimeserver
	appleCommand = ["sudo", "systemsetup",  "getnetworktimeserver"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getTimeServer')
	stdout=retObj.getStdout().strip()
	stderr=retObj.getStderr().strip()
	if stdout == "Network Time Server: " + timeserver.strip():
		retObj.setRetVal(0)
		retObj.setResult ("Network Time is set to " + timeserver)
	else:
		retObj.setResult ("Network Time is not set to " + timeserver)
	return retObj