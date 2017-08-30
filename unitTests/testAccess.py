#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import access
import funcReturn

class accessTestCase(unittest.TestCase):
	print "Tests for `Access.py`."

	def setUp(self):
		print ""
		print "\tset up"	
		print ""

	def testFastSwitching(self):
 		print "\ttestFastSwitching"
 		retObj = access.fastSwitching()
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
 		
	def testSecureKeychain(self):
 		print "\ttestSecureKeychain"
 		retObj = access.secureKeychain()
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
 		
	def testSpecializedKeychains(self):
 		print "\ttestSpecializedKeychains"
 		retObj = access.specializedKeychains()
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
 		
	def testGetWarning(self):
		print "\ttestGetWarning"
		retObj = access.getWarning()
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

	def testSetWarning(self):
		print "\ttestSetWarning"
		warning="This US Government computer is for authorized users only. By accessing this system you are consenting to complete monitoring with no expectation of privacy. Unauthorized access or use may subject you to disciplinary action and criminal prosecution."
		retObj = access.setWarning(warning)
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
						
# 	def testSetLibraryDir(self):
# 		print "\ttestSetLibraryDir"
# 		retObjGet = access.getLibraryDir()
# 		result = retObjGet.getResult()
# 		
# 		retObj = access.setLibraryDir(result)
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"	
# 		
# 
# 	def testGetLibraryDir(self):
# 		print "\ttestGetLibraryDir"
# 		retObj = access.getLibraryDir()
# 		result = retObj.getResult()
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"	
# 
# 		
# 	def testSetSystemDir(self):
# 		print "\ttestSetSystemDir"
# 		retObjGet = access.getSystemDir()
# 		result = retObjGet.getResult()
# 		
# 		retObj = access.setSystemDir(result)
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"	
# 		
# 
# 	def testGetSystemDir(self):
# 		print "\ttestGetSystemDir"
# 		retObj = access.getSystemDir()
# 		result = retObj.getResult()
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"	
# 				
# 	def testSetSysWideApps(self):
# 		print "\ttestSetSysWideApps"
# 		retObjGet = access.getSysWideApps()
# 		result = retObjGet.getResult()
# 		
# 		retObj = access.setSysWideApps(result)
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"			
# 
# 	def testGetSysWideApps(self):
# 		print "\ttestGetSysWideApps"
# 		retObj = access.getSysWideApps()
# 		result = retObj.getResult()
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"	
# 		
# 	def testSetRepairPremissions(self):
# 		print "\ttestSetRepairPremissions"
# 		retObj = access.setRepairPremissions()
# 		result = retObj.getResult()
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"	
# 				
# 	def testGetRepairPremissions(self):
# 		print "\ttestGetRepairPremissions"
# 		retObj = access.getRepairPremissions()
# 		result = retObj.getResult()
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"	
# 			
# 	def testSetPermissHome(self):
# 		print "\ttestSetPermissHome"
# 		retObjGet = access.getPermissHome()
# 		theList = retObjGet.getResult()
# 		retObj = access.setPermissHome(theList )
# 		result = retObj.getResult()
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"
# 		
# 	def testGetPermissHome(self):
# 		print "\ttestGetPermissHome"
# 		retObj = access.getPermissHome()
# 		result = retObj.getResult()
# 		retVal = retObj.getRetVal()
# 		comment = retObj.getComment()
# 		stdout = retObj.getStdout()
# 		stderr = retObj.getStderr()
# 		found = retObj.getFound()
# 		remed = retObj.getRemed()
# 		print "\t\tresult:  _" + str(result)  + "_"
# 		print "\t\tretVal:  _" + str(retVal)  + "_"
# 		print "\t\tcomment: _" + comment + "_"
# 		print "\t\tstdout:  _" + stdout + "_"
# 		print "\t\tstderr:  _" + stderr + "_"
# 		print "\t\tremed:   _" + remed + "_"
# 		print "\t\tfound:   _" + str(found) + "_"
# 
# 				
	def tearDown(self):
		print ""
		print "\ttear down"
		print ""
	