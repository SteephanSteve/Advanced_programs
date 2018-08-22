#!/usr/bin/python

n=int(input())
a=[]
s=0
for i in range(m):
    x=map(int,raw_input().split(' '))
    a.append(x)
for i in range(m):
    s=s+a[i][i]
print s
