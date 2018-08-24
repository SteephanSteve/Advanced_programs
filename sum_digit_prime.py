#!/usr/bin/python

l,r=map(int,raw_input().split(' '))
c=0
for i in range(l,r):
    i=list(map(int,str(i)))
    i=sum(i)
    if i>1:
       for n in range(2,i):
           if i%n==0:
              break
       else:
           c+=1
print c

    

