#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import uuid
import re
import appleUsers
import funcReturn
import dictFunc

#2.3 Desktop & Screen Saver  10.11 CIS Benchmark  
def run (l, TEMP, dictVar):

	for (n, v) in dictVar.items():
		exec('%s=%s' % (n, repr(v)))
		
	l.info( "\tDesktop & Screen Saver")
	l.info( "\t\tGet Screen Saver")
	retObj=getAllScreen(secondsMore, secondsLess)
	retVal=retObj.getRetVal()
	results = retObj.getResult()
	if retVal == 1:
		l.info( "\t\t\tScreensavers set inaccurately")
		retObj=setAllScreen(results, secondsMore, secondsLess, secondScreen)
	else:
		l.info( "\t\t\tScreensaver set accurately")		
 		for n, p, s in results:
			l.info ( "\t\t\t\tuser:  "+ str(n) + "   seconds:  " + str(s))
			
	l.info( "\t\tGet Screen Saver")
	retObj=getAllHotCorner()
	retVal=retObj.getRetVal()
	results = retObj.getResult()
	if retVal == 1:
		l.info( "\t\t\Hot Conners are set inaccurately")
		retObj=setAllHotCorner(results, 12)
	else:
		l.info( "\t\t\Hot Conners set accurately")
 		for user, pref, setting in results:
			l.info ( "\t\t\t\tuser:  "+ str(user) + "   pref:  " + str(pref) + "   setting:  " + str(setting))
			
			
#2.3.1 Set an inactivity interval of 20 minutes or less for the screen saver
def getAllScreen(saverSecondsMore, saverSecondsLess):
	retObj = funcReturn.funcReturn('getAllScreen')
	retObjUUID = appleUsers.getUUID()
	UUID = retObjUUID.getResult()
	retObjUsers = appleUsers.getUsers()
	usersList = retObjUsers.getResult()
	result = []
	check = 0
	for i in usersList:
		pref = "/Users/" + i + "/Library/Preferences/ByHost/com.apple.screensaver." + UUID + ".plist"
		#print pref
		if os.path.isfile(pref) == True:
			#defaults read $PREF.plist idleTime
			appleCommand = ["defaults", "read", pref, "idleTime"]
			retObj = comWrap.comWrapRetObj(appleCommand)
			retObj.setName('getAllScreen')
			stdout=retObj.getStdout().strip()
			stderr=retObj.getStderr().strip()
			result.append([i, pref, stdout])	
			if check == 0:
				if int(stdout) >= int(saverSecondsMore) and int(stdout) <= int(saverSecondsLess):
					check = 0
				else:
					check = 1
	retObj.setRetVal(check)
	retObj.setResult(result)
	return retObj	

#2.3.1 Set an inactivity interval of 20 minutes or less for the screen saver
def setAllScreen(getlist, secondsMore, secondsLess, seconds):
	retObj = funcReturn.funcReturn('setAllScreen')
	for pref, time in getlist:
		if int(time) < secondsMore or int(time) > secondsLess:
			#defaults write $PREF.plist idleTime seconds
			appleCommand = ["defaults", "write", pref, "idleTime", str(time)]
			retObj = comWrap.comWrapRetObj(appleCommand)
			retObj.setName('setAllScreen')
			stdout=retObj.getStdout().strip()
			stderr=retObj.getStderr().strip()
	retObj.setRetVal = 0
	return retObj	
	
#2.3.2 Secure screen saver corners - check for disable screen saver (Scored)
def getAllHotCornerDisable():
	retObj = funcReturn.funcReturn('getAllHotCorner')
	#defaults read com.apple.dock wvous-bl-corner
	import sys,pwd,os
	retObjUUID = appleUsers.getUUID()
	UUID = retObjUUID.getResult()
	retObjUsers = appleUsers.getUsers()
	usersList = retObjUsers.getResult()
	result = []
	checkAll = 0
	for i in usersList:
		pref = "/Users/" + i + "/Library/Preferences/com.apple.dock.plist"
		cornerList = ["wvous-bl-corner", "wvous-br-corner", "wvous-tl-corner", "wvous-tr-corner"]
		if os.path.isfile(pref) == True:
			for c in cornerList:
				appleCommand = ["defaults", "read", pref, c]
				retObj = comWrap.comWrapRetObj(appleCommand)
				retObj.setName('getAllHotCorner')
				stdout=retObj.getStdout().strip()
				stderr=retObj.getStderr().strip()
				unsetResponse = "does not exist"
				check = stdout.find(unsetResponse)
				if check == -1:
					if stdout != "":
						stdoutInt = int (stdout)
						if stdoutInt == 6:
							checkAll = 1
							result.append([i, pref, stdout, c])
			
	retObj.setRetVal(checkAll)
	retObj.setResult(result)
	return retObj

