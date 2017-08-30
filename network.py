#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex
import re
import plistlib


#Chapter 4 Network Configurations 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tNetwork")
	
	l.info( "\t\tgetBonjour")
	retDict = getBonjour ()	
	retVal=retDict['retVal']
	remed=retDict['remed']
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )

	l.info( "\t\tsetBonjour")
	retDict = setBonjour ()	
	retVal=retDict['retVal']
	remed=retDict['remed']
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )

	l.info( "\t\tgetWifiMenu")
	retDict = getWifiMenu ()	
	retVal=retDict['retVal']
	remed=retDict['remed']
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	
	l.info( "\t\tgetNetworkLocations")
	retDict = getNetworkLocations ()	
	retVal=retDict['retVal']
	remed=retDict['remed']
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )

def getNetworkLocations ():
	dict = {'function' : 'getNetworkLocations' }
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['remed']= """\t1. Select Edit Locations from the Locations popup menu.
\t\t\t\t\t\t\t\t2. Select the Automatic location.
\t\t\t\t\t\t\t\t3. Click the minus button for any unneeded service."""
	return dict
	
def getWifiMenu ():
	dict = {'function' : 'getWifiMenu' }
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['remed']= """\t1. Open System Preferences
\t\t\t\t\t\t\t\t2. Select Network
\t\t\t\t\t\t\t\t3. Check Show Wi-Fi status in menu bar"""
	return dict


def getBonjour():
	#defaults read /Library/Preferences/com.apple.alf globalstate
	dict = {'function' : 'getBonjour' }
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['remed']= ""
	appleCommand = ["defaults", "read", "/Library/Preferences/com.apple.alf", "globalstate"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = int(stdout.strip())
	if result == 1 or result == 2:
		dict['retVal'] = 0
		dict['comment'] = "Bonjour is disabled"
	else:
		dict['comment'] = "Bonjour is enabled"
		dict['retVal'] = 1

	return dict

def setBonjour():
	#defaults read /Library/Preferences/com.apple.alf globalstate
	dict = {'function' : 'getBonjour' }
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['remed']= ""
	
	plistPath = "/System/Library/LaunchDaemons/com.apple.mDNSResponder.plist"
	
	retDict = getBonjour()
	if retDict['retVal'] == 1:
		pl = plistlib.readPlist(plistPath)
		results = pl["ProgramArguments"]
		dict['result'] = results
		item = "-NoMulticastAdvertisements"
		pl["ProgramArguments"].append(item)
		plistlib.writePlist(pl, plistPath)
		retDict = getBonjour()
		if retDict['retVal'] == 0:
			dict['retVal'] = 0
			dict['comment'] = "Bonjour is disabled"
		else:
			dict['comment'] = "Bonjour is enabled"
			dict['retVal'] = 1
	else:
		dict['retVal'] = 0
		dict['comment'] = "Bonjour is disabled"


	return dict
