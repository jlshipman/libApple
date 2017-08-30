#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import commandwrapper
	
def bluetooth (tempDir):
	dict = {'function' : 'bluetooth'}
	dict['retVal'] = 0
	dict['error'] = ""
	dict['comment'] = ""
	tempFile = tempDir + "bluetooth.txt"
	appleCommand = "defaults read /Library/Preferences/com.apple.Bluetooth ControllerPowerState >"+ tempFile + " 2>&1  "
	result = comWrap.comWrap(appleCommand)  
	f = open (tempFile, "r")
	resultString = f.read()
	f.close ()
	dict['command']= resultString.strip()
	searchString = "0"
	check = resultString.find(searchString)
	if check == -1:
		dict['retVal']= 1
		dict['comment'] = "bluetooth is enabled"
	else:
		dict['retVal']= 0
		dict['comment'] = "bluetooth is disabled"
	return dict

def bluetoothDisable(tempDir):
	dict = {'function' : 'bluetoothDisable'}
	dict['retVal'] = 0
	dict['error'] = ""
	dict['comment'] = ""
	appleCommand = "sudo defaults write /Library/Preferences/com.apple.Bluetooth ControllerPowerState -int 0"
	result = comWrap.comWrap(appleCommand)  
	appleCommand = "sudo killall -HUP blued"
	result = comWrap.comWrap(appleCommand)	
	retDict=bluetooth (tempDir)
	if retDict['retVal'] == 0:
		dict['retVal']= 0
		dict['comment'] = "bluetooth is disabled"
	else:
		dict['retVal']= 1
		dict['comment'] = "bluetooth is enabled"
	return dict
		
# def bluetoothPaired (tempDir):
# 	dict = {'function' : 'bluetoothPaired'}
# 	dict['retVal'] = 0
# 	dict['error'] = ""
# 	dict['comment'] = ""
# 	tempFile = tempDir + "bluetoothPaired.txt"
# 	appleCommand = "defaults read /Library/Preferences/com.apple.Bluetooth ControllerPowerState"+ tempFile + " 2>&1  "
# 	#appleCommand = "system_profiler | grep 'Bluetooth:' -A 20 | grep Connectable" + tempFile + " 2>&1"
# 	result = comWrap.comWrap(appleCommand)  
# 	f = open (tempFile, "r")
# 	resultString = f.read()
# 	f.close ()
# 	dict['command']= resultString.strip()
# 	searchString = "Yes"
# 	check = resultString.find(searchString)
# 	if check == -1:
# 		dict['retVal']= 1
# 		dict['comment'] = "bluetooth is not paired"
# 	else:
# 		dict['retVal']= 0
# 		dict['comment'] = "bluetooth is paired"
# 	return dict