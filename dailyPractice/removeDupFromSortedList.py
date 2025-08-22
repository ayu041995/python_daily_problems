# Remove duplicates from sorted List

list1 = [1,5,6,7,7,8,8,8,8,9,10,11,100,101,101]

# def removeDup():
#     i = 0
#     while i < (len(list1)-1):
#         if list1[i] == list1[i+1]:
#             list1.pop(i+1)
#         i += 1
#     return list1


# print(removeDup())


# def removeDup():
#     uniq_list = []
#     for i in list1:
#         if i not in uniq_list:
#             uniq_list.append(i)
#     return uniq_list
# print(removeDup())

def removeDup():
    left = 0
    right = left + 1
    while right < len(list1):
        if list1[left] == list1[right]:
            list1.pop(left)
            left -= 1
            right-= 1
        left += 1
        right += 1
    return list1

print(removeDup())



