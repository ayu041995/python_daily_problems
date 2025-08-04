# Move all the zeros to the end

list1 = [0,6,9,0,2,7,0,0,8,0,2,5,0]

def moveZero():
    list_new = []
    total = 0
    for i in list1:
        if i == 0:
            total += 1
        else:
            list_new.append(i)
    for i in range(total):
        list_new.append(0)
    
    return list_new

print(moveZero())




