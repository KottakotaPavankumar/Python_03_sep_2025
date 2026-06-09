"""
a = [2, 4, 8, 3]
res = 1

for val in a:
    res = res * val

print(res)
"""
"""
import math

a = [2, 4, 8, 3]
res = math.prod(a)

print(res)
"""
from functools import reduce
from operator import mul

a = [2, 4, 8, 3]
res = reduce(mul, a)

print(res)