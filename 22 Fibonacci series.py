# Write a Python Program to Display Fibonacci Sequence Using Recursion.

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter the number of terms (> 0): "))

if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))

# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

def fibonacci(n):
    sequence = [0, 1] # Initializing the sequence with the first two F
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
    return sequence
try:
    n = int(input("Enter a value for n: "))
    result = fibonacci(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
