def insertion_sort(list1):
    for i in range(1, len(list1)):
        value = list1[i]
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value
    return list1

list1 = [11, 75, 33, 48, 92]
print("The unsorted list is:", [11, 75, 33, 48, 92])
print("The sorted list is:", insertion_sort(list1))