#!/usr/bin/python

s,x=raw_input().split(' ')
c=''
for i in x:
    if i in s:
        if i not in c:
            c=c+i
print c
