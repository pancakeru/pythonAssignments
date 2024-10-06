
#Zoe Chow, 014

import os

#open the names and ranks file (when its in the same directory)
valid_names = open("names_and_ranks.txt", "r")

#create a new file for storing the registered accounts
accounts = open("registered_users.txt", "a")
#close this file
accounts.close()

#check if successfully logged in
logged = False
BYEBYE = False

#create a new file for storing strikes
strikes = open("strikes_info.txt", "a")
#close this file
strikes.close()

#function for checking username in a file
def check_info(username, file_name):
    #variable to store the file info after reading
    info = file_name.read()
    file_name.seek(0)#return the file cursor back to the beginning

    #if the given username is in the info, true or false
    if username in info:
        return True
    else:
        return False

#function for extracting passwords and ranks in file
def find_info(name, file_name, pos):
    #return cursor back to start of file
    file_name.seek(0)

    #iterate over every line
    for line in file_name:
        #if the name is in the line
        if name in line:
            #split the line by ', ' to extract the info at the specified pos
            extract = line.split(', ')[pos].strip()
            #return that value
            return extract

#~~~~~~~~~~~~~~~~~~~~~PROGRAM STARTS HERE~~~~~~~~~~~~~~~~
print("* * * * * * * * * * * * * * * * *")
print("* * WELCOME TO THE DEATH STAR * *")
print("* * * * * * * * * * * * * * * * *")

#~~~~~~~~~while the user isnt logged in~~~~~~~~~~~~
while logged == False:
    #re-open in read mode
    accounts_read = open("registered_users.txt", "r")
    
    #ask for menu input
    query = str.lower(input("Main Menu: Press (l)ogin, (r)egister, (o)rder, (q)uit: "))

    #~~~~~~~LOGIN MODE~~~~~~~~
    if query == "l":
        while True:
            #get user inputs for account
            user = input("Username: ")
            pwd = input("Password: ")

            #check if the username is registered using the function
            registered = check_info(user, accounts_read)

            #if the result is false, tell them to register
            if registered == False:
                print("You do not have an account. To register, select (r)egister.")
                break
            else:
                #check if the password is correct by extracting from accounts file
                correct_pwd = find_info(user, accounts_read, 1)

                #if it matches, congrats
                if pwd == correct_pwd:
                    name = find_info(user, accounts_read, 0)
                    logged = True
                    break
                else:
                    #if it doesnt, try again
                    print(f"Incorrect password for username {user}. Please try again.")

    #~~~~~~REGISTER MODE~~~~~~~~~
    elif query == "r":
        #get user inputs
        name = str.title(input("Name: "))

        #check if it is a valid name that can be registered
        valid = check_info(str.title(name), valid_names)

        #if it is valid, find their rank
        if valid == True:
            #extract rank info form the file
            rank = find_info(name, valid_names, 1)
            #print it out w the header
            print(f"Welcome {rank} {name}. Please choose your account details.")

            #ask for new info input
            new_user = input("Username: ")
            new_pwd = input("Password: ")

            #add this new info to the account file in format Name, Password, Username
            with open("registered_users.txt", "a") as file:
                file.write(name + ", " + new_pwd + ", " + new_user + "\n")
                file.close()
            #print thank u
            print("Thank you. Your account has been created.")

        #if it is not valid
        else:
            #report the mf
            print(f"{name} is not an authorized Imperial Officer. This incident will be reported.")

    #~~~~~~QUIT~~~~~~~~~~~
    elif query == "q":
        print("Thank you for your service to your emperor. Goodbye.")
        break

    elif query == "o":
        print("Please login to use orders.")

#~~~~~~lists of the ranks~~~~~~~~~~
lowbobs = ["ENSIGN", "LIEUTENANT JR"]
goons = ["LIEUTENANT SR", "LT COMMANDER", "COMMANDER", "CAPTAIN", "COMMODORE", "ADMIRAL", "GENERAL"]
topdogs = ["GRAND MOFF", "SUPREME COMMANDER"]

