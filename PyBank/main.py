#import libraries
import os
import csv

#check the current directory and files
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))

#file location
file_to_read = os.path.join('Resources','budget_data.csv')

#variable declarations
month_count = 0
total_pl = 0
pl_change = 0
pl_change_no = 0
max_pl_change = 0
min_pl_change = 0
prev_pl = 0
pl_change_total = 0

#open the file and store it as an object
with open(file_to_read) as data_file:
    data = csv.reader(data_file)

    #read the header
    header = next (data)

    #first row since there is no need to calculate p/l change, we do this outside the loop
    firstrow = next(data)
    month_count = month_count +1
    total_pl = total_pl + int(firstrow[1])
    prev_pl = int(firstrow[1])

    #loop from second row till the end
    for row in data:
        
        #count months and total ammounts
        month_count = month_count +1
        total_pl = total_pl + int(row[1])
        
        #keep a count of p/l change and not count if there is no change
        if int(row[1]) == prev_pl:
            pl_change_no = pl_change_no
        else:
            pl_change_no = pl_change_no +1
        
        #calculate p/l change and total change
        pl_change = int(row[1]) - prev_pl
        prev_pl = int(row[1])
        pl_change_total = pl_change_total + pl_change
        
        #find max increase of pl and its month
        if pl_change>max_pl_change:
            max_pl_change=pl_change
            max_inc_month=str(row[0])
        #find max decrease of pl and its month
        if pl_change<min_pl_change:
            min_pl_change=pl_change
            max_dec_month=str(row[0])
#calculate avg pl change
avg_pl_change = pl_change_total / pl_change_no

result = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total_pl}\n"
    f"Average  Change: ${avg_pl_change:.2f}\n"
    f"Greatest Increase in Profits: {max_inc_month} (${max_pl_change})\n"
    f"Greatest Decrease in Profits: {max_dec_month} (${min_pl_change})\n")

#print output
print(result)

#output to analysis.txt
output_file = os.path.join('analysis.txt')

with open(output_file, "w") as file_text:
    file_text.write(result)

