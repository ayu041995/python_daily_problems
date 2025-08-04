dict1 = {
    "name" : "ayushi",
    "age" : "28",
    "roll_no" : "1001"
}

dict2 = {
    "name1" : "akash",
    "age1" : "30",
    "roll_no1" : "1002"
}


# How to add values to dictionary in Python
# veg_dict = {}
# veg_dict[0] = 'Carrot'
# veg_dict[1] = 'Raddish'

for i in dict2:
    # print(dict2[i])
    dict1[i] = dict2[i]

print(dict1)

