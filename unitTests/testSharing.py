#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import sharing

class sharingTestCase(unittest.TestCase):
	print "Tests for `sharing.py`."

	def setUp(self):
		print "\tset up"	
	
	def testgetRemoteAppleEvents(self):
		print "\ttestGetRemoteAppleEvents"
		retDict = sharing.getRemoteAppleEvents()
		stderr = retDict['stderr']
		stdout = retDict['stdout']
		result = retDict['result']
		retVal = retDict['retVal']
		print "\t\tstdout:  " + str(stdout)
		print "\t\tstderr:  " + stderr
		print "\t\tresult:  " + str(result)	
		print "\t\tretVal:  " + str(retVal)
		self.assertEqual(retVal, 0)
	
	def setRemoteAppleEventsOff(self):
		print "\ttestSetRemoteAppleEventsOff"
		retDict = sharing.setRemoteAppleEventsOff()
		stderr = retDict['stderr']
		stdout = retDict['stdout']
		result = retDict['result']
		retVal = retDict['retVal']
		print "\t\tstdout:  " + str(stdout)
		print "\t\tstderr:  " + stderr
		print "\t\tresult:  " + str(result)	
		print "\t\tretVal:  " + str(retVal)
		self.assertEqual(retVal, 0)

	def testGetInternetSharing(self):
		print "\ttestGetInternetSharing"
		retDict = sharing.getInternetSharing()
		stderr = retDict['stderr']
		stdout = retDict['stdout']
		result = retDict['result']
		retVal = retDict['retVal']
		print "\t\tstdout:  " + str(stdout)
		print "\t\tstderr:  " + stderr
		print "\t\tresult:  " + str(result)	
		print "\t\tretVal:  " + str(retVal)
		self.assertEqual(retVal, 0)

	def testSetInternetSharingOff(self):
		print "\ttestSetInternetSharingOff"
		retDict = sharing.setInternetSharingOff()
		stderr = retDict['stderr']
		stdout = retDict['stdout']
		result = retDict['result']
		retVal = retDict['retVal']
		print "\t\tstdout:  " + str(stdout)
		print "\t\tstderr:  " + stderr
		print "\t\tresult:  " + str(result)	
		print "\t\tretVal:  " + str(retVal)
		self.assertEqual(retVal, 0)

	def testGetPrinterSharing(self):
		print "\ttestGetPrinterSharing"
		retDict = sharing.getPrinterSharing()
		stderr = retDict['stderr']
		stdout = retDict['stdout']
		result = retDict['result']
		retVal = retDict['retVal']
		print "\t\tstdout:  " + str(stdout)
		print "\t\tstderr:  " + stderr
		print "\t\tresult:  " + str(result)	
		print "\t\tretVal:  " + str(retVal)
		self.assertEqual(retVal, 0)

	def testGetRemoteLogin(self):
		print "\ttestGetRemoteLogin"
		retDict = sharing.getRemoteLogin()
		stderr = retDict['stderr']
		stdout = retDict['stdout']
		result = retDict['result']
		retVal = retDict['retVal']
		print "\t\tstdout:  " + str(stdout)
		print "\t\tstderr:  " + stderr
		print "\t\tresult:  " + str(result)	
		print "\t\tretVal:  " + str(retVal)
		self.assertEqual(retVal, 1)
	
	def testGetDVDsharing(self):
		print "\ttestGetDVDsharing"
		retDict = sharing.getDVDsharing()
		stderr = retDict['stderr']
		stdout = retDict['stdout']
		result = retDict['result']
		retVal = retDict['retVal']
		print "\t\tstdout:  " + str(stdout)
		print "\t\tstderr:  " + stderr
		print "\t\tresult:  " + str(result)	
		print "\t\tretVal:  " + str(retVal)
		self.assertEqual(retVal, 0)	
				
	def tearDown(self):
		print "\ttear down"

	