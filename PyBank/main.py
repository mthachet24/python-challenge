import os 
import csv 

budget_csv = os.path.join("Resources", "budget_data.csv")

budget_csv_output = os.path.join("analysis", "budget_analysis.txt")


# Read the csv and convert it into a list of dictionaries


total_months = 0

months_of_change = 0

net_change_list = []

totalprofit_losses = 0

previousprofit_losses = 0

profit_losses_change = 0

profitloss_change_list = []

greatest_increase = 0 

greatest_decrease = 0

greatest_increase_month = 0

greatest_decrease_month = 0

total_net = 0


with open(budget_csv) as budget:
        budget_reader = csv.reader(budget)





# Read the header row


with open(budget_csv) as budget_data:
    reader = csv.reader(budget_data)
    next(reader)
# Extract first row to avoid appending to net_change_list than inside the for loop


    index = 0
    for row in reader:
        previous_row = int(row[1])
        total_months+=1
        totalprofit_losses = totalprofit_losses + int(row[1]) - previousprofit_losses
        months_of_change = months_of_change + 1 
        greatest_increase = int(row[1])
        greatest_increase_month = row[0]

       
    # Calculate the greatest increase 
        if int(row[1]) > greatest_increase: 
            greatest_increase = int(row[1])
            greatest_increase_month = [0]
    



# Calculate the greatest decrease

        if int(row[1]) < greatest_decrease: 
            greatest_decrease = int(row[1])
            greatest_decrease_month = [0]

 





# Track the total


total_months = total_months + 1


# Track the net change




# Calculate the greatest decrease 

print(totalprofit_losses)
greatest_decrease = min(totalprofit_losses)



# Calculate the greatest increase


greatest_increase = max(profitloss_change_list)



# add 1 for the month 
greatest_decrease_month = profitloss_change_list.index(greatest_decrease) + 1
greatest_increase_month = profitloss_change_list.index(greatest_increase) + 1



# calculate average and date

average_change = sum(months_of_change)/len(months_of_change)


highest = max(months_of_change)
lowest = min(months_of_change)


# Generate Output Summary


print("Financial Analysis")

print("----------------------------------")

print(f"Total Months: {total_months}\n")

print(f"Total Profit/Losses: ${totalprofit_losses}\n")

print(f"Average Change: ${round(sum(profitloss_change_list)/len(profitloss_change_list),2)}")

print(f"Greatest increase in Profits: {months_of_change[greatest_increase_month]} (${(str(greatest_increase))})")

print(f"Greatest decrease in Profits: {months_of_change[greatest_decrease_month]} (${(str(greatest_decrease))})")




with open ("budget_analysis.txt", "w") as txt_file:
    Financial_analysis = (
        f"election results\n"
        f"----------------------\n"
        f"total months: {total_months}\n"
        f"Total Profit/Losses: ${totalprofit_losses}\n"
        f"Average Change: ${round(sum(profitloss_change_list)/len(profitloss_change_list),2)}\n"
        f"Greatest increase in Profits: {months_of_change[greatest_increase_month]} (${(str(greatest_increase))})\n"
        f"Greatest decrease in Profits: {months_of_change[greatest_decrease_month]} (${(str(greatest_decrease))})\n")

    print(Financial_analysis, end="")

    txt_file.write(Financial_analysis)







# ALL OF THE STEPS TO COMPLETE: 

# Read the csv and convert it into a list of dictionaries
# Read the header row
# Extract first row to avoid appending to net_change_list than inside the for loop
# Track the total
# Track the net change
# Calculate the greatest decrease
# Calculate the greatest increase
# Calculate the Average Net Change
# Generate Output Summary
# Print the output (to terminal)
# Export the results to text file