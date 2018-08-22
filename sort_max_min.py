#!/usr/bin/python

n=int(input())
a=map(int,raw_input().split(' '))
a.sort(reverse=True)
ma=a[0:len(a)/2]
mi=a[len(a)/2:len(a)]
mi=mi[::-1]
for i in range(len(a)):
    if i<len(ma):
        print ma[i],
    if i<len(mi):
        print mi[i],
        


