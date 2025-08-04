
#TYPE 1
# "5. Valid Parentheses
# Example 1: Input: s = ""()"" Output: true
# Example 2:Input: s = ""([{}])"" Output: true
# Example 3: Input: s = ""(]"" Output: false"

def validPar(s):
    refD = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    i = 0
    j = len(s)-1

    while i <= j:
        if s[i] in refD:
            # print(refD[s[i]],s[j])
            if refD[s[i]] != s[j]:
                return 'false'
        i += 1
        j -= 1
    return 'true'
   

# print(validPar('([{])'))

#TYPE 2
# "5. Valid Parentheses
# Example 1: Input: s = ""()"" Output: true
# Example 2:Input: s = ""()[]{}"" Output: true
# Example 3: Input: s = ""(]"" Output: false"

# def validParn(s):
#     refD = {
#         "(" : ")",
#         "[" : "]",
#         "{" : "}"
#     }
#     l = []
#     # print( "]" in refD
#     x = ''
#     for i in s:
#         if i in refD.keys():
#             l.append(i)
#             x = i
#         elif i in refD.values() and i == refD[x] :
#             l.pop()
#     if len(l) > 0:
#         return 'false'
#     else:
#         return 'true'

# print(validParn('()[]{}'))

def validParn(s):
    refD = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    l = []
    # print( "]" in refD
    for i in s:
        if i in refD:
            l.append(refD[i])
        else:
            if len(l) > 0 and l[-1] == i:
                l.pop()
            else:
                l.append(i)
    if len(l) > 0:
        return 'false'
    else:
        return 'true'


print(validParn("()[]{}}"))