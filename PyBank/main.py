# import the os and csv
import os
import csv
 
 
 
# define the variables
total_of_months=0
net_amount_change=0
monthly_change_rate=[]
month_count_total=[]
greatest_increase=0
greatest_increase_month=0
greatest_decrease=0
greatest_decrease_month=0
 
 
 
# set a file for the path to print to
csvpath=os.path.join("Resources", "budget_data.csv")
 
 
 
 
#open + read the csv file 
with open(csvpath, newline='') as csvfile:
   
    csvreader=csv.reader(csvfile, delimiter=',')
   
 
 
    # header row read 
    csv_header=next(csvreader)
    row=next(csvreader)
 
 
    
    # calc # months, net amt p/l, row variables
    previous_row=int(row[1])
    total_of_months+=1
    net_amount_change+=int(row[1])
    greatest_increase=int(row[1])
    greatest_increase_month=row[0]
 
 
 
    for row in csvreader:
 
 
        
        # define num of months found in ds
        total_of_months+=1
        # define net amt of p/l in whole
        net_amount_change+=int(row[1])
 
 
 
        # calculate change from now to previous month
        revenue_change=int(row[1]) -previous_row
        monthly_change_rate.append(revenue_change)
        previous_row=int(row[1])
        month_count_total.append(row[0])
 
 
 
        
        #calc greatest inc
        if int(row[1]) >greatest_increase:
            greatest_increase=int(row[1])
            greatest_increase_month=row[0]
  
 
          
        #calc greatest dec
        if int(row[1]) <greatest_decrease:
            greatest_decrease=int(row[1])
            greatest_decrease_month=row[0]  
 
 
 
        
    # calc avg + date
    average_change=sum(monthly_change_rate)/len(monthly_change_rate)
    highest=max(monthly_change_rate)
    lowest=min(monthly_change_rate)
 
 
 
# print financial analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_of_months}")
print(f"Total: ${net_amount_change}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")
 
 
 
# file it needs to be written to
output_file=os.path.join("Resources", "budget_analysis.txt")
 
 
with open(output_file, 'w',) as txtfile:
 
 
#rewrite with new data in file
 
 
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_of_months}\n")
    txtfile.write(f"Total: ${net_amount_change}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")