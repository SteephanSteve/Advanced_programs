n=int(input())
a=map(int,raw_input().split(' '))
d={}
for i in a:
     d[i]=0
for i in a:
     c=d[i]+1
     d[i]=c
print max(d,key=d.get)


