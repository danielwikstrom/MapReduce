#!/usr/bin/python
import fileinput
import sys
currentStreet=None
trafficValue=0
for line in sys.stdin:
	list = line.split(',')
	if(currentStreet==list[0]):
		trafficValue+=int(list[1])
	else:
		if(currentStreet):
	 		print currentStreet + ',' + str(trafficValue)
		currentStreet=list[0]
		trafficValue=int(list[1])
print currentStreet + ',' + str(trafficValue)
	