#2.3.2 Secure screen saver corners - check for disable screen saver (Scored)
def setAllHotCornerDisable(getlist, hotCornerSetting):
	retObj = funcReturn.funcReturn('setAllHotCorner')
	for user, pref, setting, c in getlist:
		if int(setting) == 6:
			appleCommand = ["defaults", "write", pref, c, str(hotCornerSetting)]
			retObj = comWrap.comWrapRetObj(appleCommand)
			retObj.setName('setAllHotCorner')
			stdout=retObj.getStdout().strip()
			stderr=retObj.getStderr().strip()
	retObj.setRetVal(0)
	return retObj	
	
#2.3.3 Verify Display Sleep is set to a value larger than the Screen Saver
def getDisplaySleep ():
	#sudo systemsetup -getdisplaysleep
	appleCommand = ["sudo", "systemsetup", "-getdisplaysleep"]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('getDisplaySleep')
	stdout=retObj.getStdout().strip()
	stderr=retObj.getStderr().strip()
	resultList = re.findall(r'\d+', stdout)
	if len(resultList) == 1:
		minutes = resultList[0]
		resultInSeconds = 60 * int(minutes)
		if resultInSeconds >= 0:
			retObj.setComment ("Display sleep set to: " + str(resultInSeconds) + " seconds")
			retObj.setResult(str(resultInSeconds))
			retObj.setRetVal(0)
		else:
			retObj.setComment ("Display sleep is not set")
	else:
		retObj.setComment ("Should only be one number")
	return retObj
	
#2.3.3 Verify Display Sleep is set to a value larger than the Screen Saver
def setDisplaySleep (minutes = 15):
	#sudo systemsetup -setDisplaySleep minutes
	appleCommand = ["sudo", "systemsetup", "-setDisplaySleep", str(minutes)]
	retObj = comWrap.comWrapRetObj(appleCommand)
	retObj.setName('setDisplaySleep')
	stdout=retObj.getStdout().strip()
	stderr=retObj.getStderr().strip()
	resultList = re.findall(r'\d+', stdout)
	if len(resultList) == 1:
		minutes = resultList[0]
		resultInSeconds = 60 * int(minutes)
		if resultInSeconds >= 0:
			retObj.setComment ("Display sleep set to: " + str(resultInSeconds) + " seconds")
			retObj.setResult(str(resultInSeconds))
			retObj.setRetVal(0)
		else:
			retObj.setComment ("Display sleep is not set")
	else:
		retObj.setComment ("Should only be one number")
	return retObj

#2.3.4 Set a screen corner to Start Screen Saver (Scored)
def getSleepCorners ():
	retObj = funcReturn.funcReturn('getSleepCorners')
	#	#defaults read com.apple.dock wvous-bl-corner
	import sys,pwd,os
	retObjUUID = appleUsers.getUUID()
	UUID = retObjUUID.getResult()
	retObjUsers = appleUsers.getUsers()
	usersList = retObjUsers.getResult()
	result = []
	checkAll = 0
	for i in usersList:
		pref = "/Users/" + i + "/Library/Preferences/com.apple.dock.plist"
		cornerList = ["wvous-bl-corner", "wvous-br-corner", "wvous-tl-corner", "wvous-tr-corner"]
		if os.path.isfile(pref) == True:
			for c in cornerList:
				appleCommand = ["defaults", "read", pref, c]
				retObj = comWrap.comWrapRetObj(appleCommand)
				retObj.setName('getAllHotCorner')
				stdout=retObj.getStdout().strip()
				stderr=retObj.getStderr().strip()
				unsetResponse = "does not exist"
				check = stdout.find(unsetResponse)
				if check == -1:
					if stdout != "":
						stdoutInt = int (stdout)
						if stdoutInt == 5:
							checkAll = 1
			if checkAll != 1:
				#a user does not have a corner set for screen sleep
				result.append([i, pref])
				checkAll = 1
			else:
				checkAll = 0
						
	retObj.setRetVal(checkAll)
	retObj.setResult(result)
	return retObj
	
#2.3.4 Set a screen corner to Start Screen Saver (Scored)
def setSleepCorners(getlist, corner = "wvous-bl-corner"):
	retObj = funcReturn.funcReturn('setSleepCorners')
	for user, pref in getlist:
		appleCommand = ["defaults", "write", pref, corner, "5"]
		retObj = comWrap.comWrapRetObj(appleCommand)
		retObj.setName('setSleepCorners')
		stdout=retObj.getStdout().strip()
		stderr=retObj.getStderr().strip()
	retObj.setRetVal(0)
	return retObj