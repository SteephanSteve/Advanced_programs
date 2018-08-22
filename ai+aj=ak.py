#!/usr/bin/python

n=int(input())
a=map(int,raw_input().split(' '))
c=0
for i in range(len(a)):
    for j in range(i,len(a)):
        for k in range(j,len(a)):
            if a[i]+a[j]==a[k] and i<j<k:
                c+=1
print c
