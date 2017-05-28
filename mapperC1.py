#!/usr/bin/python
import fileinput
import sys
def rehabParaStrings(str1):
	return ' '.join([x for x in str1.split(" ") if x])

for line in sys.stdin:
	list = line.split(',')

	if len(list) == 32: 
		try:
			nums = [int(x)  for x in list[7:31]]
			print rehabParaStrings(list[2])+','+ str(sum(nums)) + ' '
		except ValueError:
			continue;

	


