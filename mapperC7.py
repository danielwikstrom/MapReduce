#!/usr/bin/python
import fileinput
import sys
def rehabParaStrings(str1):
	return ' '.join([x for x in str1.split(" ") if x])

for line in sys.stdin:
	list = line.split(',')

	if len(list) == 32: 
		try:
			if((rehabParaStrings(list[3])=="BROADWAY") or (rehabParaStrings(list[4])=="BROADWAY")):
				nums = [str(int(x))  for x in list[7:31]]
				print rehabParaStrings(list[3]) +','+rehabParaStrings(list[4]) +','+','.join(nums)+' '
		except ValueError:
			continue;

	


