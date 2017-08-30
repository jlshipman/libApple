#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import energy

class energyTestCase(unittest.TestCase):
	print "Tests for `energy.py`."

	def setUp(self):
		print "\tset up"	

	def testSleep(self):
		print "\ttestSleep"
		retDict = energy.getSleep()
		result = retDict['result']
		line = retDict['line']
		text = retDict['text']
		retVal = retDict['retVal']
		comment = retDict['comment']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tline:  _" + line  + "_"
		print "\t\ttext:  _" + text  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
			
	def testWake(self):
		print "\ttestWake"
		retDict = energy.getWake()
		result = retDict['result']
		line = retDict['line']
		text = retDict['text']
		retVal = retDict['retVal']
		comment = retDict['comment']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tline:  _" + line  + "_"
		print "\t\ttext:  _" + text  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		
	def tearDown(self):
		print "\ttear down"

	