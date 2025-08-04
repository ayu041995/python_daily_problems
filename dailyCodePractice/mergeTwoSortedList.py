# Merge two sorted lists

list1 = [1,7,10,11]
list2 = [2,5,8,15,17]


def mergeSortedList():
    list_sort = list1 + list2
    # print(list_sort)
    for i in range(len(list_sort)):
        for j in range(i+1, len(list_sort)):
            # print(i,j)
            if list_sort[i] > list_sort[j]:
                list_sort[i],list_sort[j] = list_sort[j],list_sort[i]
    return list_sort

print(mergeSortedList())


