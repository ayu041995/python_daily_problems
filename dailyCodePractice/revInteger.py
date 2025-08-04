#  Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
# causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
# then return 0.
# Input: x = 123 Output: 321, 
# Input: x = -123 Output: -321, 
# Input: x = 120 Output: 21


# def revInt(int1):
#     # print(int1)
#     str1 = str(int1)
#     revStr = ''
#     for i in range(len(str1)-1,-1,-1):
#         print(i)
#         revStr = revStr + str1[i]
#     print(type(int(revStr)))

# print(revInt(321))



def revInt(int1):

    if int1 > 0:
        str1 = str(int1)
        str3 = ''.join(reversed(str1))
        str2 = int(str3)
    else:
        str1 = (int1 * -1)
        str1 = str(str1)
        str3 = ''.join(reversed(str1))
        str4 = int(str3)
        str2 = str4 * -1
    return str2

print(revInt(120))