#!/usr/bin/python
import fileinput
import sys
trafficGiven=0
trafficReceived=0
for line in sys.stdin:
	list = line.split(',')
	aux=0
	for i,x in enumerate(list):
		if(i is not 0 and i is not 1):
			aux += int(list[i])
	list[2]=aux
	if(list[0]=="BROADWAY"):
		trafficReceived+=aux
	else:
		trafficGiven+=aux
print "total traffic given is: " + str(trafficGiven)
print "total traffic received is: " + str(trafficReceived)



