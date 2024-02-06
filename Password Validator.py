import re

#password Validator

"""
This program takes a password as an input and checks it against the following
conditions to ensure that it matches the valid password standards.
The conditions are
1) Passwords should be 8 to 16 characters in length
2) password should contain alphabets
    --> atleast 1 capital
    --> atleast 1 small letter
3) Password should conatin atleast 1 number
4) password should contain any of the following special characters
    '!', '@', '#', '_'
"""


def password_validator(password):


    common_passwords = ["123456","123456789","12345","qwerty","password","12345678","111111","123123","1234567890","1234567","qwerty123","000000","1q2w3e","aa12345678","abc123","password1","1234","qwertyuiop","123321","password123"]

    if password in common_passwords:
        res = 0
        print ("common password cannot be used")
        
    else:
        
        count = 0

        pwd_len = len(password)
        print("password has a length of ", pwd_len)

        if pwd_len<8 or pwd_len>16:
            print ("Password must contain minimum 8 or maximum 16 characters")
        else:
            print ("Password meets the length requirements")

        #Step 2: check if the password contains alphabets numbers and the special characters

        cap_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        small_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        num_list = ["0","1","2","3","4","5","6","7","8","9"]
        spec_list = ["!","@","#","_"]
        char_list = cap_list+small_list+num_list+spec_list

        #print(char_list)

        # Validating the characters in the password based on the above lists of character
        
        # Check whether the string contains atleast 1 allowed special characters
        
        pattern = "[!@#_]"
        spec_char_res = re.search(pattern,password)
        print(spec_char_res)

        if spec_char_res != None:

            # check the string against approved character list to  see if there are any non approved characters

            for i in password:
      
                if i in char_list:
                    count = count+1
                    if 8<= count <=16:
                        res = 1
                    else:
                        res = 0
                else:
                    res = 0
                    print("invalid chararacter ",i)
                    print ("check capital & small letters numbers and special characters ")
                    break
        else:
            res = 0
            print ("Password must contain a special charater from !@#_")
            
                

        # check if the password has the correct length  and characters
        if 8 <= pwd_len <= 16 and res == 1:
            print ("Strong password")
        else:
            print("""INVALID PASSWORD: Please eneter a password based on the following conditions
        1) Passwords should be 8 to 16 characters in length
        2) password should contain alphabets
            --> atleast 1 capital
            --> atleast 1 small letter
        3) Password should conatin atleast 1 number
        4) password should contain any of the following special characters
            '!', '@', '#', '_'
        """)

# Calling the password validator method
pwd = "123456"
password_validator(pwd)

