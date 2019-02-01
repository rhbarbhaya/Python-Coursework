import matplotlib.pyplot as plt 

def get_index(parts):
	if parts[1] == "1":
		if parts[0] == "1" or parts[0] == "2" or parts[0] == "3":
			return 0
		elif parts[0] == "4" or parts[0] == "5" or parts[0] == "6":
			return 2
		elif parts[0] == "7" or parts[0] == "8" or parts[0] == "9":
			return 4
	elif parts[1] == "2":
		if parts[0] == "1" or parts[0] == "2" or parts[0] == "3":
			return 1
		elif parts[0] == "4" or parts[0] == "5" or parts[0] == "6":
			return 3
		elif parts[0] == "7" or parts[0] == "8" or parts[0] == "9":
			return 5

file_handle = open("marketingdata.txt","r")
data = file_handle.readlines()

counts = [0,0,0,0,0,0]

for line in data:
	parts = line.strip().split()
	if "NA" in line:
		pass
	else:
		index = get_index(parts)
		counts[index] += 1

Lower_Income_Total = counts[0] + counts[1]
Middle_Income_Total = counts[2] + counts[3]
Higher_Income_Total = counts[4] + counts[5]
Pie_Diag = []
Pie_Diag.append(Lower_Income_Total)
Pie_Diag.append(Middle_Income_Total)
Pie_Diag.append(Higher_Income_Total)

print "\n\tLower Income\tMiddle Income\tHigher Income"
print "Male:\t\t", counts[0], "\t\t", counts[2], "\t\t", counts[4]
print "Females:\t", counts[1], "\t\t", counts[3], "\t\t", counts[5]
print "--------------------------------------------------------"
print "Total:\t\t", Lower_Income_Total, "\t\t", Middle_Income_Total, "\t\t", Higher_Income_Total

name1 = ["Lower Income Men", "Lower Income Women", "Middle Income Men", "Middle Income Women", "Higher Income Men", "Higher Income Women"]
name2 = ["Lower Income", "Middle Income", "Higher Income"]

plt.figure()
plt.subplot(221)
x = [0,1,2,3,4,5]
plt.bar(x, counts)
plt.xticks(x, name1, rotation = 90)
plt.xlabel("Income Level: Groups")
plt.ylabel("Income")

plt.subplot(222)
plt.pie(Pie_Diag, labels = name2, rotatelabels = True, startangle = 180, labeldistance = 0.28)

plt.suptitle("Income VS Sex")
plt.show()