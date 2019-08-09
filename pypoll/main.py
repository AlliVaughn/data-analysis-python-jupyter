
import os
import csv
# changed this bc of the situation of the Resources folder in this case. Add the second line if your structure demands it.   
csvpath = os.path.join('Resources', 'election_data.csv')
# csvpath = os.path.join('../','Resources', 'election_data.csv')

# Make a dict of the election data
elect_dict = {}

# initialize votes
votes = 0 
    
# open and read our csv file using a comma delimiter
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip headers
    next(csvreader)
    
    #loop over our data
    for row in csvreader:  
        #add up votes
        votes += 1

        #determine of chosen name is in set of valid names
        if row[2] in elect_dict.keys():
            # the row we are on  is the row + 1
            elect_dict[row[2]] = elect_dict[row[2]] + 1
        else:
            #otherwise 
            elect_dict[row[2]] = 1 

        
# create arrays for candidates and their vote counts
candidates = []
votes_per_candidate = []

# takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and votes_per_candidate
for key, value in elect_dict.items():
    candidates.append(key)
    votes_per_candidate.append(value)

# create vote percent array 
vote_percent = []

for v in votes_per_candidate:
    vote_percent.append(round(v/votes*100, 1))
    

# zips candidates, votes_per_candidate, vote_percent 
# I also iterate over the zip_results below to print as well. 
zip_results = list(zip(candidates, votes_per_candidate, vote_percent))
    
# Winner array 
election_winner = []

#iterate over zip_results 
for name in zip_results:
    # eveluates if the max votes_per_candidate equals the name 
    if max(votes_per_candidate) == name[1]:
        #IF IT DOES, append that name to the  0 position of election_winner ( first in the  array)
        election_winner.append(name[0])

# Here's the top winner 
winner = election_winner[0]


# Print the results to terminal 
print("-------------------------")
print(f'Total Votes: {votes}')
print("-------------------------")      
print("Name | Votes | Percentage ")
print("-------------------------") 
for index in range(len(zip_results)):
    print(f'{candidates[index]} : ({votes_per_candidate[index]}) {vote_percent[index]}%')
print("-------------------------")     
print(f'Winner: {winner}') 
print("-------------------------")     

# there must be a more Elegant way to do this, but this was the best I I could do. :P  
# print results to a txt file 
file1 = open("pypoll.txt","w") 
file1.write("Election Results\n")
file1.write("------------------------\n")
file1.write(f'Total Votes: {votes}\n')
file1.write("------------------------\n")
for index in range(len(zip_results)):
    file1.write(f'{candidates[index]} : ({votes_per_candidate[index]}) {vote_percent[index]}% \n')
file1.write("------------------------\n")    
file1.write(f'Winner: {winner}\n') 
file1.write("------------------------\n")
file1.close() # to change file access modes 



