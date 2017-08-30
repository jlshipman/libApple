#!/usr/bin/python
#run as non-root or admin
import sys
sys.path.append('lib')
import comWrap
import os
import shlex

def run (l, TEMP):
	l.info( "\tKeyboard")
	l.info( "\t\tsecureKeyboard")
	retDict = getSecureKeyboard ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
		
def getSecureKeyboard ():
	#defaults read -app Terminal SecureKeyboardEntry
	dict = {'function' : 'getSecureKeyboard'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['remed'] = "1. Open Terminal \n2. Select Terminal \n3. From the File menu, Select Secure Keyboard Entry"
	filter = ""
	appleCommand = ["defaults", "read", "-app", "Terminal", "-SecureKeyboardEntry"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	print "stdout:  " + stdout
	print "stderr:  " + stderr
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = int(stdout.strip())
	dict['result'] = result

	if result == 0:
		dict['comment'] = "Terminal keyboard is secure"	
		dict['retVal'] = 0
	else:
		dict['retVal'] = 1
		dict['comment'] = "Terminal keyboard is not secure /n" + dict['remed']
	return dict	
	
