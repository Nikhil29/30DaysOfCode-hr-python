#!/usr/bin/env python
t=int(raw_input())
for i in range(0,t):
	input=raw_input()
	input=input.split(" ")
	a=int(input[0])
	b=int(input[1])
	n=int(input[2])
	ans=a
	for j in range(0,n):
		ans+=b*pow(2,j)
		print "%d " % ans,
	print ""
