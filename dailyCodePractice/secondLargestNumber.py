# list1 = ['10','5','3','7']

def secondLargest(list1):
    l1 = list1[0]
    l2 = 0
    for i in list1:
        if i > l1:
            l2 = l1
            l1 = i
        # elif i < l1 and i > l2:
        #     l2 = i
        # print(l1,l2)
    return l2
    

print(secondLargest([10,6,7,13,100,101,9]))