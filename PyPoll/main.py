#import libraries
import csv
import os

#file location
file_to_read = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = []
candidates_votes ={}
candidates_percent ={}
winner_votes = 0

#open file as object
with open(file_to_read) as data_file:
    data = csv.reader(data_file)
    
    #read header
    header = next(data)

    #iterate through data
    for row in data:
        #count total votes and read candidate
        total_votes=total_votes+1
        candidate = str(row[2])

        #make a list of candidates
        if candidate not in candidates:
            candidates.append(row[2])
            candidates_votes[candidate] = 0
        
        #count cadidate votes and percentage
        candidates_votes[candidate] = candidates_votes[candidate] + 1
        candidates_percent[candidate] = candidates_votes[candidate]/total_votes*100

    #find out winner
    for candidate in candidates:
        if candidates_votes[candidate]>winner_votes:
            winner_votes = candidates_votes[candidate]
            winner = candidate
    
    #output file location
    output_file = os.path.join('analysis.txt')

    with open(output_file, "w") as file_text:

        #print details about total votes & write to file
        result_totalvotes = (
            f"\n\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")
        
        print(result_totalvotes)
        file_text.write(result_totalvotes)

        #print cadidates vote & write to file
        for candidate in candidates:
            result_candidate = (f"{candidate}: {candidates_percent[candidate]:.3f}%  ({candidates_votes[candidate]})\n")
            print(result_candidate)
            file_text.write(result_candidate)
        
        #print the winner & write to file
        result_winner = (    f"-------------------------\n"
            f"Winner: {winner}\n"
            f"-------------------------\n")
        print(result_winner)
        file_text.write(result_winner)