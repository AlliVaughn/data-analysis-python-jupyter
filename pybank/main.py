
# Loading the data
import os
import csv
# rounding
from decimal import Decimal
# for initialization of delta variables
import sys
(INT_MAX, INT_MIN) = (sys.maxsize, -sys.maxsize -1)

# changed this bc of the situation of the Resources folder in this case.  Add the second line if your structure demands it.   
csvpath = os.path.join('Resources', 'budget_data.csv')
# csvpath = os.path.join('../','Resources', 'budget_data.csv')

#open and read our csv file 
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the headers
    next(csvreader)
    #Arrays/Variables 
    months = []
    total_money = []
    delta_money = []
    #Initialize 
    smol_delta = INT_MAX
    big_delta = INT_MIN
    smol_delta_month = 0
    big_delta_month = 0
    
    # Read each row of data after the header
    for row in csvreader:

        #capture total number of months
        months.append(row[0])
        # capture total money 
        total_money.append(float(row[1]))
        #conditional checking if total_moneey has something in it 
        if len(total_money) > 1:
            #set the delta variable to skip back to accurately capture between months
            delta = (total_money[-1] - total_money[-2]) 
            #capture the delta 
            delta_money.append(delta) 
            #conditional
            # Is this the biggest delta yet seen?
            if delta >= big_delta: 
                big_delta = delta
                big_delta_month = months[-1]
            # Is the the smallest delta yet seen?      
            elif delta <= smol_delta:  
                smol_delta = delta
                smol_delta_month = months[-1]
                
    #print our analysis to terminal 
    print("Financial Analysis\n")
    print("------------------------\n")
    print(f'Total Months: {len(months)}\n')
    print(f'Total : (${str(round(Decimal(sum(total_money)), 2))})\n')
    print(f'Average Change: (${str(round(Decimal(sum(delta_money)/len(delta_money)), 2))})\n')
    print(f'Greatest Increase in profits: {big_delta_month} {big_delta}\n')
    print(f'Greatest Decrease in profits: {smol_delta_month} {smol_delta}\n')

# write data to a .txt a file. 
file1 = open("pybank.txt","w") 
file1.write("Financial Analysis\n")
file1.write("------------------------\n")
file1.write(f'Total Months: {len(months)}\n')
file1.write(f'Total : (${str(round(Decimal(sum(total_money)), 2))})\n')
file1.write(f'Average Change: (${str(round(Decimal(sum(delta_money)/len(delta_money)), 2))})\n')
file1.write(f'Greatest Increase in Profits: {big_delta_month} (${big_delta})\n')
file1.write(f'Greatest Decrease in Profits: {smol_delta_month} (${smol_delta})\n')

file1.close() #to change file access modes 
