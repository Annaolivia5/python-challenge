import os
import csv

# file to read from
budget_data_path = os.path.join('.', 'Resources', 'budget_data.csv')

total_months = 0
total = 0
average_change = 0
greatest_inc_in_profits = 0
greatest_dec_in_profits = 0
greatest_inc_month = ""
greatest_dec_month = ""

# Read in the CSV file
with open(budget_data_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    first_row = next(csvreader)

    total_months += 1
    curr_prof_los = int(first_row[1])
    total += curr_prof_los
    total_change = 0
    

    # greatest_inc_in_profits = int(first_row[1])
    # greatest_dec_in_profits = int(first_row[1])
    greatest_inc_month = first_row[0]
    greatest_dec_month = first_row[0]

    # Loop through the data
    for row in csvreader:

        prof_loss = int(row[1])
        # print(row[0])
        # print(f"*******{prof_loss}")
        month = row[0]

        total_months += 1
        total = total + prof_loss
        total_change += (prof_loss - curr_prof_los)

        if (prof_loss - curr_prof_los) > greatest_inc_in_profits:

            # print(f"/////////////////inc: {row[0]}")
            greatest_inc_in_profits = (prof_loss - curr_prof_los)
            greatest_inc_month = month
        
        if (prof_loss - curr_prof_los) < greatest_dec_in_profits:

            # print(f"/////////////////dec: {row[0]}")
            greatest_dec_in_profits = (prof_loss - curr_prof_los)
            greatest_dec_month = month

        curr_prof_los = prof_loss


average_change = total_change / (total_months -1)

print(f"Total Month: {total_months}")
print(f"Total Month: ${total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_in_profits})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_in_profits})")
