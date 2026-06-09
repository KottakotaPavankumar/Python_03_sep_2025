def binary_search(list1, n):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = (high + low) // 2

        if list1[mid] < n:
            low = mid + 1
        elif list1[mid] > n:
              high = mid - 1
        else:
            return mid  # Element found
    return -1  # Element not found

# Test the function
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 54
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in list1")
