#!/usr/bin/env python
import sys

def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

input=raw_input().split(' ')
print gcd(int(input[0]), int(input[1]))