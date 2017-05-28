#!/usr/bin/python
import fileinput
import sys
def rehabParaStrings(str1):
	return ' '.join([x for x in str1.split(" ") if x])

for line in sys.stdin:
	list = line.split(',')

	if len(list) == 32: 
		try:
			nums = [str(int(x))  for x in list[7:31]]
			print rehabParaStrings(list[2]) +','+','.join(nums)+' '
		except ValueError:
			continue;

	


