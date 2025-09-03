dict1 = {
    "a" : 1,
    "c" : 3
}
dict2 = {
    "b" : 1,
    "d" : 4
}

# # o/p : keys from dict1 and dict2 



for i in dict1:
    for j in dict2:
        # print(dict1[i],dict2[j])
        if dict1[i] == dict2[j]:
            print(i,j)

for i,j in dict1.items():
    for m,n in dict2.items():
        if j == n:
            print(i,m)


