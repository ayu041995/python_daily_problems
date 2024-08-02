str1 = 'abfhgytbbvactj'

def minMaxOccurance():
    dict1 = {}
    max_count = 0

    for i in str1:
        # print(i)
        if i in dict1.keys():
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
            # dict1.update({ i : 1})
    print(dict1)
    for i in dict1:
        # print(dict1[i])
        if dict1[i] > max_count:
            max_count = dict1[i]
    print("MAX count is", max_count)


print(minMaxOccurance())