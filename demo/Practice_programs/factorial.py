"""
n = 6

# Initialize the factorial variable to 1
fact = 1

# Calculate the factorial using a for loop
for i in range(1, n + 1):
    fact *= i

print(fact)
"""

"""
import math

def factorial(n):
    return(math.factorial(n))

# Driver Code
num = 5
print(factorial(num))
"""

"""
import numpy
n=5
x=numpy.prod([i for i in range(1,n+1)])
print(x)
"""

"""
def fact(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)
"""

"""
# Driver Code
num = 5
print(fact(num))
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        # Calculate factorial by multiplying n with factorial(n-1)
        return n * factorial(n-1)

num = int(input("Enter a number:"))
print("The factorial of", num, "is", factorial(num))
