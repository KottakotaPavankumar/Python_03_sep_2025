"""
P = 1200
R = 5.4
T = 2

A = P * (1 + R/100) ** T
CI = A - P

print("Compound interest:", CI)
"""

"""
p = 10000
r = 10.25
t = 5

Amt = p * (pow((1 + r / 100), t))
CI = Amt - p

print("Compound interest:", CI)
"""

"""
p = 1200
r = 5.4
t = 2          

Amt = p
for i in range(t):
    Amt = Amt * (1 + r / 100)

CI = Amt - p
print("Compound interest:", CI)
"""

p = int(input("Principal amount: "))
r = int(input("Rate of interest: "))
t = int(input("Time in years: "))


Amt = p * (pow((1 + r / 100), t))
CI = Amt - p

print("Compound interest:", CI)