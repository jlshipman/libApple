#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os

def run (l, TEMP):
	l.info( "\tKeyboard")
	l.info( "\t\tsecureKeyboard")
	retDict = getSecureKeyboard ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal) )
	l.info( "\t\t\tcomment: " + comment )
		
def getJavaVersion ():
	#java -version
	#java -version produces pop up that crashes script
	dict = {'function' : 'getJavaVersion'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	filter = ""
	appleCommand = ["java", "-v"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	print "stdout:  " + stdout
	print "stderr:  " + stderr
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = int(stdout.strip())
	dict['result'] = result
	return dict	
	
