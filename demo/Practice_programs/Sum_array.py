"""
# Python 3 code to find sum
# of elements in given array


def _sum(arr):
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0

    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for x in arr:
        sum = sum + x

    return (sum)


# main function
if __name__ == "__main__":
    # input values to list
    arr = [12, 3, 4, 15]

    # calling function ans store the sum in ans
    ans = _sum(arr)

    # display sum
    print('Sum of the array is ', ans)
"""

"""
# Python 3 code to find sum
# of elements in given array

# input values to list
arr = [12, 3, 4, 15]

# sum() is an inbuilt function in python that adds
# all the elements in list,set and tuples and returns
# the value
ans = sum(arr)

# display sum
print('Sum of the array is ', ans)
"""

"""
from functools import reduce
# Python 3 code to find sum
# of elements in given array


def _sum(arr):

    # iterate over array
    # using reduce and get
    # sum on accumulator
    sum = reduce(lambda a, b: a+b, arr)

    return(sum)


# driver function
arr = []
# input values to list
arr = [12, 3, 4, 15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print('Sum of the array is ', ans)
"""

"""
list1 = [12, 3, 4, 15];s=0
for i,a in enumerate(list1):
  s+=a
print(s)
"""

from collections import Counter

arr = [12, 3, 4, 15]
c = Counter(arr)
sum = 0

for key, value in c.items():
    sum += key * value

print("Sum of the array is", sum)