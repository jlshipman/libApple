#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import commandwrapper
import os
import funcReturn

#Chapter 2.1 Bluetooth  10.11 CIS Benchmark  
def run (l):
	l.info( "\tBluetooth")
	
	l.info( "\t\tBluetooth Activity Settings")
	retObj=bluetooth ()
	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\t\tBluetooth Turned On")
		retObj=bluetoothDisable ()
		retVal=retObj.getRetVal()
		comment = retObj.getComment()
		l.info( "\t\t\t\tretVal: " + str(retVal) )
		l.info( "\t\t\t\tcomment: _" + comment + "_")
	else:
		l.info( "\t\t\tBluetooth Turned Off")

	l.info( "\t\tBluetooth Discoverable Settings")
 	retObj=getDiscoverable()
 	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\t\tBluetooth is Discoverable")
		comment = retObj.getComment()
		l.info( "\t\t\t\tretVal: " + str(retVal) )
		l.info( "\t\t\t\tcomment: _" + comment + "_")
	else:
		l.info( "\t\t\tBluetooth is not Discoverable")		

	l.info( "\t\tBluetooth Menu Settings")
 	retObj=getMenu ()
 	retVal=retObj.getRetVal()
	if retVal == 1:
		l.info( "\t\t\tBluetooth Menu is not Displayed")
		retObj=setMenu ()
		retVal=retObj.getRetVal()
		comment = retObj.getComment()
		l.info( "\t\t\t\tretVal: " + str(retVal) )
		l.info( "\t\t\t\tcomment: _" + comment + "_")
	else:
		l.info( "\t\t\tBluetooth Menu is Displayed")

#2.1.1 Turn off Bluetooth, if no paired devices exist	
def bluetooth ():
	retObj = funcReturn.funcReturn('bluetooth')
	appleCommand = ["sudo", "defaults", "read", "/Library/Preferences/com.apple.Bluetooth", "ControllerPowerState ", "2>&1"]
	retObj = comWrap.comWrapRetObj(appleCommand) 
	retObj.setName('bluetooth')
	retObj.setCommand (appleCommand)
	resultString=retObj.getStdout().strip() + " " +retObj.getStderr().strip()
	searchString = "0"
	check = resultString.find(searchString)
	if check == -1:
		retObj.setRetVal(1)
		retObj.setResult ("bluetooth is enabled")
	else:
		retObj.setRetVal(0)
		retObj.setResult ("bluetooth is disabled")
	return retObj

#2.1.1 Turn off Bluetooth, if no paired devices exist	
def bluetoothDisable():
	retObj = funcReturn.funcReturn('bluetoothDisable')
	appleCommand = ["sudo", "defaults", "write", "/Library/Preferences/com.apple.Bluetooth", "ControllerPowerState", "-int", "0"]
	retObj = comWrap.comWrapRetObj(appleCommand) 
	retObj.setCommand (appleCommand) 
	appleCommand = ["sudo", "killall", "-HUP", "blued"]
	retObj = comWrap.comWrapRetObj(appleCommand)	
	retObj.setName('bluetoothDisable')
	retObjBlue=bluetooth ()
	if retObjBlue.getRetVal() == 0:
		retObj.setRetVal(0)
		retObj.setResult ("bluetooth is disabled")
	else:
		retObj.setRetVal(1)
		retObj.setResult ("bluetooth is enabled")
	return retObj

#2.1.2 Turn off Bluetooth "Discoverable" mode when not pairing devices
#/usr/sbin/system_profiler SPBluetoothDataType | grep -i discoverable
#discoverable not a return of command
def getDiscoverable():
	retObj = funcReturn.funcReturn('getDiscoverable')
	appleCommand = ["/usr/sbin/system_profiler", "SPBluetoothDataType"]
	retObj = comWrap.comWrapRetObj(appleCommand) 
	retObj.setName('getDiscoverable')
	retObj.setCommand (appleCommand) 
	resultString=retObj.getStdout()
	searchString = "Discoverable: On"
	check = resultString.find(searchString)
	retObjBlue = bluetooth()
	if retObjBlue.getRetVal() == 0:
		retObj.setRetVal(0)
		retObj.setResult ("bluetooth is disabled")
	else:
		if check == -1:
			retObj.setRetVal(0)
			retObj.setResult ("bluetooth is not discoverable")
		else:
			retObj.setRetVal(1)
			retObj.setResult ("bluetooth is discoverable")
	return retObj
	
#2.1.3 Show Bluetooth status in menu bar (Scored)
def getMenu():
	retObj = funcReturn.funcReturn('getMenu')
	appleCommand = ["defaults", "read", "com.apple.systemuiserver", "menuExtras"]
	retObj = comWrap.comWrapRetObj(appleCommand) 
	retObj.setName('getMenu')
	retObj.setCommand (appleCommand) 
	resultString=retObj.getStdout()
	searchString = "Bluetooth.menu"	
	check = resultString.find(searchString)
	if check == -1:
		retObj.setRetVal(1)
		retObj.setResult ("bluetooth Menu Bar is off")		
	else:
		retObj.setRetVal(0)
		retObj.setResult ("bluetooth Menu Bar is on")
	return retObj

#2.1.3 Show Bluetooth status in menu bar (Scored)
def setMenu():
	retObj = funcReturn.funcReturn('setMenu')
	appleCommand = ['defaults', 'write', 'com.apple.systemuiserver', '-array-add', '"/System/Library/CoreServices/Menu Extras/Bluetooth.menu"']
	retObj = comWrap.comWrapRetObj(appleCommand) 
	retObj.setName('setMenu')
	retObj.setCommand (appleCommand) 
	retObjMenu = getMenu()
	retObj.setRetVal(retObjMenu.getRetVal())
	retObj.setResult(retObjMenu.getResult())
	return retObj