#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import file
import funcReturn

class fileTestCase(unittest.TestCase):
	print "Tests for `file.py`."

	def setUp(self):
		print ""
		print "\tset up"	
		print ""

	def testGetFileExt(self):
 		print "\ttestGetFileExt"
 		retObj = file.getFileExt()
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
 
 	def testSetFileExt(self):
 		print "\ttestSetFileExt"
 		retObj = file.setFileExt()
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
	