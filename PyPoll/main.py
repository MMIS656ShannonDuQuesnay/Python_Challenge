import os

# Module for reading CSV files
import csv

election_data = os.path.join('Desktop', 'Python_Challenge', 'PyPoll', 'Resources', 'election_data.csv')


candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline="") as csvfile:
    reader = csv.reader(csvfile)
    header = next(csvfile)
    #first_row = next(reader)
    #print(header)


    for row in reader:
        total_votes+=1    
        #print(max(int(total_votes)))

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1


    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    #winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")


for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


# Exporting to .txt file

# Specify File To Write To
output_file = os.path.join('Desktop', 'Python_Challenge', 'PyPoll', 'Analysis', 'election_data.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------------------\n")
    for i in range(len(candidates)):
        txtfile.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    txtfile.write(f"------------------------------------\n")
    txtfile.write(f"Winner: ${winning_candidate}\n")
    txtfile.write(f"------------------------------------\n")