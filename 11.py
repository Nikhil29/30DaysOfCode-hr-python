#!/usr/bin/env python
import sys

arr = []
max=-1000000
for i in range(6):
	row=map(int,raw_input().split(' '))
	arr.append(row)
for i in range(4):
	for j in range(4):
		temp=arr[i][j]+arr[i][j+1]+arr[i][j+2]
		temp+=arr[i+1][j+1]
		temp+=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
		if temp>max:
			max=temp
print max