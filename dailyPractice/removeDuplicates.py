# list1 = [2,5,8,9,2,5,7,8]

# def removeDuplicates(list1):
#     # pass
#     new_list = []
#     for i in list1:
#         if i in new_list:
#             continue
#         else:
#             new_list.append(i)
#     return new_list


# print(removeDuplicates([2,5,8,9,2,5,7,8]))


#aakashks -> aksh

def removeDuplicate(str1):
    # pass
    new_str = ''
    for i in str1:
        if i in new_str:
            continue
        else:
             new_str = new_str + i
    return new_str

print(removeDuplicate('aakashks'))

