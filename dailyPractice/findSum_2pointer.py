#sorted array
# find target sum of two numbers using 2 pointer

def findNum(list1,num1):
    i , j = 0, len(list1)-1
    while i < j :
        sum = list1[i]+list1[j]
        if sum > num1:
            j -= 1
        elif sum < num1:
            i += 1
        elif sum == num1:
            return (i,j)



print(findNum([1,3,4,5,9,11,13], 15))