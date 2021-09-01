import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the csv file and print the data
    file_reader = csv.reader(election_data)

    # Print each row of data from the csv file
    for row in file_reader:
        print(row)





#####
# Create a new file and filename variable for the path to the new file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# use the with command and open() function and "w" write to write data to the new file
with open(file_to_save, "w") as txt_file:

    #write data to the file
    txt_file.write("Test 1, test 2...")    

    txt_file.write("Arapahoe\nDenver\nJefferson")

