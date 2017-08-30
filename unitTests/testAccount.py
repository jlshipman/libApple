#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import accounts
import funcReturn

class accountsTestCase(unittest.TestCase):
	print "Tests for `account.py`."

	def setUp(self):
		print ""
		print "\tset up"	
		print ""

	def testGetDisableGuestSMB(self):
 		print "\ttestGetDisableGuestSMB"
 		retObj = accounts.getDisableGuestSMB()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"
 		
	def testSetDisableGuestSMB(self):
 		print "\ttestSetDisableGuestSMB"
 		retObj = accounts.setDisableGuestSMB()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"	
 		
	def testGetDisableGuestAFP(self):
 		print "\ttestGetDisableGuestAFP"
 		retObj = accounts.getDisableGuestAFP()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"

	def testSetDisableGuestAFP(self):
 		print "\ttestSetDisableGuestAFP"
 		retObj = accounts.setDisableGuestAFP()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"

 		
	def testGetDisableGuest(self):
 		print "\ttestGetDisableGuest"
 		retObj = accounts.getDisableGuest()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"

	def testSetDisableGuest(self):
 		print "\ttestSetDisableGuest"
 		retObj = accounts.setDisableGuest()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"
 				
	def testGetDisableHints(self):
 		print "\ttestGetDisableHints"
 		retObj = accounts.getDisableHints()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"

	def testSetDisableHints(self):
 		print "\ttestSetDisableHints"
 		retObj = accounts.setDisableHints()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"
 		
	def testGetLoginWindow(self):
 		print "\ttestGetLoginWindow"
 		retObj = accounts.getLoginWindow()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"

	def testSetLoginWindow(self):
 		print "\ttestSetLoginWindow"
 		retObj = accounts.setLoginWindow()
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
 		print "\t\tstdout:  _" + stdout + "_"
 		print "\t\tstderr:  _" + stderr + "_"
 		print "\t\tremed:   _" + remed + "_"
 		print "\t\tfound:   _" + str(found) + "_"
 		
	def tearDown(self):
		print ""
		print "\ttear down"
		print ""
	