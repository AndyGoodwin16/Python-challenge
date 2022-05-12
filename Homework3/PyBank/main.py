import os
import csv

input_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Analysis", "pybank.txt")

with open(input_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    months_list = []
    net_list = []
    change_list = [0]
    for row in csvreader: 
        months_list.append(row[0])
        net_list.append(int(row[1]))
          
    for i in range(len(net_list)-1):
        change_list.append(int(net_list[i+1]) - int(net_list[i]))
    
    total_months = len(months_list)
    net = sum(net_list)
    average_change = sum(change_list[1:])/len(change_list[1:])
    
    date_max_increase = ''
    date_max_decrease = ''
    max_increase = 0
    max_decrease = 0
    for i in range(len(change_list)-1):
        if change_list[i+1] > change_list[i] and change_list[i+1] > max_increase:
            max_increase = change_list[i+1]
            date_max_increase = months_list[i+1]
        elif change_list[i+1] < change_list[i] and change_list[i+1] < max_decrease:
            max_decrease = change_list[i+1]
            date_max_decrease = months_list[i+1]

output = (
    f"Financial Analysis \n"
    f"---------------------------- \n"
    f"Total Months: {total_months} \n"
    f"Total: ${net} \n"
    f"Average Change: ${average_change:.2f} \n"
    f"Greatest Increase in Profits: {date_max_increase} (${max_increase}) \n"
    f"Greatest Decrease in Profits: {date_max_decrease} (${max_decrease}) \n"
    )

print(output)

with open(output_path, 'w') as txt_file:
    txt_file.write(output)