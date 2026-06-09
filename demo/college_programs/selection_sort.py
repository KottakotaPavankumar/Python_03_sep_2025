def selection_sort(list1):
    for i in range(len(list1)):
        min_index = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        temp = list1[i]
        list1[i] = list1[min_index]
        list1[min_index] = temp
    return list1

list1 = [51, 35, 87, 69, 73, 29]
print("The unsorted list is:", [51, 35, 87, 69, 73, 29])
print("The sorted list is:", selection_sort(list1))
