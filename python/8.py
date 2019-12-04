#!/usr/bin/env python
import sys

n=int(raw_input().strip())
a={}
for i in range(n):
	name=raw_input().strip()
	mobile=raw_input().strip()
	a[name]=mobile
while(1):
	try:
		query=raw_input().strip()
	except EOFError:
		break
	try:
		print "%s=%s" % (query,a[query])
	except KeyError:
		print "Not found"