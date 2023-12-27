#initialize variables
VoteCount = 0
CandidateVotes = {}
WinningPercent = 0
CandidatePercents = {}

#Open data file for reading
DataFile = open("Resources/election_data.csv", "r")

#Read the first line and move on to the actual data
CurrentLine = DataFile.readline()

#Open loop
while True:

    #read next line
    CurrentLine = DataFile.readline()

    #If there are no more lines, end the loop
    if not CurrentLine:
        break

    #if there is a line, add one to the vote count
    VoteCount += 1

    #split the data using the commas
    LineData = CurrentLine.split(",")
    
    #label data and remove nextline from candidate name
    VoterID = LineData[0]
    County = LineData[1]
    Candidate = LineData[2].strip()

    # Create a dictionary with politician name and their vote count
    if Candidate in CandidateVotes:
        CandidateVotes[Candidate] += 1
    else:
        CandidateVotes[Candidate] = 1

#end while loop
        
#close the data file
DataFile.close()

#loop through candidates using for loop to get percentages
for Candidate in CandidateVotes:
    CandidatePercents[Candidate] = CandidateVotes[Candidate]/VoteCount * 100

    #Determine winner by who has the most votes
    if CandidatePercents[Candidate] > WinningPercent:
        WinningPercent = CandidatePercents[Candidate]
        WinningCandidate = Candidate

#end for loop

#Print results to terminal
print("Election Results")
print("-------------------------------")
print("Total Votes: ", VoteCount)
print("-------------------------------")

#use a for loop to print candidate votes and percentages
for Candidate in CandidateVotes:
    print(Candidate, ": ", round(CandidatePercents[Candidate], 2), "% (", CandidateVotes[Candidate], ")")
print("-------------------------------")

#print winner
print("Winner: ", WinningCandidate)
print("-------------------------------")

#Export a text file with results
ResultsFile = open("Analysis/results.txt", "w")
print("Election Results", file=ResultsFile)
print("-------------------------------", file=ResultsFile)
print("Total Votes: ", VoteCount, file=ResultsFile)
print("-------------------------------", file=ResultsFile)
for Candidate in CandidateVotes:
    print(Candidate, ": ", round(CandidatePercents[Candidate], 2), "% (", CandidateVotes[Candidate], ")", file=ResultsFile)
print("-------------------------------", file=ResultsFile)
print("Winner: ", WinningCandidate, file=ResultsFile)
print("-------------------------------", file=ResultsFile)

#close results file
ResultsFile.close()