# dependencies
import os
import csv

# create filepath 
pybank_analysis = os.path.join("//03-Python⁩/Homework⁩/⁨PyBank⁩/Resources⁩/budget_data.csv")

# using csv module, read CSV file
with open(pybank_analysis, "r", newline = " ") as csv:
    csvreader = csv.reader(csv, delimiter = ",")
    csv_header = next(csvreader)
   
    
# create variables needed for mathematical operations
total_months = 0
previous_month_revenue = 0
monthly_variances_list = []
month_list = []


    # 1. create a 'for loop' to read each row of data after the header
    # 2. update the tally for total_months
    # 3. update the tally for total_net_revenue


for row in csvreader:
    total_months += 1
    total_net_revenue += int(row[1])
        
        
        
        # Calculate Current Month Changes as long as the total months is greater than 1
        # 1. calculate the monthly change in revenue & append to monthly_variance_list
        # 2. change previous_month_rev to equal current_month_rev as needed for the next loop iteration

    if total_months > 1:
        monthly_variance = int(row[1]) - previous_month_revenue
        monthly_variances_list.append(monthly_variance)
        month_list.append(row[0])
        previous_month_revenue = int(row[1])


# Calculate Summary Variables
# 1. average change
# 2. identify max/min rev change & index location (greatest increase/decrease in revenue change)
# 3. identify the month of max/min & index location

avg_change = sum(monthly_variances_list) / len(monthly_variances_list)

max_month = monthly_variances_list.index(max(monthly_variances_list))
min_month = monthly_variances_list.index(min(monthly_variances_list))
greatest_increase = month_list[max_month]
greatest_decrease = month_list[min_month]


# Summary for Output

summary = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_net_revenue}\n"
    f"Average Revenue Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Revenue: {greatest_increase} (${max_month})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease} (${min_month})\n")
print(summary)


# 1.Create a text file to write output(summary)- using '+' sign (create file if doesn't exist)
# 2.Write summary to text file
# 3.Close output file

summary_output_txt = open("summary_pybank.txt", "w+")
summary_output_txt.write(summary)
summary_output_txt.close()