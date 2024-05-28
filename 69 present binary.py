# Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

def binary(decimal):
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal = decimal // 2
    return binary_str if binary_str else "0"
    
print(binary(1))
print(binary(5)) 
print(binary(10)) 
