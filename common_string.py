#!/usr/bin/python

a,b=raw_input().split(' ')
c=''
for i in b:
    if i in a:
        if i not in c:
            c=c+i
print c
