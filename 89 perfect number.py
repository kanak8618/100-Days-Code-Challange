# write logic to know whethe given number is perfect number or not

from functools import reduce
n=28
l1=[]
for i in range(1,n):
    if n%i==0:
        l1.append(i)
 
result=reduce(lambda x,y:x+y,l1) 
if n==result:
    print("perfect number")
else:
    print("Not perfect number")
