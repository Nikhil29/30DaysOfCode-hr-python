#!/usr/bin/env python
import sys

n=int(raw_input().strip())
for i in range(n):
	for j in range(n-i):
		print "",
	for j in range(i+1):
		sys.stdout.write('#')
	print ""
