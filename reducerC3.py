#!/usr/bin/python
import fileinput
import sys
currentStreet=None
bestStreet=None
maxVal=0
trafficValue=0
totalTraffic=0
for line in sys.stdin:
	list = line.split(',')
	aux=0
	for i,x in enumerate(list):
		if(i is not 0):
			aux += int(list[i])
	list[1]=aux
	if(currentStreet==list[0]):
		trafficValue+=aux
	
	else:
		if(trafficValue > maxVal):
			maxVal= trafficValue
			bestStreet=currentStreet
		totalTraffic+=trafficValue
		currentStreet=list[0]
		trafficValue=aux
print "total traffic = " + str(totalTraffic)
print "Best street is: "+ bestStreet + " with total traffic of: "+ str(maxVal) 



