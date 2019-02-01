"""
Assignment 4

Author: Rushabh Barbhaya

Tip: You can check the average and 24-hour passes for the whole files.
Just replace the data variable to data1 or data2 respectively
"""

import pandas as pd #Importing pandas directory and calling it as pd for convinence
print "\nAssignment 4" #Printing the assignment number

file_handle = open("citi_bike.txt","r") #Importing the text file
data1 = [] #Declaring a variable for storing a list of lists
data_june = [] #Declaring a variable and storing data entries that are in June
for line in file_handle: #Loop for creating a list of lists
    	parts = line.strip().split() #removing any white space and splitting at columns
        data1.append(parts) #Adding parts to list
    	if parts[0].startswith("6"): #Checking if condition in the date column for variables starting in month 6
    		data_june.append(parts) #Adding those parts to january list

print "\nData Added for text file" #Checking the completion of for loop

def Print_details(data): #defining a function for printing details of the text file
    total_miles = 0.0 #Variable for total number of miles
    total_passes = 0.0 #Variable for total number of 24-hour passes
    sorting = [] #Declaring a variable for sorting
	
    for day in data: #loop for index purpose
		distance = float(day[3]) #extracting the column of miles travelled
		total_miles = total_miles + distance #adding and storing the value for calc. average
		passes = float(day[7]) #Extracting the column of 24-hour passes
		total_passes = total_passes + passes #Calculating the total number of passes
    
    sort = sorted(data, key = lambda i:int(i[1]), reverse = True) #Sorting the data list as per column 2
    average_miles = total_miles/len(data) #Calculating the average of miles travelled
    sorting.append([i[0] for i in sort]) #Adding values to sorting list
    print "\nData is from", data[0][0], "to", data[-1][0]
    print "Average of the distance travelled: {:.3f}".format(average_miles) #Printing and formating the average miles to the 3rd decimal
    print "Total 24-hour Passes Sold: ", total_passes #Printing the total passes sold
    print "Top 5 trips are:\n", sorting[0][:5] #Printing top 5 values of dates of total trips
    return #Ending define function and returning all values

file_handle2 = open("citi_bike.csv","r") #Importing a csv file
data2 = [] #Decalring a variable for creating a list of lists
data_jan = [] #Declaring a variable and storing data entries that are in Jan
for line in file_handle2: #Loop for creating a list of lists
    parts = line.strip().split(",") #Clearing white spaces and seperating at comma
    if parts[0].startswith("1"): #Checking if condition in the date column for variables starting in month 1
    	data_jan.append(parts) #Adding those parts to january list
    data2.append(parts) #Adding parts to list
    
print "\nData Added for csv file" #Checking completion of loop
print "\n------ Part 1 ------" #file seperator
Print_details(data_june) #Calling the function for data list
print "\n------ Part 2 ------" #file seperator
Print_details(data_jan) #Calling the function for data1 list 

merged_file = pd.DataFrame(data1 + data2) #Merging the text and csv file and storing it in variable called "merged_file"
print "\n\n____________________________________________________" #Printing line seperator
print "Merged file (text and csv file)" #Printing that line :P
print merged_file #Printing the entire data file
print "end of file" #printing just that

print "\n\n\n--This is the end of the files processing--" #Final step