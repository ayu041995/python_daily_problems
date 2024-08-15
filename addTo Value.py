# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# Input: [3, 5, 2, 8, 11], target = 10 Output: [2, 3] 2+8 --> 10

def addToValue(list1,target):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i] + list1[j] == target:
                return [i,j]

print(addToValue([3, 5, 2, 8, 11],10))


# ### Make it using dict

# int1 = 2

# print(int1)

# int1 + 2




# print(int1)

# list1 = [1,2]

# print(id(list1))

# list1.append(4)

# print(id(list1))

