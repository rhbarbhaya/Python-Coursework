# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:25:45 2018
Assignment 6 - EM624 - Infomatics for Engineering Management
@author: Rushabh Barbhaya
Each section of exptected answer is seperated by a dashed line.
"""
#Importing all the necessary libraries
import pandas as pd

print "------Output------"
#Importing all the data structures in pandas structure
movies = pd.read_table("movies.dat", header = None, sep = "::", names = ["MovieID", "Title", "Genres"], engine='python')
print "DataFrame Added"
ratings = pd.read_table("ratings.dat", header = None, sep = "::", names = ["UserID", "MovieID", "Rating", "Timestamp"], engine='python')
print "DataFrame Added"
users = pd.read_table("users.dat", header = None, sep = "::", names = ["UserID", "Gender", "Age", "Occupation", "Zip-Code"], engine='python')
print "DataFrame Added"
#Merging movies and ratings 
movie_ratings = movies.merge(ratings, how = "inner")
print "DataFrame Merged"

#Merging movie_rating and users
data = movie_ratings.merge(users, how = "inner")
print "DataFrame Merged"

#Printing the first 3 rows of data
print "\n\n-----------------"
print "\nData in movies.dat"
print movies.head(3)
print "\nData in ratings.dat"
print ratings.head(3)
print "\nData in users.dat"
print users.head(3)

#Printing the merged dataset
print"\n\n------------------\n"
print data.head()

#Printing the number of records for the datasets
print"\n\n------------------"
print "\n\nNumber of records for 'Movies' DataFrame:\t", movies["MovieID"].count()
print "Number of records for 'Ratings' DataFrame:\t", ratings["UserID"].count()
print "Number of records for 'Users' DataFrame:\t", users["UserID"].count()
print "Number of records for 'Data' DataFrame:\t\t", data["UserID"].count()

#Masking the Occupation Dataset
data.Occupation.replace(range(0,21,1), ["Other/not specified", "academic/educator", "artist", "clerical/admin", "college/grad student", "customer service", "doctor/health care", "executive/managerical", "farmer", "homemaker", "K-12 student", "lawyer", "programmer", "retired", "sales/marketing", "scientist", "self-employed", "technician/engineer", "tradesman/craftsman", "unemployed", "writer"], inplace = True)

#Printing the last 3 entries in the dataset
print "\n\n------------------"
print "\n\nSample of data after cleaning the data (last 3)"
print data.tail(3)

#Section Title
print "\n\n------------------"
print "\n\nThe 5 Occupations that give high overall ratings are:"
ordered_data = data.groupby(["Occupation"]).count() #Grouping by Occupation
sorted_data = ordered_data.sort_values(by = "Rating", ascending = False) #Sorting data by largest first
#ratings_data = pd.concat([sorted_data["Rating"], data["Occupation"]]) #Creating a new data frame of the required objects
print "\n", sorted_data["Rating"].head() #First 5 Occupations with higher average rating