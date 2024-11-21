####### Read in Data #######
#Open File
filename = input("Enter the name of the data file: ")
infile = open(filename, 'r')
#Read lines from File
datalist = []
for line in infile:
    #Get data from line
    date, h, l, r = line.split(',')
    lowtemp = int(l)
    hightemp = int(h)
    rainfall = float(r)
    m, d, y = date.split('/')
    month = int(m)
    day = int(d)
    year = int(y)
    #Put data into list
    datalist.append([day, month, year, lowtemp, hightemp, rainfall])
#Close File
infile.close()

######## Analyze Data ########
#Get date of interest
month = int(input("Enter the month you care about: "))
day = int(input("Enter the day you care about: "))
#Find historical data for date
good_data = []
for singleday in datalist:
    if (singleday[0] == day) and (singleday[1] == month):
        good_data.append([singleday[2], singleday[3], singleday[4], singleday[5]])
#Perform analysis
minsofar = 120
maxsofar = -100
num_good_dates = 0
sumofmin = 0
sumofmax = 0
for singleday in good_data:
    num_good_dates += 1
    sumofmin += singleday[1]
    sumofmax += singleday[2]
    if singleday[1] < minsofar:
        print(minsofar, singleday[1])
    if singleday[2] > maxsofar:
        maxsofar = singleday[2]
avglow = sumofmin / num_good_dates
avghigh = sumofmax / num_good_dates
######## Present Results #########
print("There were", num_good_dates, "days")
print("The lowest temperature on record was", minsofar)
print("The highest temperature on record was", maxsofar)
print("The average low has been", avglow)
print("The average high has been", avghigh)