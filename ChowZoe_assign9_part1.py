
#Zoe Chow

#getting access to my files
import os

# find the directory
folder_path = '/Users/Zoec/Desktop/Comp Sci Assignments 2024/Intro to Comp Sci assignment 9/Assignment 9 Supporting Files/problem1_supporting_files'

# get all files in the directory
files = os.listdir(folder_path)

#list of possible classifications and a prelim total of each
classifications = ["CONFIDENTIAL", "SECRET", "TOP SECRET", "TOP SECRET - SCI"]
doc_nums = [0, 0, 0, 0]

#make dictionary for years, topics, authors
years = {}
topics = {}
authors = {}

#prevent program from crashing by only reading text files (yes i made my stuff crash multiple times)
txt_files = [file for file in files if file.endswith('.txt') and not os.path.isdir(os.path.join(folder_path, file))]

#~~~~~~~~~~~~~~~~~~~~~~EXTRACTING INFO FROM FILE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#read the txt files and iterate over all
for txt_file in txt_files:
    #get the path by joining the directory path with the individual file path
    file_path = os.path.join(folder_path, txt_file)

    #open each file with a context manager in read mode and assign it to a temporary var
    with open(file_path, 'r') as file:
        
        #read contents of file by line
        for line in file:

            #~~~~~~~~~~~CLASSIFICATION~~~~~~~
            #check each classification type by line
            for cl in classifications:
                #add 1 to the appropriate var storing the nums
                if cl in line:
                    doc_nums[classifications.index(cl)] += 1

            #~~~~~~~~~~~YEAR~~~~~~~~~~~~~~~
            #extract the year number from the line with year info
            if 'Year (in BBY):' in line:
                #split it by the ':' and get the number half as a string
                year_str = line.split(':')[1].strip()
                
                #convert the string into an int
                year = int(year_str)

                #check if the year is already in the dictionary
                if year not in years:
                    #if not in the dict, add it as a key with value of 1
                   years[year] = 1
                else:
                    #if it is already there, find it by key and add 1 to value 
                   years[year] += 1

            #~~~~~~~~~~~~TOPIC~~~~~~~~~~~~~~~~
            #p much the same but minus the int conversion
                   
            #extract the topic from the line with topic infor
            if 'Topic:' in line:
                #split it by the : and get the later half and remove additional spaces
                topic = line.split(':')[1].strip()

                #check if already in the topic dict
                if topic not in topics:
                    #if not in the dict, add it as a key with value of 1
                   topics[topic] = 1
                else:
                    #if it is already there, find it by key and add 1 to value 
                   topics[topic] += 1

            #~~~~~~~~~~~~AUTHORS~~~~~~~~~~~~~~~~
            #could i hv made this a function?
            #its all slightly different tho so idk
                   
            #extract the topic from the line with topic infor
            if 'Author(s):' in line:
                #split it by the : and get the later half and remove additional spaces
                author_check = line.split(':')[1].strip()

                #check to see if there are multiple authors by looking for ',' 
                if ',' in author_check:
                    #if there are, split by ',' and make list of names
                    author = list(author_check.split(', '))
                else:
                    author = [author_check]
                
                #check if already in the topic dict
                for guy in range(0, len(author)):
                    if author[guy] not in authors:
                        #if not in the dict, add it as a key with value of 1
                       authors[author[guy]] = 1
                    else:
                        #if it is already there, find it by key and add 1 to value 
                       authors[author[guy]] += 1

#remove duplicates from the classification list
doc_nums[1] -= doc_nums[2] #remove TOP SECRET from SECRET
doc_nums[2] -= doc_nums[3] #remove TOP SECRET - SCI from TOP SECRET
#this order matters cuz it adds up to 10,000

#create a dictionary of classications for easier tracking
#(and bc i did not think of this earlier)
dictionary = dict(zip(classifications, doc_nums))

#sort the years dictionary in descending order by key
sorted_years = dict(sorted(years.items(), reverse=True))

#create norida files file
norida_file = open("norida_files_report.txt", "w")


#~~~~~~~~~~~~~~~~~~~~~~~~WRITING TO THE NORIDA FILE~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Open norida for writing with a context manager
with open("norida_files_report.txt", "w") as norida_file:

    #~~~~~~~~~~~~~PRINTING CLASSIFICATIONS~~~~~~~~~~~~~
    #function for printing the classification doc total summary
    #takes 2 lists as parameters (classifcation and total num of each)
    def class_sum(classes, totals):
        #make new string for the final input
        summary = ""
        
        # add the header to the string
        summary += "===============================\n"
        summary += "DOCUMENT CLASSIFICATION SUMMARY\n"
        summary += "===============================\n\n"

        #add the table header to the string
        summary += format("Classifications", "<20") + format("Number of Documents", "<20") + "\n"

        #add the info for each row using the inputted lists
        for i in range(0, 4):
            summary += format(classes[i], "<20") + format(totals[i], "<20") + "\n"

        #return the final string
        return summary
    
    # write the output of class_sum function to the file
    norida_file.write(class_sum(classifications, doc_nums) + "\n" + "\n")


    #~~~~~~~~~~~~~PRINTING YEARS~~~~~~~~~~~~~
    #new function for printing the years and pub dates
    def year_sum(year_dict):
        #the first part is mostly the same
        #make new string for the final input
        summary = ""
        
        # add the header to the string
        summary += "===============================\n"
        summary += "DOCUMENT PUBLICATION SUMMARY\n"
        summary += "===============================\n\n"

        #add the table header to the string
        summary += format("Year (BBY)", "<20") + format("Number of Documents", "<20") + "\n"

        #iterate through every pair in the dict and print
        for key, value in year_dict.items():
            summary += format(key, "<20") + format(value, "<20") + "\n"

        return summary

    # write the output of year_sum function to the file
    norida_file.write(year_sum(sorted_years) + "\n" + "\n")


    #~~~~~~~~~~~~~PRINTING TOPICS~~~~~~~~~~~~~
     #new function for printing the topics
    def topic_sum(topic_dict):

        #i couldve just made one base function and then iterate the variables
        #but its too late rip just go with it
        #u live and u learn
        
        summary = ""
        
        # add the header to the string
        summary += "===============================\n"
        summary += "DOCUMENT TOPIC SUMMARY\n"
        summary += "===============================\n\n"

        #add the table header to the string
        summary += format("Topic", "<30") + format("Number of Documents", "<30") + "\n"

        #iterate through every pair in the dict and print
        for key, value in topic_dict.items():
            summary += format(key, "<30") + format(value, "<30") + "\n"

        return summary

    # write the output of topic_sum function to the file
    norida_file.write(topic_sum(topics) + "\n" + "\n")


    #~~~~~~~~~~~~~PRINTING AUTHORS~~~~~~~~~~~~~
     #new function for printing the topics
    def author_sum(author_dict):

        #oops
        
        summary = ""
        
        # add the header to the string
        summary += "===============================\n"
        summary += "DOCUMENT AUTHOR SUMMARY\n"
        summary += "===============================\n\n"

        #add the table header to the string
        summary += format("Author", "<30") + format("Number of Documents", "<30") + "\n"

        #iterate through every pair in the dict and print
        for key, value in author_dict.items():
            summary += format(key, "<30") + format(value, "<30") + "\n"

        return summary

    # write the output of author_sum function to the file
    norida_file.write(author_sum(authors) + "\n" + "\n")

#close the file BYE BYE 
norida_file.close()


