#PyPoll assignment

#Import csv
import os
import csv

#Assign file path
csvpath= os.path.join("resources",'election_data.csv')

#lists to store data
total_votes= 0
candidate_list = []
specific_candidate =[]
vote_count =[]
vote_percent =[]
#open csv file
with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile,delimiter =',')
#skip header
	csvheader=next(csvfile)
#create for loop to go through data
	for row in csvreader:
#count the total number of ballots (votes) and store them in total_votes variable
		total_votes +=1
#set row 2 which is candidate names to candidate list
		candidate_list.append(row[2])
#using candidate list find each specific candidate that is mentioned
	for x in set(candidate_list):
		specific_candidate.append(x)
#y= total votes by that specific candidate, use .append(y) to add each vote total to the vote_count list
		y= candidate_list.count(x)
		vote_count.append(y)
#z=percent of the votes rounded 3 decimal places and appended to the vote_percent list
		z='{:.3f}'.format((y/total_votes)*100)
		vote_percent.append(z)
#find winner by finding the max and use vote_count index to find winnder name
	winning_vote= max(vote_count)
	winner = specific_candidate[vote_count.index(winning_vote)]


#print everything in order
print ('Election Results')
print ('---------------------')
print (f'Total votes: {total_votes}')
print ('------------------------')
for i in range(len(specific_candidate)):
	print(specific_candidate[i]+ ':' + str(vote_percent[i]) + '% ('+str(vote_count[i])+ ')')
print ('----------------------------')
print ("Winner:" + winner)
print ('-----------------------------')

#output as file.txt
file = open('output.txt','w')
file.write('Election Results\n')
file.write('----------------------\n')
file.write(f'Total votes: {total_votes}\n')
file.write('-----------------------\n')
for i in range(len(specific_candidate)):
	file.write(specific_candidate[i]+ ':' + str(vote_percent[i]) + '% ('+str(vote_count[i])+ ')\n')
file.write('--------------------------\n')
file.write('Winner:' + winner)
file.write('\n')
file.write('---------------------------\n')
file.close
