#!/usr/bin/env python
import sys,re

input = raw_input().strip()
input = re.split("[ !\[,?.\\\_'@+\]]", input)
input = filter(None, input)
print len(input)
print "\n".join(input)
