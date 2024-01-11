#PyBank Assignment


#import the csv file
import os
import csv
#file path
csvpath= os.path.join("Resources", "budget_data.csv")
#lists to store data
row = []
total_months = []
greatest_increase =[]
greatest_decrease = []
net_total = 0
#open and read csv
with open(csvpath) as csvfile:
	csvreader= csv.reader(csvfile, delimiter =',')
#skip header
	csvheader = next(csvfile)
	print (f"Header: {csvheader}")

#analyze and calculate number of months
	total_months = sum(1 for _  in csvreader)

print (f"Total Months: {total_months}")

#analyze and calculate net total amount of Profit/loss over the entire period
column_index= 1
	for row in csvreader:
	net_total += int(row[column_index])

print (f'Total: {net_total}')



#calculate and analyze greatest increase in profits(date and amount) over entire period (min and max)





#calculate and analyze greatest decrease in profits (date and amt) over entire period




#final script needs to print out analysis in terminal and export a text file with results
