#!/usr/bin/env python
import sys

t=int(raw_input().strip())
for i in range(t):
	arr=list()
	n=int(raw_input())
	while n!=0:
		arr.append(n%2)
		n=n/2
	arr.reverse()
	for j in arr:
		sys.stdout.write('%d' % j)
	print ""