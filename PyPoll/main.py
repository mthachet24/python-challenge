# import all modules/dependencies
import os
import csv
 
##
 
# list all variables present in code
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
 
##
 
# set the path for file
csvpath = os.path.join("Resources", "election_data.csv")
 
##
 
# open & read the CSV File needed for code
with open(csvpath, newline='') as csvfile:
 
 
##
 
 
    # csv reader inserted
#this reader also  specifies the delimiter as well as variable which  holds all contents
    csvreader=csv.reader(csvfile, delimiter=',')
   
##
 
    # read container with header 
    csv_header = next(csvfile)
 
##
 
    # read all rows of data after header
    for row in csvreader:
        
##
 
        # calculate the total number of votes casted by
        total_votes+=1
 
 
##
        
        # calculate the total number of votes that  every candidate has won
        if(row[2] =="Khan"):
            khan_votes+=1
        elif(row[2] =="Correy"):
            correy_votes+=1
        elif(row[2] =="Li"):
            li_votes+=1
        else:
            otooley_votes+=1
   
##
 
         
    # this code calculates percentagage of votes each candidate has won
    kahn_percent=khan_votes/total_votes
    correy_percent=correy_votes/total_votes
    li_percent=li_votes/total_votes
    otooley_percent=otooley_votes/total_votes
    
##
 
 
    # calculate the winner of the election based on the popular vote of candidacy
    winner=max(khan_votes, correy_votes, li_votes, otooley_votes)
 
    if winner==khan_votes:
        winner_name="Khan"
    elif winner==correy_votes:
        winner_name="Correy"
    elif winner==li_votes:
        winner_name="Li"
    else:
        winner_name="O'Tooley"
 
 
##
 
# print the analysis of the results
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")
 
##
 
# specify the file to which the code will be printed
output_file=os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')
 
##
 
 
# open file and specify the variable to hold the contents
with open(output_file, 'w',) as txtfile:
 
 
##
 
 
# rewrite the new data 
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")