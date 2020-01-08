import os
import sys
year = "121010110101" #every '1' == month with 31 days, '0' == month with 30 days, '2' == month with 28 days (february)
Feb = [31, 30, 29] #If the day is the theoretical 29th, 30th or 31th of february there is an exception as it falls into march. 
def substractMonth(month): #function that subtracts the necessary number of days (31, 30 or 28) from the initial day variable. This function is looped through until the day variable falls into one of the if statements in the for loop
	global m #counter for the months
	m = m + 1
	global day
	if month=="1":
		day = day-31
		if m == 2 and day in Feb: #exception mentioned above
			print("\n" + "Date: " + str(day - 28) + ".3.2019" + "\n")
			os.execl(sys.executable, sys.executable, *sys.argv)
    
		else:
			return day
	elif month== "0":
		day = day - 30
		return day
	elif month== "2": #if the day falls not into the february/march exception mentioned above, it falls into this exception as february only has 28 days
		day = day - 28
		return day
   
def NumbertoDate():
	global day
	day = int(input("Please enter a day of the year (number between 1-365): "))

	if day <= 31: #If the day is <= 31 it is guaranteed to be in january so there is no point in using the algorithm
		print("\n" + "Date: " + str(day) + ".01.2019" + "\n")
		return
	if day > 365: 
		print("Error: Number exceeds 365. ")
		return
	global m
	m=1
	for month in year: #cycles through the year variable. 
		substractMonth(month)
		if day == 31 and m == 8: #exception for August as it has 31 days. This affects the algorithm and needs an exception
			print("\n" + "Date: " + str(day) + "." + str(m) + ".2019" + "\n")
			return
    
		elif day == 31 and month == "1":
			substractMonth("0")
			print("\n" + "Date: "  + str(day) + "." + str(m) + ".2019" + "\n")
			return
  
		elif day<= 31:
			print("\n" + "Date: " + str(day)+ "." + str(m) + ".2019" + "\n")
			return
		else:
			continue
		
def DateToNumber():
	Day = int(input("Day: "))
	month = int(input("Month: "))
	print("Date: " + str(Day) + "." + str(month) + ".2019")
	M= 1
	for mth in "121010110101":	
		if M == int(month):
			
			print("Number of day: " + str(Day) + "\n")
		if mth == "1":
			
			Day = Day + 31
		if mth == "2":
			Day = Day + 28
		if mth == "0":
			Day = Day + 30
		M +=1
			
while True:
	print("NumberToDate or DateToNumber? (1/2)")
	choice = input("")
	if choice == "1":
		NumbertoDate()
	elif choice== "2":
		DateToNumber()
