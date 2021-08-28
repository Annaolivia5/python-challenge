import os
import csv

# File to read from
election_data_path = os.path.join('.', 'Resources', 'election_data.csv')

# Calculate the Following
total_votes_cast = 0
candidates = {}
winner = ""
winner_vote_count = 0

# read each row of data
with open(election_data_path, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for candidate in csvreader:

        total_votes_cast += 1

        candidate_name = candidate[2]
        
        # add candidate and their total votes to the dictionary
        if(candidate_name in candidates):
            candidates[candidate_name] = (candidates[candidate_name] + 1)             
        else:
            candidates[candidate_name] = 1     


for candidate in candidates:

    # check to see if candidate is winning
    if(candidates[candidate] > winner_vote_count):
        winner_vote_count = candidates[candidate] 
        winner = candidate

    # calculate the % of votes for each candidate and update the dictionary with the percentages 
    candidates[candidate] = [candidates[candidate]/total_votes_cast, candidates[candidate]]

print(candidates)

#-----------------------------------------------------------------------------------------
# print the analysis
print("\nElection Results\n-------------------------")
print(f"Total Votes: {total_votes_cast}")
print("-------------------------")

for candidate in candidates:
    percentage_won = round((candidates[candidate][0] * 100),3)
    votes = candidates[candidate][1]
    print(f"{candidate}: {percentage_won}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#-----------------------------------------------------------------------------------------
# Export the analysis to a text file.

# Set variable for output file
output_file = os.path.join('.', 'analysis', 'PyPollAnalysis.txt')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    
    datafile.write("Election Results\n-------------------------\n")
    datafile.write(f"Total Votes: {total_votes_cast}\n")
    datafile.write("-------------------------\n")

    for candidate in candidates:
        percentage_won = round((candidates[candidate][0] * 100),3)
        votes = candidates[candidate][1]
        datafile.write(f"{candidate}: {percentage_won}% ({votes})\n")
 
    datafile.write("-------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("-------------------------")
    

 