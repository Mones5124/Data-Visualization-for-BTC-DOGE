import csv
from datetime import datetime as dt
import pandas as pd
import calendar

folder = "/Users/juanm./Documents/Coding/Python/CSV things/Best BTC days/"
filename = "bitcoin_2016-8-5_2021-4-17.csv"
#filename = "DOGE-USD.csv"
#filename = "/Users/juanm./Documents/Coding/Python/CSV things/Best BTC days/bitcoin_2016-8-5_2021-4-17.csv"
#import a file that you want and then change the names to match the stock ticker symbol

all_data = pd.read_csv(folder+filename)

#print(all_data.head())
all_data.pop("Low")
all_data.pop("High")
#all_data.pop("Market Cap")
#Market Cap not in yahoo finance data for DogeCoin

#print(all_data.head())

all_data['Date'] = pd.to_datetime(all_data["Date"]).dt.strftime('%A')
all_data["Change"] = ((all_data["Close"] - all_data["Open"])/all_data["Open"])*100
#all_data.pop("Date")
print(all_data.tail())

Mon = Tues = Wed = Thurs = Fri = Sat = Sun = all_data

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#sorts the original data and turns the day into the index so this index is kept for the Pandas Series later
#we must reindex so it doesn't use alphabetical order, we want it to use weekday order

all_data['Date'] = pd.Categorical(all_data['Date'], categories=days, ordered=True)
all_data = all_data.sort_values('Date')


"""Pandas Series:"""
by_day = all_data.groupby('Date')

mean_change_by_day = by_day.Change.mean()
print(mean_change_by_day)

volume_by_day = by_day.Volume.mean()
print(volume_by_day)

from matplotlib import pyplot as plt

print(filename[:8])

plt.title(filename + " - Mean Change by Day")
mean_change_by_day.plot(x = "Date", y = "", kind = "bar")
plt.show()

plt.title(filename + " - Mean Volume by Day")
volume_by_day.plot(x = "Date", y = "", kind = "bar")
plt.show()

"""
def split_dataframe():
	Mon = all_data.apply()
"""

"""
with open(filename, newline="") as File:
	reader = csv.reader(File)
	header = next(reader)
	#convert data types accordingly
	#Date, Open, High, Low, Close, Volume
	data = []
	useful_data = []
	mon = tues = wednes = thurs = fri = sat = sun = []
	for column in reader:
		date_time = dt.strptime(column[0], "%b-%d-%Y")
		#<Format that the time is 
		#https://www.programiz.com/python-programming/datetime/strptime
		date = dt.strftime(date_time, "%A")
		#converts it into only showing the weekday

		open_price = float(column[1])
		#high = float(column[2])
		#low = float(column[3])
		close = float(column[4])
		change = ((close - open_price)/open_price)*100
		#volume = float(column[5]) #disregarded
		data.append([date, open_price, close, change])
		useful_data.append([date, change])

		if date = "Monday":
			mon.append([date, change])
		elif date = "Tuesday":

		elif date = "Wednesday":

		elif date = "Thursday":

		elif date = "Friday":

		elif date = "Saturday":
		
		elif date = "Sunday":

		else:
			print("Code is broken " + column)

		#Organizing the format given in the imported file
		#Importing all the the data in the imported file as variables per day

print("Imported")
#print(len(useful_data))
print(data)

#print(contracts)

with open(folder+"/BTC days"+".csv", "w", newline="") as newfile:
	writer = csv.writer(newfile)
	i = 0
	#writer.writerow([str(data[i]+ "		" + data[i+1])])
	for i in range (1,len(useful_data)):
		writer.writerow(useful_data[i])
		#i+=2
"""