"""
Assignment 7 - EM624
@author - Rushabh Barbhaya

Problem Statement - Analysis on Pros and Cons of Animal Testing
"""

#Import all the necessary libraries
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import sentiwordnet as swn
from wordcloud import WordCloud

#Using regular expressions form nltk
tokenizer = RegexpTokenizer(r'\w+')

#Importing the pros, cons and stopwords file.
in_file_1 = open("pro.txt", "r")
in_file_2 = open("cons.txt", "r")
control_file = open("stopwords_en.txt", "r")

#Reading the input files and converting them to lower case
pro_read = in_file_1.read().lower()
cons_read = in_file_2.read().lower()
control_read = control_file.read().lower()

#Replacing the new line command with space ("\n" to " ")
pro_read = pro_read.replace("\n", " ")
cons_read = cons_read.replace("\n", " ")
control_read = control_read.replace("\n", " ")

#Removing Punctuations and tokenizing
pro_read = tokenizer.tokenize(pro_read)
cons_read = tokenizer.tokenize(cons_read)
control_read = tokenizer.tokenize(control_read)

#Adding certain words for this case senario for "animal testing"
control_read.append("animal")
control_read.append("animals")
control_read.append("testing")
control_read.append("tested")
control_read.append("test")
control_read.append("tests")

#Removing numerial data
alpha_pro = []
alpha_con = []

for i in pro_read:
	if i.isdigit() == False:
		alpha_pro.append(i)

for j in cons_read:
	if j.isdigit() == False:
		alpha_con.append(j)

#Removing stopwords
cleaned_pro = []
cleaned_con = []
for i in alpha_pro:
	if i not in control_read:
		cleaned_pro.append(i)

for j in alpha_con:
	if j not in control_read:
		cleaned_con.append(j)
 
#Creating bigrams       
bigrammed_pro = list(nltk.bigrams(cleaned_pro))
bigrammed_cons = list(nltk.bigrams(cleaned_con))

#Creating a string of all the cleaned text
pro_data = " ".join(cleaned_pro)
con_data = " ".join(cleaned_con)

#Plotting a WordCloud of all the Cleaned Pro text
plt.figure()
wc = WordCloud(background_color="white", max_words=100)
wc.generate(pro_data)
wc.to_file('Pro.png')
plt.title("Pros Data - WordCloud")
plt.imshow(wc)
plt.axis('off')
plt.show()

#Plotting a WordCloud of all the Cleaned Cons text
plt.figure()
wc = WordCloud(background_color="white", max_words=100)
wc.generate(con_data)
wc.to_file('Pro.png')
plt.title("Cons Data - WordCloud")
plt.imshow(wc)
plt.axis('off')
plt.show()

#Sentiment Calculation
Positive_Score_Pro = 0
Negetive_score_Con = 0
Positive_Score_Con = 0
Negetive_score_Pro = 0

for i in cleaned_pro:
    try:
        sentiment_pos = swn.senti_synset(i + '.n.03').pos_score()
        Positive_Score_Pro += sentiment_pos
        sentiment_con = swn.senti_synset(i + '.n.03').neg_score()
        Negetive_score_Pro += sentiment_con
    except:
        try:
            sentiment_pos = swn.senti_synset(i + '.v.03').pos_score()
            Positive_Score_Pro += sentiment_pos
            sentiment_con = swn.senti_synset(i + '.v.03').neg_score()
            Negetive_score_Pro += sentiment_con
        except:
            continue
                        
for j in cleaned_con:
    try:
        sentiment_pos = swn.senti_synset(j + '.n.03').pos_score()
        Positive_Score_Con += sentiment_pos
        sentiment_con = swn.senti_synset(j + '.n.03').neg_score()
        Negetive_score_Con += sentiment_con
    except:
        try:
            sentiment_pos = swn.senti_synset(j + '.v.03').pos_score()
            Positive_Score_Con += sentiment_pos
            sentiment_con = swn.senti_synset(j + '.v.03').neg_score()
            Negetive_score_Con += sentiment_con
        except:
        	continue


#Printing the sentimental scores
print "\n\n---------------------------"
print "Total of Positive Score of all the Pros are:", Positive_Score_Pro
print "Total of Negative Score of all the Pros are:", Negetive_score_Pro
print "---------------------------"
print "Total of Positive Score of all the Cons are:", Positive_Score_Con
print "Total of Negative Score of all the Cons are:", Negetive_score_Con
print "---------------------------"