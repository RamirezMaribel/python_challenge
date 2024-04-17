import os
import csv
import statistics
budget=os.path.join('..','Resources','budget_data.csv')


with open(budget) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)

# rows of data without header line
    rows=[rows for rows in csvreader]
print("FINANCIAL ANALSYSIS")

#total sum of P/L column
totalpl=sum(int(row[1]) for row in rows)
totalmths=len(rows)
print(f'Total: ${totalpl}')
print(f'Total months:{totalmths}')
      
# average of P/L column
changes=[int(rows[i+1][1])- int(rows[i][1]) for i in range(len(rows)-1)]
avgchanges=statistics.mean(changes)
print(f'Average Change: ${avgchanges}')

# greatest increase in profits

maxchange=max(changes)
maxchangeindex=changes.index(max(changes))
maxchangerow=rows[maxchangeindex+1]
print(f'Greatest Increase in Profits:', maxchangerow[0], "$",maxchange)

# greatest decrease in profits
minchange=min(changes)
minchangeindex=changes.index(min(changes))
minchangerow=rows[minchangeindex+1]
print(f'Greatest Decrease in Profits:', minchangerow[0],"$",minchange)

with open("results.txt","w") as file:
    file.write
    file.write("FINANCIAL ANALSYSIS\n")
    file.write('----------\n')
    file.write(f"Total months: {len(rows)}\n")
    file.write(f'Total: ${totalpl}\n')
    file.write(f'Average Change: ${avgchanges}\n')
    file.write(f'Greatest Increase in Profits: {maxchangerow[0]} ${maxchange}\n')
    file.write(f'Greatest Decrease in Profits: {minchangerow[0]} ${minchange}\n')