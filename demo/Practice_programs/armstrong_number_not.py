"""
n = 153
s = n
b = len(str(n))
sum1 = 0

while n != 0:
    r = n % 10
    sum1 = sum1 + (r ** b)
    n = n // 10

if s == sum1:
    print(s, "is an Armstrong number")
else:
    print(s, "is not an Armstrong number")
"""

"""
num = 153
num2 = str(num)
n = len(num2)
sum1 = 0

for digit in num2:
    sum1 += int(digit) ** n

if sum1 == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
"""

"""
num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
"""

num = int(input("Enter a number: "))
power = len(str(num))

def armstrong_sum(n):
    if n == 0:
        return 0
    return (n % 10) ** power + armstrong_sum(n // 10)

if armstrong_sum(num) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")