# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Constraints


# Each character in the string is an ascii character.

# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2

# SLiding window approach

def count_substring(string, sub_string):
    count = 0
    i = 0
    j = len(sub_string)
    
    while j <= len(string):
        str1 = string[i:j]
        # print(str1)
        if str1 == sub_string:
            count += 1
        i += 1
        j += 1
        
    return count

print(count_substring("ABCDCDC", "CDC"))
print(count_substring("I am an Indian, by birth.", "Birth"))
print(count_substring("ThIsisCoNfUsInG", "is"))