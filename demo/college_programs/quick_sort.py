def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

# Driver code
arr = [62, 37, 18, 79, 81, 56]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Unsorted array :", [62, 37, 18, 79, 81, 56] )
print("Sorted array   :", arr)
