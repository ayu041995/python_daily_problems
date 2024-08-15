# Given an array of random integers, find the index of first non-repeating integer in the array.
# [4, 5, 1, 2, 0, 4] o/p -> 1
# [2, 5, 4, 5, 0, 2,1,2] o/p ->  2

#### Using List #########

# def nonreap(list1):
#     for i in range(len(list1)):
#         new_list = []
#         for j in range(0,len(list1)):
#             # print(i,j)
#             if i == j:
#                 continue
#             else:
#                 new_list.append(list1[j])
#         print(new_list)
#         if list1[i] in new_list:
#             continue
#         else:
#             return i
            
 

# print(nonreap([4, 5, 1, 2, 0, 4]))
# print(nonreap([2, 5, 4, 5, 0, 2,1,2]))


##### Using dictionary #########

def firstNonRepeatingInteger(list1):
    dict1 = {}
    for i in list1:
        # print(i)
        if i in dict1.keys():
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    print(dict1)
    # for i in dict1:
    #     if dict1[i] == 1:
    #         return i
    for i in range(len(list1)):
        if dict1[list1[i]] == 1:
            return i
    
        
print(firstNonRepeatingInteger([4, 5, 1, 2, 0, 4]))
print(firstNonRepeatingInteger([2, 5, 4, 5, 0, 2,1,2]))


