#!/usr/bin/python

s,x=raw_input().split(' ')
c=''
for i in x:
    if i in s:
        c=c+i
print c
