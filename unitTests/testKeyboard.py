#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import keyboard

class keyboardTestCase(unittest.TestCase):
	print "Tests for `keyboard.py`."

	def setUp(self):
		print "\tset up"	

	def testGetSecureKeyboard(self):
		print "\ttestGetSecureKeyboard"
		retDict = keyboard.getSecureKeyboard()
		result = retDict['result']
		retVal = retDict['retVal']
		remed = retDict['remed']
		comment = retDict['comment']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tremed: _" + remed + "_"
		
	def tearDown(self):
		print "\ttear down"

	