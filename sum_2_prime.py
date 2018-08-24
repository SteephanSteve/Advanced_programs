#!/usr/bin/python

n=int(input())
c=0
p,a=[],[]
for i in range(2,n):
    if i>1:
       for j in range(2,i):
           if i%j==0:
              break
       else:
           p.append(i)
for i in range(len(p)):
    for j in range(len(p)):
        if p[i]+p[j]==n:
            if p[j] not in a:
                a.append(p[i])
                c+=1
print c

    

