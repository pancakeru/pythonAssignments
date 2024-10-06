
#Zoe Chow, 014

##############
#   Part 1   #
##############

#create a function called shift left that takes 2 parameters
def shift_left(the_word, the_num):

    #create empty string to hold the new string
    new_string = ""

    #go through every char in the string and shift it
    for char in range(0, len(the_word)):

        #if shifting the char is out of range, loop around
        if char + the_num > len(the_word) - 1:
            #use the modulo value to stay within range
            new_string += the_word[the_num % len(the_word) - (len(the_word) - char)]
        #if it is within range, just add the number
        else:
            new_string += the_word[char + the_num]
            
    #return the value for printing
    return new_string


##############
#   Part 2   #
##############

#defining the function and parameters
def swap(the_word, the_chunk):

    #setting up empty string and list
    new_string = ""
    chunks = []

    #splitting the string into chunks by increment
    for char in range(0, len(the_word), the_chunk):
        #define index range of current chunk
        current_chunk = the_word[char: char+the_chunk]
        #add to the chunks list
        chunks.append(current_chunk)

    #iterate through every item in the chunks list
    for i in range(0, len(chunks)):
        #if the item is in an even position
        if i % 2 == 0:
            #check if the swap is possible and in list range
            if i + 1 < len(chunks) and len(chunks[i]) == len(chunks[i+1]):
                #add the swapped chunks to the empty string
                new_string += chunks[i + 1] + chunks[i]
            else:
                #if the item can't be swapped, add it as is
                new_string += chunks[i]
        #if the item is the last position in the list, add it as is
        elif i == len(chunks) - 1:
            new_string += chunks[i]

    #return the new string
    return new_string


##############
#   Part 3   #
##############

#defining the function and parameters
def encrypt(the_word, shift_num, chunk_num):

    #use the shift_left function
    shifted = shift_left(the_word, shift_num)

    #use the swap function on the shift result
    swapped = swap(shifted, chunk_num)

    #return the results
    return swapped


##############
#   Part 4   #
##############

#defining the function and parameters
def decrypt(the_word, shift_num, chunk_num):

    #use the swap function first
    swap_back = swap(the_word, chunk_num)

    #use shift_left and make shift_num negative to reverse it on the swap result
    shift_right = shift_left(swap_back, -shift_num)

    #return the results
    return shift_right


