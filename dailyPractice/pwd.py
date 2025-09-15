# Write a script to validate a password based on the following enhanced criteria:

# The password must be at least 10 characters long.
# It should contain at least one uppercase letter, one lowercase letter, and one numeric digit.
# It must contain at least one special character (e.g., @, #, $, %).
# The password should not contain any consecutive repeating characters (e.g., 'aa', '11').
# If the password fails the validation, output the specific reason why.
# Once validated, the script should hash the password using a secure hashing algorithm (e.g., bcrypt) before storing it. Explain how this can be integrated with an API to support password updates.



def pwdValidate(pwd):
    if len(pwd) < 10:
        print("password must be at least 10 characters long")
    
    has_upper = False
    has_lower = False
    has_digit = False

    spcial_character = '@#$%'
    spcial_character_count = 0
    for j in pwd:
        if j in spcial_character:
            spcial_character_count += 1
    if spcial_character_count == 0:
        print("PWD must contain at least one special character")
        
    for i in pwd:
        # print(i)
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True  
        else:
            # print("PWD should have at least one uppercase letter, one lowercase letter, and one numeric digit")
            return False

    # if has_upper == False :
    #     print("PWD should have at least one uppercase letter") 
    # if has_lower == False:
    #     print("PWD should have at least one lower letter") 
    # if has_digit == False:
    #     print("PWD should have at least one digit") 
    
    for k in range(len(pwd)-1):
        if pwd[k] == pwd[k+1]:
            print("password should not contain any consecutive repeating characters")
        

print(pwdValidate("1T3#AbubgdSsdf@T"))
# print(pwdValidate("T1ajshdfhgfcjfhg"))

