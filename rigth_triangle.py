#!/usr/bin/python

n=int(input())
for i in range(n):
    l=n-i
    while l:
        print '1',
        l-=1
    print ''
