# The data we need to retrieve
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each cadidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file to write a data
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create list for candidate options
candidate_options = []

# Create dictionary for candidate votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader funtion
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add the candiate name to the candidate list.
            candidate_options.append(candidate_name)
            
            # Begin candidate's vote count
            candidate_votes[candidate_name] = 0
                
        # Add vote to candidate's vote count
        candidate_votes[candidate_name] += 1
    
# Save the results to text file
with open(file_to_save, "w") as txt_file:
        
    # Print the final count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percendate of votes for each candidate by loopint through the counts

    # Iterate through candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100
        
        # Calculate candidate's results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print the candidate name and percentage of votes to the terminal
        print(candidate_results)

        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determine if the votes greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print the winning candidate's results to the terminal. 
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file. 
    txt_file.write(winning_candidate_summary)