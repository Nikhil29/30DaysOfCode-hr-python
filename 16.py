#!/usr/bin/env python
import sys

#take input
n = int(raw_input().strip())
input_array = map(int,raw_input().split(' '))

input_array.sort()

ans=[]
minDifference=1000000000
for i in range(0,n-1):
	if(input_array[i+1]-input_array[i]<minDifference):
		minDifference = input_array[i+1]-input_array[i]
		ans = []
		temp = [input_array[i], input_array[i+1]]
		ans.append(temp)
	elif(input_array[i+1]-input_array[i]==minDifference):
		temp = [input_array[i], input_array[i+1]]
		ans.append(temp)

#print
for pair in ans:
	for i in pair:
		sys.stdout.write(str(i)+" ") 