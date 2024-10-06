
#Zoe Chow, 014

#~~~~~~Part A~~~~~~~~~~~~~~

#importing some modules
import random
from datetime import date

#call the class
class Passenger():

    #constructor function w arguments for name, meal, birth year
    def __init__(self, first_name, last_name, meal, birth_year):
        #assigning each argument to the property
        self.first_name = first_name
        self.last_name = last_name
        self.meal = meal
        self.birth_year = birth_year

        #create an empty string
        num = ""

        #generate a random 10 digit num
        #iteratre 10 times
        for i in range(0, 10):
            #pick a random number and add to the string
            num += str(random.randint(0, 9))

        #assign the final string as the passenger ID
        self.passenger_ID = num

    #check if minor function
    def is_minor(self):
        #subtract birth year from current year and see if 18 years
        if date.today().year - self.birth_year <= 18:
            #if less than 18, its a minor
            return True
        else:
            return False

    #function for getting name
    def get_full_name(self):
        #return first and last name 
        return self.first_name + " " + self.last_name

    #function for getting initials
    def get_initials(self):
        #retrun pos 0 of first and last name
        return self.first_name[0] + self.last_name[0]


#~~~~~~~~~~~Part B~~~~~~~~~~~~~~~

#coach class
class Coach():

    #constructor
    def __init__(self, seq_num, rows, seats):
        self.seq_num = seq_num
        self.rows = rows
        self.seats = seats

        #empty list for setting up the seat chart
        layout = []

        #creating the seat chart
        #make 1 row by multiplying the number of seats
        for seat in range(0, rows):
            #make the bus by duplicating that row by num rows
            layout.append(list(seats * "_"))

        #assign the list as seating chart
        self.seating_chart = layout

    #add passenger
    def add_passenger(self, passenger, row, seat):
        #ensure seat is a letter
        if type(seat) != str:
            return "Pleae enter a letter for seat"
        
        #convert seat letter into number using ASCII
        seat_num = ord(str.lower(seat)) - ord("a")

        #ensure row num is not 0 or less
        if row <= 0:
            return "That is not a valid seat"

        #exception case for valid seats
        try:
            #assign pos as the position in the list of seat chart
            pos = self.seating_chart[row - 1][seat_num]
        #if it returns index error
        except IndexError:
            #inform user
            return "That is not a valid seat"

        #if the position of the seat is valid
        #and it is empty 
        if pos == "_":
            #assign the value of that spot to be the passenger's data
            self.seating_chart[row - 1][seat_num] = passenger
        else:
            #inform user there is another passenger there
            return "There is already a passenger in that seat"
            
    def get_passenger_for_seat(self, row, seat):
        #ensure seat is a letter
        if type(seat) != str:
            return "Please enter a letter for seat"
        
        #convert seat letter into number using ASCII
        seat_num = ord(str.lower(seat)) - ord("a")

        #ensure row num is not 0 or less
        if row <= 0:
            return "That is not a valid seat"

        #exception case for valid seats
        try:
            #assign pos as the position in the list of seat chart
            pos = self.seating_chart[row - 1][seat_num]
        #if it returns index error
        except IndexError:
            #inform user
            return "That is not a valid seat"

        #if the position of the seat is valid
        #and it is empty 
        if pos == "_":
            #return nothing
            return "This seat is empty"
        else:
            #return the passenger's full name
            return self.seating_chart[row - 1][seat_num].get_full_name()

    #function for finding seat by passenger id
    def get_seat_for_passenger(self, passenger_ID):

        #iteratre through all the rows
        for i, row in enumerate(self.seating_chart):
            #iterate through all the seats in each row
            for j, seat in enumerate(row):
                #if the seat isnot empty
                if seat != "_":
                    #check if passenger id matches the search
                    if self.seating_chart[i][j].passenger_ID == passenger_ID:
                        #return the row and seat number if it does
                        return str(i + 1) + str.upper(chr(j + 97))
                    
        #return the passenger is not here if not found
        return "Passenger not found in any seat"


    #function for finding meal by row and seat
    def get_meal_for_seat(self, row, seat):

        #ensure seat is a letter
        if type(seat) != str:
            return "Please enter a letter for seat"
        
        #convert seat letter into number using ASCII
        seat_num = ord(str.lower(seat)) - ord("a")

        #ensure row num is not 0 or less
        if row <= 0:
            return "That is not a valid seat"

        #exception case for valid seats
        try:
            #assign pos as the position in the list of seat chart
            pos = self.seating_chart[row - 1][seat_num]
        #if it returns index error
        except IndexError:
            #inform user
            return "That is not a valid seat"

        #if the position of the seat is valid
        #and it is empty 
        if pos == "_":
            #return nothing
            return "This seat is empty"
        else:
            #return the passenger's meal
            return self.seating_chart[row - 1][seat_num].meal

    #printing the seating chart
    def print_seating_chart(self):
        #empty string for the column header
        header_string = ""
        
        #start with column headers
        #iterate through all the letters in the seats
        for i in range(0, self.seats):
            #column num convert to ASCII 
            column = str.upper(chr(i + 97))
            #add it to the header string w spacing
            header_string += "   " + column
        #print the header
        print(header_string)

        #iteratre through all the rows
        for i, row in enumerate(self.seating_chart):
            #make a new empty string for the row
            row_string = ""
            #add the header of the row to the start of the string
            row_string += str(i + 1)
            
            #iterate through all the seats in each row
            for j, seat in enumerate(row):
                #if the seat not empty
                if seat == "_":
                    #add an empty seat to the string
                    row_string += "  --"
                #if not empty
                else:
                    #add the passenger's initials to the string
                    row_string += "  " + self.seating_chart[i][j].get_initials()

                #if the current seat is the last in the row
                if j == self.seats -1:
                    #print the row string
                    print(row_string)

    #function for tracking minors
    def age_counter(self):
        #starting int
        minors = 0

        #iterate through each row
        for i, row in enumerate(self.seating_chart):
            #iterate through all the seats in each row
            for j, seat in enumerate(row):
                #if the seat isnot empty
                if seat != "_":
                    #check if passenger is a minor
                    if self.seating_chart[i][j].is_minor() == True:
                        #add to the minor count
                        minors += 1
        #return the counted num
        return minors

    #function for tracking meal types
    def meal_counter(self, meal_type):
        #var for meals
        total = 0

        #iterate through each row
        for i, row in enumerate(self.seating_chart):
            #iterate through all the seats in each row
            for j, seat in enumerate(row):
                #if the seat isnot empty
                if seat != "_":
                    #check what type of meal the passenger has
                    if self.seating_chart[i][j].meal == meal_type:
                        #add to the meal count if it matches
                        total += 1
        #return the counted num
        return total


