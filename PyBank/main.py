# Import Modules/Dependencies
import os
import csv

# Variables
total_months = 0
total_profits = 0
monthly_change = []
month_count = []
largest_increase = 0
largest_increase_month = 0
largest_decrease = 0
largest_decrease_month = 0

# Set Path For File
budget_data = os.path.join( 'Desktop', 'Python_Challenge', 'PyBank', 'Resources', 'budget_data.csv')

# Open & Read CSV File
with open(budget_data, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    header = next(csvreader)
    row = next(csvreader)
    
    # Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows
    previous_row = int(row[1])
    total_months += 1
    total_profits += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Months Included In Dataset
        total_months += 1
        #Profit/Losses
        total_profits += int(row[1])

        # Calculate Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > largest_increase:
            largest_increase = int(row[1])
            largest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < largest_decrease:
            largest_decrease = int(row[1])
            largest_decrease_month = row[0]  
        
    # Calculate The Average & The Date
    average_change = average_change = sum(monthly_change)/ (len(monthly_change))
    
    largest_increase = max(monthly_change)
    largest_decrease = min(monthly_change)

#print(len(monthly_change))
#print(sum(monthly_change))

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {largest_increase_month}, (${largest_increase})")
print(f"Greatest Decrease in Profits: {largest_decrease_month}, (${largest_decrease})")

# Specify File To Write To
output_file = os.path.join('Desktop', 'Python_Challenge', 'PyBank', 'Analysis', 'budget_data.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"------------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profits}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {largest_increase_month}, (${largest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {largest_decrease_month}, (${largest_decrease})\n")