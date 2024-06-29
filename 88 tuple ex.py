# Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

# Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

# Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
a,b,c,d=tuple1
print( a,"\n",b,"\n",c,"\n",d)

# Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2=tuple2,tuple1
print("tuple1",tuple1)
print("tuple2",tuple2)

# Copy specific elements from one tuple to a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:5]
print(tuple2)

#Modify the tuple
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


# Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple1=sorted(list(tuple1),key=lambda x:x[1])
tuple(tuple1)

#Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
tuple1.count(50)

t = (45, 45, 45, 45)
all_same=all(i==t[0] for i in t)
if all_same:
    print("yes all the item are same in the given tuple")
else:
    print("No all the item are not same in the given table")
