list1 = [10,5,7,5,10,7,8,3,8,6,1]


#Finding Duplicates
def dupUniq():
    unqList = []
    dupList = []
    # pass
    for i in list1:
        if i not in unqList:
            unqList.append(i)
        else:
            dupList.append(i)
    print(unqList)
    print(dupList)

dupUniq()