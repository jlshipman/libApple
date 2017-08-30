#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import dictFunc
import screensaver

############## variable assignments - begin #####################
variableAssign="/scripts/appleBench/LIST/baseVariables.txt"
baseVar = dictFunc.fileToDict(variableAssign, ",")
	
variableAssign="/scripts/appleBench/LIST/variableAssign.txt"
dictVar = dictFunc.fileToDict(variableAssign, "#")
sizeOfBaseDict = len (baseVar)
for x in range(0, sizeOfBaseDict):
	for (n, v) in dictVar.items():
		var = dictVar[n]
		for (key, value) in baseVar.items():
			searchTerm="<"+str(key)+">"
			retVal=var.find(searchTerm)
			if retVal != -1:
				newString = var.replace(searchTerm, value)
				dictVar[n]=newString

for (n, v) in dictVar.items():
	exec('%s=%s' % (n, repr(v)))
############## variable assignments - end #####################

class screenSaverTestCase(unittest.TestCase):
	print "Tests for `screensaver.py`."

	def setUp(self):
		print "\tset up"

	def testGetAllScreen(self):
		print "\ttestGetAllScreen"
		retObj = screensaver.getAllScreen(60, 1200)
		resultDesired = 0
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)		
					
	def testGetAllHotCornerDisable(self):
		print "\ttestGetAllHotCornerDisable"
		retObj = screensaver.getAllHotCornerDisable()
		resultDesired = 0
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)	

	def testSetAllHotCorner(self):
		print "\ttestSetAllHotCornerDisable"
		retObj = screensaver.getAllHotCornerDisable()
		results = retObj.getResult()
		retObj = screensaver.setAllHotCornerDisable(results, 12)
		resultDesired = 0
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)	

	def testGetAllHotCorner(self):
		print "\ttestSetAllHotCornerDisable"
		retObj = screensaver.getAllHotCornerDisable()
		resultDesired = 0
		results = retObj.getResult()
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)	

	def testGetDisplaySleep(self):
		print "\ttestGetDisplaySleep"
		retObj = screensaver.getDisplaySleep()
		resultDesired = 0
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)	
		
	def testSetDisplaySleep(self):
		print "\ttestSetDisplaySleep"
		retObj = screensaver.setDisplaySleep()
		resultDesired = 0
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)	
		
	def testGetSleepCorners(self):
		print "\ttestGetSleepCorners"
		retObj = screensaver.getSleepCorners()
		resultDesired = 0
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)	
		
	def testSetSleepCorners(self):		
		print "\ttestSetSleepCorners"
		retObj = screensaver.getSleepCorners()
		results = retObj.getResult()
		retObj = screensaver.setSleepCorners(results)
		resultDesired = 0
		result = retObj.getResult()
		retVal = retObj.getRetVal()
		comment = retObj.getComment()
		stdout = retObj.getStdout()
		stderr = retObj.getStderr()
		found = retObj.getFound()
		remed = retObj.getRemed()
		command = retObj.getCommand()
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		print "\t\tcommand:   _" + str(command) + "_"
		self.assertEqual(retVal, resultDesired)	
		
	def tearDown(self):
		print "\ttear down"
		print ""

	