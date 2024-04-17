import os
import csv
import statistics
election=os.path.join('..','Resources','election_data.csv')


with open(election) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)

#Lists to store data
    candidate=set()
    candidatevotes={}

# rows of data without header line and printing intial total votes, which is all the rows except for the header
    rows=[row for row in csvreader]
    totalvotes=len(rows)    
    print("Election Results")
    print('----------')
    print('Total Votes:',totalvotes)
    print('----------')

# loop to add candidate name to list of candidate with help of Xpert Learning Assistant to specify that 3rd column is all I want to add to candidate name list
    for row in range(0,totalvotes):
        candidatename=rows[row][2]
        candidate.add(candidatename)

# to increase vote per candidate url: https://stackoverflow.com/questions/2632677/python-integer-incrementing-with
        if candidatename in candidatevotes:
            candidatevotes[candidatename]+=1
        else:
            candidatevotes[candidatename]=1

# to calculate percentages from votes above. code given by Xpert Learning Assistant
# understanding of .3f url: https://www.w3schools.com/python/python_string_formatting.asp
    for candidatename, votes in candidatevotes.items():
        percentage=(votes/totalvotes)*100
        print(f"{candidatename}: {percentage:.3f}% ({votes})")
        
# find the candidate with the most votes
# code given by Xpert Learning Assistant
# understanding of key= .get from url:https://stackoverflow.com/questions/39496096/understanding-dictionary-get-in-python
        winner=max(candidatevotes,key=candidatevotes.get) 
    print('----------')       
    print(f"Winner: {winner}")
    print('----------') 

# creating and writing text file called winners.txt
# Xpert Learning Assistant had me surround the with open with defining the results to not repeat the entire block of code
def writeresults(totalvotes, candidatevotes, winner):
    with open('winners.txt','w') as file:
        file.write("Election Results\n")
        file.write('----------\n')
        file.write(f'Total Votes: {totalvotes} \n')
        file.write('----------\n')
        for candidatename,votes in candidatevotes.items():
            percentage=(votes/totalvotes)*100
            file.write(f"{candidatename}: {percentage:.3f}% ({votes})\n")
        file.write('----------\n')       
        file.write(f"Winner: {winner}\n")
        file.write('----------') 
# call the functionto write the results to the file
writeresults(totalvotes, candidatevotes, winner)