#function for checking and returning each rank
def rank_power(rank):
    if rank in lowbobs:
        return "lowbob" #indicator of what actions u can do
    elif rank in goons:
        return "goon"
    else:
        return "topdog"

#function for striking
def strike():
    #check if there are any ongoing strikes
    ongoing = check_info("ongoing", strikes_read)

    #if there are, inform the user
    if ongoing == True:
        print(f"Strike on {find_info('ongoing', strikes_read, 0)} in progress. Cannot authorize another strike")

        #if there arent
    else:
        #ask for target
        target = str.title(input("Enter Target: "))

        #check if target is Yavin 4
        if target == "Yavin 4":
            #if it is, dont let them do it!!!
            print("Strike on Yavin 4 cannot be authorized. Please check your permissions with the system administrator.")
        else:       
            #add this new info to the strikes file in format Target, Status
            with open("strikes_info.txt", "a") as file:
                file.write(target + ", " + "ongoing")
                file.close()
                #inform the user it is done
            print(f"Strike has been authorized for {target}")

#function for cancelling
def cancel():
    #check if there are ongoing strikes
    strike_yes = check_info("ongoing", strikes_read)

    #if there are, overwrite the file to be empty
    if strike_yes == True:
        print(f"Strike on {find_info('ongoing', strikes_read, 0)} has been cancelled.")
        with open('strikes_info.txt', 'w') as file:
            file.close()
    else:
        #say there are no strikes to cancel
        print("There are no ongoing strikes to cancel.")

#function for marking
def mark():
    #check if there are ongoing strikes
    strike_yes = check_info("ongoing", strikes_read)

    #if there are, overwrite the file to be empty
    if strike_yes == True:
        print(f"Strike on {find_info('ongoing', strikes_read, 0)} has been marked as complete.")
        with open('strikes_info.txt', 'w') as file:
            file.close()
    else:
        #say there are no strikes to cancel
        print("There are no ongoing strikes to mark as complete.")


#~~~~~~~~~~while the user is logged in~~~~~~~~~
while logged == True and BYEBYE == False:
    
    #print it out w the header
    rank = find_info(name, valid_names, 1)
    print(f"Welcome {rank} {name}.")
    
    #ask for menu input
    query = str.lower(input(f"[{user}] Main Menu: (o)rder, (q)uit: "))

    #~~~~~QUIT~~~~~~~~~
    if query == "q":
        print("Thank you for your service to your emperor. Goodbye.")
        break

    #~~~~~ORDER~~~~~~~
    elif query == "o":
        
        #check the user's rank and their permissions
        power = rank_power(rank)

        #separate into different menus depending on rank
        while power == "topdog":

            #open the strikes file for reading
            strikes_read = open("strikes_info.txt", "r")
            
            #new query for action menu
            a_query = str.lower(input(f"[{user}] Action Menu: Press (s)trike, (c)ancel strike, (m)ark complete, (q)uit: "))

            #~~~~~~ordering strikes~~~~~~~~~~
            if a_query == "s":
                strike()

            #~~~~~~~~cancelling~~~~~~~~~~~
            elif a_query == "c":
                cancel()

            #~~~~~~~~~~quitting~~~~~~~~~~ 
            elif a_query == "q":
                #exit the entire program
                print("Thank you for your service to your emperor. Goodbye.")
                BYEBYE = True
                break

            #~~~~~~~~marking as complete~~~~~~~~~~~
            elif a_query == "m":
                mark()

        #if rank isnt super people
        while power == "goon":

            #open the strikes file for reading
            strikes_read = open("strikes_info.txt", "r")

            #check the action query
            a_query = str.lower(input(f"[{user}] Action Menu: Press (m)ark complete, (q)uit: "))

            if a_query == "m":
                mark()
                
            elif a_query == "q":
                #exit the entire program
                print("Thank you for your service to your emperor. Goodbye.")
                BYEBYE = True
                break

        #if u are lowest rank
        while power == "lowbob":
             print("Your rank is insufficient to order anyone around. Try harder.")
             break












             
