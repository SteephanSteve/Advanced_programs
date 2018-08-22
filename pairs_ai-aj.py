#!/usr/bin/python

n=int(input())
a=map(int,raw_input().split(' '))
c=0
for i in range(len(a)):
    for j in range(i,len(a)):
        if i<j and a[i]<a[j]:
            c+=1
print c
