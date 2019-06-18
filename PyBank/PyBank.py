# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources" , "budget_data.csv")

# Create lists to store data
month = []
profit_loss_table = []
NewPL = []
OldPL = []
amount_change = []
month_adjusted = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skips header

    # Loop through records and add months and profit/loss to individual lists
    for row in csvreader:
       month.append(row[0])
       profit_loss_table.append(int(row[1]))
    
    # Find the sum of the the profit/loss column
    total_amount = sum(profit_loss_table)

    # Create adjusted lists to later find the average change
    NewPL = profit_loss_table[1:]
    OldPL = profit_loss_table[:-1]
    
    # Find amount change of profit/loss using lists and list comprehensions:
    amount_change = [new - old for (new, old) in zip(NewPL, OldPL)]
 
    # Find average change by taking the sum of amount change divided by the # of values 
    avg_change = round((sum(amount_change) / len(amount_change)),2)
    
# Find greatest Profit and Loss Values
    # adjust month list to fit the amount_change list. It takes out the first value 
    # since the first month does not have a change.
    month_adjusted = month[1:]

    # find the highest profit and loss amount in amount_change list using max and index
    MaxIndex = amount_change.index(max(amount_change))
    MinIndex = amount_change.index(min(amount_change))

    MaxProfitMonth = month_adjusted[MaxIndex]
    MinProfitMonth = month_adjusted[MinIndex]
    MaxProfit = amount_change[MaxIndex]
    MinProfit = amount_change[MinIndex]

# print final hw
    print("----------------------------")
    print("Finacial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(month)))
    print("Total: " + "$" + format(total_amount, ","))
    print("Average Change: " + "$" + format(avg_change,',.2f'))
    print("Greatest Increase in Profits: " + MaxProfitMonth + " ($" + format(MaxProfit,',.2f') + ")")
    print("Greatest Decrease in Profits: " + MinProfitMonth + " ($" + format(MinProfit, ',.2f') + ")")
    print("----------------------------")

# print homework answers to text file
file = "PyBank_Report.txt"
with open(file,'w') as f:
    print("----------------------------",file=f)
    print("Finacial Analysis",file=f)
    print("----------------------------",file=f)
    print("Total Months: " + str(len(month)),file=f)
    print("Total: " + "$" + format(total_amount, ","),file=f)
    print("Average Change: " + "$" + format(avg_change,',.2f'),file=f)
    print("Greatest Increase in Profits: " + MaxProfitMonth + " ($" + format(MaxProfit,',.2f') + ")",file=f)
    print("Greatest Decrease in Profits: " + MinProfitMonth + " ($" + format(MinProfit, ',.2f') + ")",file=f)
    print("----------------------------",file=f)
    f.close()