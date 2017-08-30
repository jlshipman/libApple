#!/usr/bin/python
import unittest, inspect, os, sys
curDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curDir)
dirName = os.path.dirname(curDir)
sys.path.append(dirName)
dirName2 = os.path.dirname(dirName)
libPath = dirName2 + "/lib"
sys.path.append(libPath)
import logChecks

class loggingTestCase(unittest.TestCase):
	print "Tests for `logging.py`."

	def setUp(self):
		print "#####################################################################################################\n"
		print "\tset up"	

	def testSetSecurityAudit(self):
		print "\ttestSetSecurityAudit"
		retDict = logChecks.setSecurityAudit()
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
		
	def testGetSecurityAudit(self):
		print "\ttestGetSecurityAudit"
		retDict = logChecks.getSecurityAudit()
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
		
	def testGetInstallLogRetain(self):
		print "\ttestGetInstallLogRetain"
		retObj = logChecks.getInstallLogRetain()
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
		
	def testGetAuthdLogRetain(self):
		print "\ttestGetAuthdLogRetain"
		retObj = logChecks.getAuthdLogRetain()
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
				
	def testGetFirewallLogRetain(self):
		print "\ttestGetFirewallLogRetain"
		retObj = logChecks.getFirewallLogRetain()
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
	
	def testGetSystemLogRetain(self):
		print "\ttestGetSystemLogRetain"
		retObj = logChecks.getSystemLogRetain()
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
	
	def testGetAuditFlags(self):
		print "\ttestGetAuditFlags"
		retDict = logChecks.getAuditFlags()
		result = retDict['result']
		retVal = retDict['retVal']
		comment = retDict['comment']
		stdout = retDict['stdout']
		stderr = retDict['stderr']
		found = retDict['found']
		remed = retDict['remed']
		needFlag = retDict['needFlag']
		print "\t\tresult:  _" + result  + "_"
		print "\t\tretVal:  _" + str(retVal)  + "_"
		print "\t\tcomment: _" + comment + "_"
		print "\t\tstdout: _" + stdout + "_"
		print "\t\tstderr: _" + stderr + "_"
		print "\t\tfound: _" + str(found) + "_"
		print "\t\tneedFlag: _" + needFlag + "_"
		print "\t\tremed: _" + remed + "_"
		
	def tearDown(self):
		print "\ttear down"
		print "#####################################################################################################\n"

	