#PyBank Assignment


#import the csv file
import os
import csv

#file path
csvpath= os.path.join("Resources", "budget_data.csv")
#lists to store data
row = []
total_months = 0
greatest_increase =0
greatest_decrease = []
net_total = 0
change_list=[]
previous_profit= 0
month_list = []
#open and read csv
with open(csvpath) as csvfile:
	csvreader= csv.reader(csvfile, delimiter =',')
#skip header
	csvheader = next(csvfile)
	#print (f"Header: {csvheader}")- only needed to make sure header is being skipped

#analyze and calculate net total amount of Profit/loss over the entire period
	column_index= 1
	for row in csvreader:
	#within the for loop, find total number of months
		net_total += int(row[column_index])
		total_months += 1
	#using an if clause find the total net profit 
		if total_months == 1:
			previous_profit = int(row[column_index])
	#within the if clause create a new list that will hold the change of profits
		change_list.append(int(row[column_index])-previous_profit)
		previous_profit = int(row[column_index])
	#create a new list that will hold the months of greatest decrease/increase (use this list to compare index to profit)
		month_list.append(row[0])
	#use min and max functions to find greatest increase/decrease
		greatest_increase= max(change_list)
		greatest_decrease = min(change_list)
	#find the specific month by using change_list (that's holding increase/decrease) and comparing the number's index to the month 
		greatest_increase_month = change_list.index(max(change_list))-1 
		greatest_decrease_month = change_list.index(min(change_list))-1  
#use the .pop function to remove the first item in the string of change and month list
change_list.pop(0)
month_list.pop(0)
#use the average to find average change
average = round(sum(change_list)/len(change_list),2)

#print (change_list)- use this to check that the list is appended properly and to check removal of first item
#print all items in order:
print ('Financial Analysis')
print ("------------------------------")
print (f'Total Months: {total_months}')
print (f'Total: {net_total}')
print (f'Average Change:' + '$' + str(average))
print (f'Greatest Increase: {month_list[greatest_increase_month]} (${greatest_increase})')
print (f'Greatest Decrease: {month_list[greatest_decrease_month]} (${greatest_decrease})')

#final script needs to print out analysis in terminal and export a text file with results
# Output files
file= open('output.txt','w')

# Write methods to print to Financial_Analysis_Summary; \n signifies new line
file.write("Financial Analysis")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Total Months: {total_months}")
file.write("\n")
file.write(f"Total: ${net_total}")
file.write("\n")
file.write(f"Average Change:"+ "$"+ str(average))
file.write("\n")
file.write(f"Greatest Increase in Profits: {month_list[greatest_increase_month]} (${greatest_increase})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {month_list[greatest_decrease_month]} (${greatest_decrease}) ")
file.close()
