#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import javaCheck

class javaCheckTestCase(unittest.TestCase):
	print "Tests for `javaCheck.py`."

	def setUp(self):
		print "\tset up"	

	def testGetJavaVersion(self):
		print "\ttestGetJavaVersion"
		retDict = javaCheck.getJavaVersion()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		
	def tearDown(self):
		print "\ttear down"

	