# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
months = []
monthly_changes = []


# Add more variables to track other necessary financial data
highest_increase = {"month": "", "change":0}
highest_decrease = {"month": "", "change":float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    first_row = next(reader)

    # Extract first row to avoid appending to net_change_list
    total_months += 1
    

    # Track the total and net change
    total_net += int(first_row[1])
    previous_value = int(first_row[1])

    # Process each row of data
    for row in reader:
        total_months += 1
        current_value = int(row[1])
        total_net += current_value

        # Track the total
        monthly_change = current_value - previous_value
        previous_value = current_value

        # Track the net change
        months.append(row[0])
        monthly_changes.append(monthly_change)

        # Calculate the greatest increase in profits (month and amount)
        if monthly_change > highest_increase["change"]:
            highest_increase["month"] = row[0]
            highest_increase["change"] = monthly_change

        # Calculate the greatest decrease in losses (month and amount)
        if monthly_change < highest_decrease["change"]:
            highest_decrease["month"] = row[0]
            highest_decrease["change"] = monthly_change


# Calculate the average net change across the months
average_change = sum(monthly_changes) / len(monthly_changes)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change: .2f}\n"
    f"Greatest Increase in Profits: {highest_increase['month']} (${highest_increase['change']})\n"
    f"Greatest Decrease in Profits: {highest_decrease['month']} (${highest_decrease['change']})\n"
          )

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
