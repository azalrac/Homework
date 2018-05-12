# -*- coding: UTF-8 -*-
# Dependencies
import csv

# File Names
input_file1 = "election_data_1.csv"
output_file1 = "output/election_results_1.txt"
input_file2 = "election_data_2.csv"
output_file2 = "output/election_results_2.txt"

# parameters
total_votes_cast = 0
candidates_list = []
candidate_votes = {}
perc_votes = 0
total_votes_won = 0

#winners
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(input_file2) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        # Track the total
        total_votes_cast = total_votes_cast + 1

        # Grab canidates name
        candidate_name = row["Candidate"]

        #If statement
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)

            #count votes for each candidate
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count - this is outside the IF
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(output_file2, "w") as txt_file: 
# Summary
    election_results = (
    f"\n\nElection Results\n"
    f"-----------------------------------------------------------------------------\n"
    f"Total Votes: {total_votes_cast}\n"
    f"-----------------------------------------------------------------------------\n")
    # Print the output (to terminal)
    print(election_results)
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_perc = float(votes) / float(total_votes_cast) * 100

        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate_name

        voter_output = f"{candidate_name}: {vote_perc:.3f}% ({votes})\n"
        txt_file.write(voter_output)

          
        print(voter_output)
        
#winner prints to screen but not output file - I give up

    


winning_candidate_summary = (
        f"-----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------------------\n")

# Export the results to text file


print(winning_candidate_summary)
txt_file.write(winning_candidate_summary)




   




    

