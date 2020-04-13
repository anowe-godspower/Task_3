# THE CONDITIONS FOR THIS PASSWORD VALIDATOR ARE:
# The Two Passwords Entered must Match
# Minimum 8 characters.
# The alphabets must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ or &].


def password_input():
    symbols = ["_", "@", "$", "&"]
    validator = True
    print("=================================")
    password_raw    = input("Enter Password Here: ")
    password_conf   = input("Confirm Password Here: ")
        
    # Making Sure That The two Passwords match 
    if (password_raw != password_conf):
        print("---------------------------------------")
        print("Passwords Doesn's Match! Please, Please Try Again...!")
        print("1 For Yes or Any Button To Exit.")
        validator = False
        retryPwd = input("Your Choice: ")
        if (retryPwd == "1"):
            password_input()
        else:
            print("Thank You and Goodbye..!")
            exit()
  
    #   Ensuring That the password is a minimum of 8 Characters
    if (len(password_raw) < 8):
        print("---------------------------------------------")
        print("Password Must Be a Minium of 8 Characters, Please Try Agin...!")
        print("1 For Yes or Any Button To Exit.")
        validator = False
        retryPwd = input("Your Choice: ")
        if (retryPwd == "1"):
            password_input()
        else:
            print("Thank You and Goodbye..!")
            exit()
    
    # The Password Must have at least one Number
    if (not any(char.isdigit() for char in password_raw)):
        print("----------------------------------------")
        print("The Password should have at least one Number, Please Try Agin...!")
        print("1 For Yes or Any Button To Exit.")
        validator = False
        retryPwd = input("Your Choice: ")
        if (retryPwd == "1"):
            password_input()
        else:
            print("Thank You and Goodbye..!")
            exit()

    # The Password Must Have at least one upper case letter  
    if (not any(letter.isupper() for letter in password_raw)):
        print("-------------------------------------------")
        print("The Password Must Have at Least One Upper case Letter, Please Try Agin...!")
        print("1 For Yes or Any Button To Exit.")
        validator = False
        retryPwd = input("Your Choice: ")
        if (retryPwd == "1"):
            password_input()
        else:
            print("Thank You and Goodbye..!")
            exit()
    
    # The Password Must Have at least one Lower case letter  
    if (not any(char.islower() for char in password_raw)):
        print("-----------------------------------------------")
        print("The Password Must Have at Least One Lower case Letter, Please Try Agin...!")
        print("1 For Yes or Any Button To Exit.")
        validator = False
        retryPwd = input("Your Choice: ")
        if (retryPwd == "1"):
            password_input()
        else:
            print("Thank You and Goodbye..!")
            exit()

    if (not any(char in symbols for char in password_raw)):  
        print("-----------------------------------------------")
        print("The Password Must Have at Least One of The Special Symbols (_,$,@,&), Please Try Agin...!")
        print("1 For Yes or Any Button To Exit.")
        validator = False
        retryPwd = input("Your Choice: ")
        if (retryPwd == "1"):
            password_input()
        else:
            print("Thank You and Goodbye..!")
            exit()

    if (validator == True):
        print("Valid Password.")
      
password_input()
