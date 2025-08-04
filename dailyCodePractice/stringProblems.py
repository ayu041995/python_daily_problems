# "7. Find the Index of the First Occurrence in a String

# Example 1: Input: haystack = ""sadbutsad"", needle = ""sad"" Output: 0
# Explanation: ""sad"" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2: Input: haystack = ""leetcode"", needle = ""leeto"" Output: -1
# Explanation: ""leeto"" did not occur in ""leetcode"", so we return -1.
# "
# -------
# "2. Longest Substring Without Repeating Characters

# Input: s = ""abcabcbb"" Output: 3 
# Explanation: The answer is ""abc"", with the length of 3.

# Input: s = ""bbbbb"" Output: 1 
# Explanation: The answer is ""b"", with the length of 1.

# Input: s = ""pwwkew"" Output: 3
# Explanation: The answer is ""wke"", with the length of 3.
# "

# sadbutsad sad
# a=0
# b = 3


def firstOccurance(string,subString):
    a = 0
    # b = len(subString)
    strMatch = ''
    while a < len(string):
        strMatch = strMatch + string[a]
        # print(strMatch)
        if strMatch == subString:
            return (a-(len(subString)))
        if len(strMatch) == len(subString):
            strMatch = ''
            a = abs(a - len(subString))
            continue
        a += 1
        # b += 1
    # return -1

print(firstOccurance("saadbutsabcadbbsad","sabca"))


# def firstOccurance(string,subString):
#     str1 = ''
#     i = 0
#     while i < len(string):
#         j = i + len(subString)
#         str1 = str1 + string[i:j]
#         if str1 == subString:
#             return i
#         else:
#             str1 = ''
#         i += 1   

# print(firstOccurance("saadbutsabcadbbsad","sabcad"))