# write program to find Even number or odd number form list

number = [1,2,3,4,5,6,7,8,9,10]

even, odd = [], []
for num in number:
    if num % 2 == 0:
        temp = num
        even.append(temp)
    else:
        temp = num
        odd.append(temp)

# <---------------Using List Comprehension
# even =[num for num in number if num % 2 ==0]
# odd = [num for num in number if num % 2 !=0]

print(f' Even : {even}\n Odd : {odd}')