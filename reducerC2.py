#!/usr/bin/python
import fileinput
import sys
numeroTuplas=0
listita= [0 for x in xrange(0,24,1)]

for line in sys.stdin:
	list = line.split(',')
	numeroTuplas+=1
	listita=[x+int(y) for x,y in zip(listita, list)]
print ", ".join([str(x/float(numeroTuplas)) for x in listita])
print len([str(x/float(numeroTuplas)) for x in listita]) 



