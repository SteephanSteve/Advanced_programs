#!/usr/bin/python

p,q=raw_input().split(' ')
if len(p)>len(q):
    d=len(p)-len(q)
    for i in range(1,d+1):
        q+=str(i)
else:
   d=len(q)-len(p)
   for i in range(1,d+1):
        p+=str(i)
n=''
for i in range(len(p)):
    n+=p[i]+q[i]
print n

    

