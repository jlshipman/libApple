#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import apps
import funcReturn

class appsTestCase(unittest.TestCase):
	print "Tests for `apps.py`."

	def setUp(self):
		print ""
		print "\tset up"	
		print ""

	def testGetSafariSafeFilest(self):
 		print "\ttestGetSafariSafeFilest"
 		retObj = apps.getSafariSafeFiles()
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
 
	def testSetSafariSafeFiles(self):
 		print "\ttestSetSafariSafeFiles"
 		retObj = apps.setSafariSafeFiles()
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
	