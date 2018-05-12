# -*- coding: UTF-8 -*-
# Dependencies
import csv

# File Names
input_file1 = "raw_data/budget_data_1.csv"
output_file1 = "output/budget_analysis_1.txt"
input_file2 = "raw_data/budget_data_2.csv"
output_file2 = "output/budget_analysis_2.txt"

# parameters
total_months = 0
total_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the csv and convert it into a list of dictionaries
with open(input_file1) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        # Track the revenue change
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Average Revenue
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
fin_data = (
    f"\nFinancial Analysis\n"
    f"-----------------------------------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(fin_data)

# Export the results to text file
with open(output_file1, "w") as txt_file:
    txt_file.write(fin_data)
    txt_file.close()
