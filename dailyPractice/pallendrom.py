# str1 = 'abcdcba'

# def pell():
#     str2 = ''
#     for i in range(len(str1)-1,-1,-1):
#         # print(i)
#         str2 = str2 + str1[i]
#         # print(str2)
#     if str1 == str2:
#         return 'given str is pellendrom'
#     else:
#         return 'given str is not pellendrom'

# print(pell())


# 2 pointer approach

def pell(str1):
    a,b = 0,len(str1)-1

    while a < b:
        if str1[a] == str1[b]:
            a += 1
            b -= 1
        else:
            return ("not pallendrom")

    return ("pallendrom")

print(pell('abcdefedcba'))

