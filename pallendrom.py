str1 = 'abcdcba'

def pell():
    str2 = ''
    for i in range(len(str1)-1,-1,-1):
        # print(i)
        str2 = str2 + str1[i]
        # print(str2)
    if str1 == str2:
        return 'given str is pellendrom'
    else:
        return 'given str is not pellendrom'

print(pell())
