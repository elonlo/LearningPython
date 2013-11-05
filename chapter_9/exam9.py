#!/usr/bin/env python

import os

pyDir = "/usr/lib/python2.7/"

oldDir = os.getcwd()
os.chdir(pyDir)
newDir = os.getcwd()
oldList = os.listdir(newDir)
newList = []
for fileName in oldList:
	if os.path.isdir(fileName):
		continue
	npos = 0
	npos = fileName.find(".py") #string find 
	if npos:
		newList.append(fileName[0:npos])

for name in newList:
	attri = dir(name)
	if "__doc__" in attri: #list find
		print name,
