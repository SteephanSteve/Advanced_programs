
#!/usr/bin/python

n=int(input())
a=map(int,raw_input().split(' '))
p,s=[],[]
for i in range(1,len(a)-1):
    p.append(a.pop(0))
    s=a[1::]
    if sum(p)==sum(s):
        print "yes"
        break
else:
    print "no"
