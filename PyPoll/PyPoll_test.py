# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources" , "election_data.csv")

# Create lists to store data
voter_id = []
county = []
candidate_list = []
KhanList = []
TestList = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate_list.append(row[2])
    
    unique_candidate_lists = list(dict.fromkeys(candidate_list))
    
    uniquecounter = 0
    for value in unique_candidate_lists:
        # set counter to change the list appending unique candidates
        for vote in candidate_list:
            if value == vote:
                uniquecounter += 1
                #TestList{counter}.append(vote)
                #{"value1": ["khan","khan","khan"]
                #"value2": ["correy", ]}
        TestList.append(uniquecounter)
        uniquecounter = 0
    print(TestList)

    totalvoters = len(voter_id)

    print(int(TestList) / totalvoters)



                


    #print(str(len(KhanList)))
        
        #for candidate in unique_candidate_lists:
