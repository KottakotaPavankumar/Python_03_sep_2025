def recursive_insertion_sort(arr, n):
    # Base case
    if n <= 1:
        return
    # Sort first n-1 elements
    recursive_insertion_sort(arr, n-1)
    last = arr[n-1]
    j = n-2
    # Move elements greater than last up one position
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last

# Get user input
size = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the elements:")
for i in range(size):
    num = int(input())
    arr.append(num)

print("Original array:", arr)
recursive_insertion_sort(arr, len(arr))
print("Sorted array:", arr)
