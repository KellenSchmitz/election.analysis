import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")



##### All starting varibales #####
# Initialize a total vote counter variable
total_votes = 0

# create new list to count unique names in column 3 of the data
candidate_options=[]

# create a new dictionary to count up each candidate's votes
candidate_votes={}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    next(file_reader) # this just skips the first row in csv file

    # Count each row of data from the csv file
    for row in file_reader:
        total_votes +=1

        # The candidate name from each row is in column 3 (index 2)
        candidate_name = row[2]

        if candidate_name not in candidate_options: 
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # initialize candidate_votes variable to start at zero
            candidate_votes[candidate_name] = 0

        # count each vote per candidate
        candidate_votes[candidate_name] += 1

    ### Calculate the % of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name} with {vote_percentage:.2f}% of the vote and a total of {votes:,} votes.\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f" ---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count}\n"
        f"Winning percentage: {winning_percentage:.2f}%\n"
        f"----------------------------------\n"
        )
    print(winning_candidate_summary)






# Print the results
    # print(total_votes)
    # print(candidate_options)
    # print(candidate_votes)