#~~~~~~~~~~Part C~~~~~~~~~~~~~~~
#function for train
class Train():

    #constructor
    def __init__(self, first_class, standard_class, stops, date, start_time):
        #empty lists for first and standard coaches
        self.fc = []
        self.sc = []

        #iterate through the num given for each and create a coach
        #according to the class
        for i in range(0, first_class):
            #add a first class coach to fc list
            self.fc += [Coach(first_class + 1, 10, 3)]

        for j in range(0, standard_class):
            #add a standard coach to sc list
            self.sc += [Coach(standard_class + 1, 14, 4)]

        #assign the other variables
        self.stops = stops
        self.date = date
        self.start_time = start_time

    #find start point
    def get_source(self):
        #return index 0 of stops list
        return self.stops[0]

    def get_destination(self):
        #reutnr the last index of stops list
        return self.stops[-1]

    #Booking seats - passenger, sequence num, row and seat num
    def book_seat(self, passenger, seq, row, seat):

        #for coaches in first class
        for i in self.fc:
            #check for the passenger ID using the function from Coach
            if i.get_seat_for_passenger(passenger.passenger_ID) != "Passenger not found in any seat":
                #if found, inform user
                return "Passenger already has a seat"
            #if none found then
            else:
                #for coaches in standard class
                for j in self.sc:
                    #check for passenger id using function from coach
                    if j.get_seat_for_passenger(passenger.passenger_ID) != "Passenger not found in any seat":
                        #if found, return it
                        return "Passenger already has a seat"

        #check the coach num is valid
        #if it is 0 or less or greater than total num of coaches
        if seq <= 0 or seq - 1 >= len(self.fc) + len(self.sc):
            return "That coach does not exist"

        #if the sequence num is smaller than the total of first class coaches
        if seq < len(self.fc):
            #check for seat availability in first class coach at specified index
            if self.fc[seq].get_passenger_for_seat(row, seat) == "This seat is empty":
                #add passenger if valid
                self.fc[seq].add_passenger(passenger, row, seat)
            #if not valid
            else:
                #return the results from get passenger
                return self.fc[seq].get_passenger_for_seat(row, seat)
        #if the seq num is bigger then it is a standard class coach
        else:
            #if the seat is empty
            if self.sc[seq - len(self.fc)].get_passenger_for_seat(row, seat) == "This seat is empty":
                #add passenger
                self.sc[seq - len(self.fc)].add_passenger(passenger, row, seat)
            else:
                #return the results from get passenger
                return self.sc[seq - len(self.fc)].get_passenger_for_seat(row, seat)

    def cancel_booking(self, passenger):
        #iterate over first class coaches
        for coach in self.fc:
            #check if the passenger is in this coach
            #first iterate through rows
            for i, row in enumerate(coach.seating_chart):
                #then iterate through seats in a row
                for j, seat in enumerate(row):
                    #use isinstance to ensure there is instance of Passenger class
                    if isinstance(seat, Passenger) and seat.passenger_ID == passenger.passenger_ID:
                        #remove the passenger from this coach
                        coach.seating_chart[i][j] = "_"
                        return "Booking cancelled"

        #iterate over standard class coaches
        for coach in self.sc:
            #check if the passenger is in this coach
            for i, row in enumerate(coach.seating_chart):
                for j, seat in enumerate(row):
                    #use isinstance to ensure there is an instance of Passenger class
                    if isinstance(seat, Passenger) and seat.passenger_ID == passenger.passenger_ID:
                        #remove the passenger from this coach
                        coach.seating_chart[i][j] = "_"
                        return "Booking cancelled"

        #if passenger not found in any coach
        return "Passenger not found in any seat"

    #function for getting minors
    def get_num_minors(self):
        #var for the num
        total = 0

        #iterate through first class coaches
        for coach in self.fc:
            total += coach.age_counter()

        #iterate through standard class
        for coach in self.sc:
            total += coach.age_counter()

        #return the total
        return total

    #function for getting meal types
    def get_num_meals(self, meal_type):
        #var for the num
        total = 0

        #iterate through first class coaches
        for coach in self.fc:
            total += coach.meal_counter(meal_type)

        #iterate through standard class
        for coach in self.sc:
            total += coach.meal_counter(meal_type)

        #return the total
        return total
        










