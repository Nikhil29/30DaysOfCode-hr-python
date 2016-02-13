#!/usr/bin/env python
import sys

n=int(raw_input().strip())
arr = map(int, raw_input().split(' '))

for i in range(n,0,-1):
	print "%d" % arr[i-1],