list1 = [3,2,1,5,4]
k = 2

# o/p 3-1 =2,  2-4 = -2, 3-5 = -2 -- o/p is 3


def absDifference():
    i = 0
    j = len(list1)
    count = 0

    while i < j:
        if abs(list1[i] - list1[j]) == k:
            count += 1
        i += 1
        j -= 1
    return count

print(absDifference())