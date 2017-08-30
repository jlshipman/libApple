#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import security

class securityTestCase(unittest.TestCase):
	print "Tests for `security.py`."

	def setUp(self):
		print "\tset up"	

	def testGetSecureKeyboard(self):
 		print "\ttestGetSecureKeyboard"
 		retObj = security.getSecureKeyboard()
 		result = retObj.getResult()
 		retVal = retObj.getRetVal()
 		comment = retObj.getComment()
 		stdout = retObj.getStdout()
 		stderr = retObj.getStderr()
 		found = retObj.getFound()
 		remed = retObj.getRemed()
 		print "\t\tresult:  _" + str(result)  + "_"
 		print "\t\tretVal:  _" + str(retVal)  + "_"
 		print "\t\tcomment: _" + comment + "_"
 		#print "\t\tstdout:  _" + stdout + "_"
 		#print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"
 		
 		
	def testGetCore(self):
		print "\ttestGetCore"
		retDict = security.getCore()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		found = retDict['found']
		print "\t\ttresult:  _" + result  + "_"
		print "\t\tfound:  _" + str(found)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		
	def testGetInfrared(self):
		print "\ttestgGetInfrared"
		retDict = security.getInfrared()
		result = retDict['result']
		retVal = retDict['retVal']
		remed = retDict['remed']
		comment = retDict['comment']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tremed: _" + remed + "_"
		
	def testGetFileVault(self):
		print "\ttestGetFileVault"
		retDict = security.getFileVault()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"

	def testGetGatekeeper(self):
		print "\ttestGetGatekeeper"
		retDict = security.getGatekeeper()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"

	def testGetFilewallOn(self):
		print "\ttestGetFilewallOn"
		retDict = security.setFilewallOn()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		print "\t\tresult:  _" + str(result)  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		
	def tearDown(self):
		print "\ttear down"

	