#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import network

class newtorkTestCase(unittest.TestCase):
	print "Tests for `Network.py`."

	def setUp(self):
		print "#####################################################################################################\n"
		print "\tset up"	

	def testGetNetworkLocations(self):
		print "\ttestGetNetworkLocations"
		retDict = network.getNetworkLocations()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		stdout = retDict['stdout']
		stderr = retDict['stderr']
		found = retDict['found']
		remed = retDict['remed']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		
	def testGetWifiMenu(self):
		print "\ttestGetWifiMenu"
		retDict = network.getWifiMenu()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		stdout = retDict['stdout']
		stderr = retDict['stderr']
		found = retDict['found']
		remed = retDict['remed']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
		
	def testGetBonjour(self):
		print "\ttestGetBonjour"
		retDict = network.getBonjour()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		stdout = retDict['stdout']
		stderr = retDict['stderr']
		found = retDict['found']
		remed = retDict['remed']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"

	def testSetBonjour(self):
		print "\ttestSetBonjour"
		retDict = network.setBonjour()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		stdout = retDict['stdout']
		stderr = retDict['stderr']
		found = retDict['found']
		remed = retDict['remed']
		print "\t\tresult:  " 
		for i in result:
			print "\t\t\t" + i
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout:  _" + stdout + "_"
		print "\t\tstderr:  _" + stderr + "_"
		print "\t\tremed:   _" + remed + "_"
		print "\t\tfound:   _" + str(found) + "_"
				
	def tearDown(self):
		print "\ttear down"
		print "#####################################################################################################\n"

	