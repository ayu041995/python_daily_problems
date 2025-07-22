

def findMissingNum(list1,x):

    for i in range(1,x+1):
        # print(i)
        if i not in list1:
            print(i)


print(findMissingNum([9,1,2,4,5,6,8,7,99,98,97,96],100))