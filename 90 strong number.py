# Write the logic for strong number strong number in python -  145-->1!+4!+5!

n=145
total=0
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
for i in str(n):
    x=fact(int(i))
    total+=x
 
if n==total:
    print("It is strong number")
else:
    print("it is not a strong number")
