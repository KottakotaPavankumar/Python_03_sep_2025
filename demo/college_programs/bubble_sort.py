def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1

list1 = [54, 13, 28, 76, 97, 12]
print("The unsorted list is: ", [54, 13, 28, 76, 97, 12])
print("The sorted list is: ", bubble_sort(list1))
