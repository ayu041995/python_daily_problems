# Replace 2nd Occurrence in String with new string

str_given = "Gfg is best. Gfg also has Classes now. Classes help understand better Gfg"
str1 = "Gfg"
new_str = "bbb"

def replaceStr():
    list_new = str_given.split()
    count = 0
    # print(list_new)
    for i in range(len(list_new)):
        if list_new[i] == 'Gfg':
            count += 1
        # print(count)
        if count > 1 and list_new[i] == 'Gfg':
            list_new[i] = 'bbb'
    print(list_new)

print(replaceStr())