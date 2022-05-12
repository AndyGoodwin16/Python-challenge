import os
import csv

input_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis", "pypoll.txt")
    
with open(input_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_votes = 0
    candidates_list = []
    for row in csvreader:
        total_votes += 1
        candidates_list.append(row[2])
    
    unique_candidates_list = []
    unique_candidates_votes = []
    for candidate in candidates_list:
        if candidate not in unique_candidates_list:
            unique_candidates_list.append(candidate)
        
    for candidate in unique_candidates_list:    
        unique_candidates_votes.append(candidates_list.count(candidate))

    winner = unique_candidates_list[unique_candidates_votes.index(max(unique_candidates_votes))]

    print(f"Election Results \n")
    print(f"---------------------------- \n")
    print(f"Total Votes: {total_votes} \n")
    print(f"------------------------- \n")
    for i in range(len(unique_candidates_list)):
        print(f"{unique_candidates_list[i]}: {(unique_candidates_votes[i]/total_votes)*100:.3f}% ({unique_candidates_votes[i]}) \n")
    print(f"------------------------- \n")
    print(f"Winner: {winner} \n")
    print(f"------------------------- \n")

with open(output_path, 'w') as txt:
    txt.write(f"Election Results \n")
    txt.write(f"---------------------------- \n")
    txt.write(f"Total Votes: {total_votes} \n")
    txt.write(f"------------------------- \n")
    for i in range(len(unique_candidates_list)):
        txt.write(f"{unique_candidates_list[i]}: {(unique_candidates_votes[i]/total_votes)*100:.3f}% ({unique_candidates_votes[i]}) \n")
    txt.write(f"------------------------- \n")
    txt.write(f"Winner: {winner} \n")
    txt.write(f"------------------------- \n")