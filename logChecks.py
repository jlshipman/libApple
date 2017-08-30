#!/usr/bin/python
import sys
sys.path.append('lib')
import comWrap
import os
import shlex
import re
import fileFunctions
import funcReturn


#Chapter 3 Logging and Auditing 10.9 CIS Benchmark  
def run (l, TEMP):
	l.info( "\tLogging")
	
	l.info( "\t\tGet Audit Flags")
	retDict = getAuditFlags ()	
	retVal=retDict['retVal']
	remed=retDict['remed']
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremeditiion: " + remed )
	
	l.info( "\t\tRetain install.log for 365")
	retObj = getInstallLogRetain()
	retVal = retObj.getRetVal()
	remed = retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremedy: " + remed )
	
	l.info( "\t\tSystem Log Retaintion")
	retObj = getSystemLogRetain ()	
	retVal = retObj.getRetVal()
	remed = retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremedy: " + remed )

	l.info( "\t\tFirewall Log Retaintion")
	retObj = getFirewallLogRetain ()	
	retVal = retObj.getRetVal()
	remed = retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremedy: " + remed )

	l.info( "\t\tAuthd Log Retaintion")
	retObj = getAuthdLogRetain ()	
	retVal = retObj.getRetVal()
	remed = retObj.getRemed()
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tremedy: " + remed )
	
	l.info( "\t\tSet security auditing")
	retDict = setSecurityAudit ()	
	retVal=retDict['retVal']
	comment=retDict['comment']
	l.info( "\t\t\tretVal: " + str(retVal))
	l.info( "\t\t\tcomment: " + comment )

#flags:lo,aa,ad,fm,fd,-all

def setSecurityAudit():
	#sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.auditd.plist
	dict = {'function' : 'setSecurityAudit' }
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['remed']="""1. Run the following command in Terminal:
			sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.auditd.plist"""
	appleCommand = ["sudo", "launchctl", "load", "-w", "/System/Library/LaunchDaemons/com.apple.auditd.plist"]
	retDict = getSecurityAudit()
	if retDict['retVal'] == 1:
		retDict = comWrap.comWrap2(appleCommand)
		stdout = retDict['stdout'].strip()
		stderr = retDict['stderr'].strip() 
		dict['stdout'] = stdout
		dict['stderr'] = stderr
		result = stdout.strip()
		match = re.search(r'(.*)\bcom.apple.auditd\b$', result)
		if match:
			dict['found'] = 0
			dict['retVal'] = 0
			dict['comment'] = "Security auditing is enabled"
		else:
			dict['comment'] = "Security auditing is not enabled\n\t\t\t" + dict['remed']
		dict['result'] = result
	else:
		dict['found'] = 0
		dict['retVal'] = 0
		dict['comment'] = "Security auditing is enabled"
	return dict


