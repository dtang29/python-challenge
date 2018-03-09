def generate_report(csv, filename):

    #Define variable votes
    votes = 0

    #Create a list to hold the candidates
    candidates = []

    #Define a dictionary to hold the candidates and their votes
    candidate_votes = {}

    #Read in csv file 
    import os
    csvpath = os.path.join('raw_data', csv)
    output_path = os.path.join('raw_data', filename)

    import csv
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip the first row
        next(csvreader, None)
        

        for row in csvreader:
            
            #Keep track of the number of votes
            votes = votes + 1

            #check if candidate exists in list, if not add him to the list and dictionary with vote initialized to 1
            if row[2] in candidates:
                candidate_votes[row[2]] = candidate_votes[row[2]] + 1
            else:
                candidates.append(row[2])
                candidate_votes[row[2]] = 1

        print("Election Results")
        print("--------------------------------")
        print("Total Votes: " + str(votes))
        print("--------------------------------")
        for candidate in candidates:
            print(candidate + ": " + "{0:.0f}%".format(candidate_votes[candidate] / votes * 100) + " (" + str(candidate_votes[candidate]) + ")")
        print("--------------------------------")
        print("Winner: " + max(candidate_votes, key=candidate_votes.get))
        print("--------------------------------")
        print("Your results have been exported to a new text file named " + filename + "! \n")

        #write the results to a new txt file
        with open(output_path, 'w', newline='') as newfile:

            #initialize csv writer
            csvwriter = csv.writer(newfile, delimiter=',')

            csvwriter.writerow(["Election Results"])
            csvwriter.writerow(["--------------------------------"])
            csvwriter.writerow(["Total Votes: " + str(votes)])
            csvwriter.writerow(["--------------------------------"])
            for candidate in candidates:
                csvwriter.writerow([candidate + ": " + "{0:.0f}%".format(candidate_votes[candidate] / votes * 100) + " (" + str(candidate_votes[candidate]) + ")"])
            csvwriter.writerow(["--------------------------------"])
            csvwriter.writerow(["Winner: " + max(candidate_votes, key=candidate_votes.get)])
            csvwriter.writerow(["--------------------------------"])

#generate the report for the 2 raw files
generate_report('election_data_1.csv', 'election_results_1.csv')
generate_report('election_data_2.csv', 'election_results_2.csv')
