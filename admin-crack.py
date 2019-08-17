#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#NAME SEFYAN BN TALB 
#FROM :MOROCO
# NUBRE : +212 632804965
#m yfb: ? 
from urllib2 import Request, urlopen, URLError, HTTPError
import os
os.system('clear')
print "\n\n"

print "      \033[38;5;21m   .d8b. \033[38;5;13m d8888b.\033[38;5;202m .88b  d88. d888888b d8b   db"
print "      \033[38;5;21m  d8' `8b\033[38;5;13m 88  `8D\033[38;5;202m 88'YbdP`88   `88'   888o  88"
print "      \033[38;5;21m  88ooo88\033[38;5;13m 88   88\033[38;5;202m 88  88  88    88    88V8o 88"
print "      \033[38;5;21m  88~~~88\033[38;5;13m 88   88\033[38;5;202m 88  88  88    88    88 V8o88"
print "      \033[38;5;21m  88   88\033[38;5;13m 88  .8D\033[38;5;202m 88  88  88   .88.   88  V888"
print "      \033[38;5;21m  YP   YP\033[38;5;13m Y8888D'\033[38;5;202m YP  YP  YP Y888888P VP   V8P   finder"
print "\n\n"
print "║████████████████████████ Auteur : sefyan bntalb  ███████████████████████ "
def findAdmin():
	fi = open("wordlist.txt","r");
	link = raw_input("\n \033[1;30mEnter domin (ex:google.com ) :>> : ")
	print "\n  \033[01mAvilable links\033[0m : \n"
	while True:
		lo_link = fi.readline()
		if not lo_link:
			break
		tol_link = "http://"+link+"/"+lo_link
		tol = Request(tol_link)
		try:
			response = urlopen(tol)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "\033[92 admin found : \033[0m ",tol_link
findAdmin()