def getSecurityAudit():
	#sudo launchctl list | grep -i auditd
	dict = {'function' : 'getSecurityAudit' }
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['remed']= ""
	appleCommand = ["sudo", "launchctl", "list"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr
	result = stdout.strip()
	
	for line in result.splitlines():
		dict['line']= line.strip()
		match = re.search(r'(.*)\bcom.apple.auditd\b$', dict['line'])
		if match:
			dict['found'] = 0
			dict['retVal'] = 0
			dict['comment'] = "Security auditing is enabled"
			
	if dict['found'] == 0:
		dict['comment'] = "Security auditing is enabled"
	else:
		dict['comment'] = "Security auditing is not enabled\n\t\t\t" + dict['remed']

	return dict


def getInstallLogRetain():
	#grep -i ttl /etc/asl/com.apple.install
	retObj = funcReturn.funcReturn('getInstallLogRetain')
	string="file /var/log/install.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=365"
	filePath="/etc/asl/com.apple.install"
	retObjFind = fileFunctions.findString(string, filePath)
	if retObjFind.getRetVal() == 0:
		comment = "Install Logs retention is set appropiately"
		retObj.setComment(comment)
		retObj.setRetVal(0)
	else:
		comment = "Install Logs retention is not set appropiately"
		retObj.setComment(comment)
		remedy="""\n\t\t\t\t\t\t\t\t1. Run the following command in Terminal:
\t\t\t\t\t\t\t\tsudo vim /etc/asl/com.apple.install
\t\t\t\t\t\t\t\t2. Replace or edit the current setting with a compliant setting
\t\t\t\t\t\t\t\t* file /var/log/install.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=365"""
		retObj.setRemed(remedy)
	return retObj

	
def getAuthdLogRetain():
	#grep -i ttl /etc/asl/com.apple.authd
	#file /var/log/authd.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90
	retObj = funcReturn.funcReturn('getAuthdLogRetain')
	string="file /var/log/authd.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90"
	filePath="/etc/asl/com.apple.authd"
	retObjFind = fileFunctions.findString(string, filePath)
	if retObjFind.getRetVal() == 0:
		comment = "Install authd Logs retention is set appropiately"
		retObj.setComment(comment)
		retObj.setRetVal(0)
	else:
		comment = "Install authd Logs retention is not set appropiately"
		retObj.setComment(comment)
		remedy="""\n\t\t\t\t\t\t\t\t1. Run the following command in Terminal:
\t\t\t\t\t\t\t\tsudo vim /etc/asl/com.apple.authd
\t\t\t\t\t\t\t2. Replace or edit the current setting with a compliant setting
\t\t\t\t\t\t\t\t file /var/log/authd.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90"""
		retObj.setRemed(remedy)
	return retObj	
		
def getFirewallLogRetain():
	#grep -i 'firewall.*ttl' /etc/asl.conf
	#> appfirewall.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90
	retObj = funcReturn.funcReturn('getFirewallLogRetain')	
	string="> appfirewall.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90"
	filePath="/etc/asl.conf"
	retObjFind = fileFunctions.findString(string, filePath)
	if retObjFind.getRetVal() == 0:
		comment = "Install authd Logs retention is set appropiately"
		retObj.setComment(comment)
		retObj.setRetVal(0)
	else:
		comment = "Install authd Logs retention is not set appropiately"
		retObj.setComment(comment)
		remedy="""\n\t\t\t\t\t\t\t\t1. Run the following command in Terminal:
			\t\t\tsudo vim /etc/asl.conf
			\t\t\t2. Replace or edit the current setting with a compliant setting
			\t\t\t> appfirewall.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90"""
		retObj.setRemed(remedy)
	return retObj	
	
def getSystemLogRetain():
	#grep -i 'system.*ttl' /etc/asl.conf
	#> system.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90
	retObj = funcReturn.funcReturn('getSystemLogRetain')
	string="> system.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90"
	filePath="/etc/asl.conf"
	retObjFind = fileFunctions.findString(string, filePath)
	if retObjFind.getRetVal() == 0:
		comment = "Install System Logs retention is set appropiately"
		retObj.setComment(comment)
		retObj.setRetVal(0)
	else:
		comment = "Install System Logs retention is not set appropiately"
		retObj.setComment(comment)
		remedy="""\n\t\t\t\t\t\t\t\t1. Run the following command in Terminal:
			\t\t\tsudo vim /etc/asl.conf
			\t\t\t2. Replace or edit the current setting with a compliant setting
			\t\t\t> system.log mode=0640 format=bsd rotate=utc compress file_max=5M ttl=90"""
		retObj.setRemed(remedy)
	return retObj	
	
def getAuditFlags():
	#sudo egrep "^flags:" /etc/security/audit_control
	dict = {'function' : 'getAuditFlags'}	
	dict['error'] = ""
	dict['comment'] = ""
	dict['stdout'] = ""
	dict['stderr'] = ""
	dict['result'] = ""
	dict['retVal'] = 1
	dict['found'] = 1
	dict['needFlag'] = ""
	dict['remed']=""
	appleCommand = ["sudo", "egrep", "flags:", "/etc/security/audit_control"]
	retDict = comWrap.comWrap2(appleCommand)
	stdout = retDict['stdout'].strip()
	stderr = retDict['stderr'].strip() 
	dict['stdout'] = stdout
	dict['stderr'] = stderr.strip()
	result = stdout.strip()
	lines=result.splitlines()
	for l in lines:
		match = re.search(r'^\bflags:\b(.*)', l)
		if match:
			dict['found'] = 0
			result = match.group(1)		
			searchList={'lo', 'ad', 'fd', 'fm', '-all'}
			for s in searchList:
				f=result.find(s)
				if f ==  -1:
					dict['needFlag'] = s.strip() + "," + dict['needFlag'].strip() 
			break
	dict['needFlag'] = dict['needFlag'].strip(",") 
	if dict['needFlag'] != "":
		first = """1. Open a terminal session and edit the /etc/security/audit_control file
\t\t\t\t\t\t\t2. Find the line beginning with "flags"
\t\t\t\t\t\t\t3. Add the following flags: """ 
		second = """
\t\t\t\t\t\t\t4. Save the file."""
		dict['remed']= first + dict['needFlag'] + second
	else:
		dict['retVal'] = 0
	dict['result'] = result
	return dict	
	
