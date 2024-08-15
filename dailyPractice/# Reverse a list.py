# Reverse a list

list1 = [7,10,20,11,4]
# print(list1)


#Method 1
# list2 = list1 [::-1]
# print(list2)

#Method 2
def reverse_My_List():
    list2 = []
    for i in range(len(list1)-1,-1,-1):
        # print(list1[i])
        list2.append(list1[i])
    return print(list2)


#Calling my function
reverse_My_List()