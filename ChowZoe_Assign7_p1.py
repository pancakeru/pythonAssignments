
#Zoe Chow, 014

#~~~~~~~~~~~~~~~~~USERNAME VALIDATION~~~~~~~~~~~~~~~~~~~~~~~~~~~
#loop the program until the username is valid
while True:
    #get input and set the valid bool to true
    username = input("Enter username: ")
    valid = True

    #validate length of username
    print(f"* Length: {len(username)}")
    if not len(username) in range(6, 13):
        print("ERROR: Username must be 6-12 characters long.")
        valid = False #if the condition doesnt meet, this bool will store that 

    #validate alphanumeric characters of username
    print(f"* Alphanumeric: {username.isalnum()}")
    if not username.isalnum():
        print("ERROR: Username cannot contain any special characters.")
        valid = False

    #validate first character of username and make sure it is not digit
    print(f"* First character is digit: {username[0].isdigit()}")
    if username[0].isdigit():
        print("ERROR: First character cannot be a digit.")
        valid = False

    #validate last character of username and if it is a digit
    print(f"* Last character is digit: {username[-1].isdigit()}")
    if username[-1].isdigit():
        print("ERROR: Last character cannot be a digit.")
        valid = False

    #setting counters for each char type
    uppers = 0
    lowers = 0
    numbers = 0

   #counting through the chars in the username 
    for i in username:
        #if the current char is a letter, differentiate between upper and lower
        if i.isalpha():
            #if it is uppercase, add it to upper
            if i.isupper():
                uppers += 1
            #if not, add to lower
            else:
                lowers += 1
        #if it is a digit, do not differentiate
        else:
            numbers += 1

    #print out the number of uppercase chars and validate
    print(f"* Uppercase characters: {uppers}")
    if uppers < 2:
        print("ERROR: Username must contain at least 2 uppercase characters.")
        valid = False

    #print out the number of lowercase chars and validate
    print(f"* Lowercase characters: {lowers}")
    if lowers < 2:
        print("ERROR: Username must contain at least 2 lowercase characters.")
        valid = False

    #prinout the number of digit chars
    print(f"* Digit characters: {numbers}")

    #after all has been evaluated, if any one of the conditions was false it would
    #change the bool "valid" to false, which tells the program to go again
    if valid:
        print("Username is valid!")
        print()
        break
    else:
        print("Username is invalid, please try again.")
        print()


#~~~~~~~~~~~~~~~~~PASSWORD VALIDATION~~~~~~~~~~~~~~~~~~~~~~~~~~~
#loop the program until the password is valid
while True:
    #get input and set the valid bool to true
    password = input("Enter password: ")
    valid = True
    user_detected = False

    #validate length of password
    print(f"* Length: {len(password)}")
    if len(password) < 10:
        print("ERROR: Password must be at least 10 characters long.")
        valid = False #if the condition doesnt meet, this bool will store that

    #check if username is in password
    if username in password:
        user_detected = True

    print(f"* Username is part of password: {user_detected}")
    if user_detected:
        print("ERROR: Username cannot be in the password.")
        valid = False

    #creating a reference for the special characters
    special_chars = "#$%@&!"

    #resetting counters for each type of char
    uppers = 0
    lowers = 0
    numbers = 0
    specials = 0
    invalids = 0

    #iterate through each char in password and sort by type
    for char in password:
        #if it is a letter, sort by upper lower case
        if char.isalpha():
            if char.isupper():
                uppers += 1
            else:
                lowers += 1
        #if not letter and is number, add to number
        elif char.isdigit():
            numbers += 1
        #else check if it is an accepted special char and add
        else:
            if char in special_chars:
                specials += 1
            else:
                invalids += 1

    #print out the number of uppercase chars and validate
    print(f"* Uppercase characters: {uppers}")
    if uppers < 2:
        print("ERROR: Password must contain at least 2 uppercase characters.")
        valid = False

    #print out the number of lowercase chars and validate
    print(f"* Lowercase characters: {lowers}")
    if lowers < 2:
        print("ERROR: Password must contain at least 2 lowercase characters.")
        valid = False

    #print out the number of digit chars and validate
    print(f"* Digit characters: {numbers}")
    if numbers < 2:
        print("ERROR: Password must contain at least 2 digit characters.")
        valid = False

    #print out the number of lowercase chars and validate
    print(f"* Special characters: {specials}")
    if specials < 2:
        print("ERROR: Password must contain at least 2 special characters.")
        valid = False

    #prinout the number of invalid chars
    print(f"* Invalid characters: {invalids}")
    
    #after all has been evaluated, if any one of the conditions was false it would
    #change the bool "valid" to false, which tells the program to go again
    if valid:
        print("Password is valid!")
        print()
        break
    else:
        print("Password is invalid, please try again.")
        print()


    
     
