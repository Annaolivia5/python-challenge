import os
import csv

# file to read from
budget_data_path = os.path.join('.', 'Resources', 'budget_data.csv')

# calculate the total_months, average_change, the find the months with great increase and decrease.
total_months = 0
total = 0
average_change = 0
greatest_inc_in_profits = 0
greatest_dec_in_profits = 0
greatest_inc_month = ""
greatest_dec_month = ""

# read each row of data
with open(budget_data_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # get the first row of data as starting point for calculations.
    first_row = next(csvreader)
    total_months += 1
    current_prof_loss = int(first_row[1])
    total += current_prof_loss
    total_change = 0 # use to calculate average change later

    greatest_inc_month = first_row[0]
    greatest_dec_month = first_row[0]

    # Loop through each of the other rows
    for row in csvreader:

        prof_loss = int(row[1])
        month = row[0]

        total_months += 1
        total = total + prof_loss
        total_change += (prof_loss - current_prof_loss)

        if (prof_loss - current_prof_loss) > greatest_inc_in_profits:

            greatest_inc_in_profits = (prof_loss - current_prof_loss)
            greatest_inc_month = month
        
        if (prof_loss - current_prof_loss) < greatest_dec_in_profits:

            greatest_dec_in_profits = (prof_loss - current_prof_loss)
            greatest_dec_month = month

        current_prof_loss = prof_loss

# calculate the average_change
average_change = total_change / (total_months -1)

# print the analysis
print(f"Total Month: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_in_profits})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_in_profits})")

#-----------------------------------------------------------------------------------------
# Export the analysis to a text file.

# Set variable for output file
output_file = os.path.join('.', 'analysis', 'PyBankAnalysis.txt')

#  Open the output file
with open(output_file, "w", newline="") as datafile:

    datafile.write("Financial Analysis\n----------------------------\n")
    datafile.write(f"Total Month: {total_months}\n")
    datafile.write(f"Total Month: ${total}\n")
    datafile.write(f"Average Change: ${round(average_change, 2)}\n")
    datafile.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_in_profits})\n")
    datafile.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_in_profits})")