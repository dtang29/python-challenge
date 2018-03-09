def generate_report(csv, filename):

    #Define variable to hold in months, revenue, previous revenue
    months = 0
    revenue = 0
    previous_rev = 0

    #Define list to hold revenue change month over month 
    revenue_change = []

    #Define a separate list to hold all the dates. Use it to reference the index of greatest/lowest revenue change later
    dates = []

    #Read in csv file 
    import os
    csvpath = os.path.join('raw_data', csv)
    output_path = os.path.join('raw_data', filename)

    import csv
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip the first row
        next(csvreader, None)
        

        for row in csvreader:
            
            #Keep track of the number of months in dataset
            months = months + 1

            #calculate the difference in revenue
            diff_revenue = int(row[1]) - previous_rev

            #add the date followed by revenue difference to the list
            dates.append(row[0])
            revenue_change.append(diff_revenue)

            #update total revenue 
            revenue = revenue + int(row[1])

            #record the previous revenue
            previous_rev = int(row[1])


        #remove the first from revenue_change and dates since first revenue is not a change in revenue
        revenue_change.pop(0)
        dates.pop(0)

        index_max = revenue_change.index(max(revenue_change))
        index_min = revenue_change.index(min(revenue_change))

        print("Financial Analysis")
        print("--------------------------------")
        print("Total Months: " + str(months))
        print("Total Revenue: $" + str(revenue))
        print("Average Revenue Change: $" + "{0:.2f}".format(sum(revenue_change) / (months - 1) ))
        print("Greatest Increase in Revenue: " + dates[index_max] + " ($" + str(max(revenue_change)) + ")")
        print("Greatest Decrease in Revenue: " + dates[index_min] + " ($" + str(min(revenue_change)) + ")")
        print("Your results have been exported to a new text file named " + filename + "! \n")

        #write the results to a new txt file
        with open(output_path, 'w', newline='') as newfile:

            #initialize csv writer
            csvwriter = csv.writer(newfile, delimiter=',')

            csvwriter.writerow(["Financial Analysis"])
            csvwriter.writerow(["--------------------------------"])
            csvwriter.writerow(["Total Months: " + str(months)])
            csvwriter.writerow(["Total Revenue: $" + str(revenue)])
            csvwriter.writerow(["Average Revenue Change: $" + "{0:.2f}".format(sum(revenue_change) / (months - 1) )])
            csvwriter.writerow(["Greatest Increase in Revenue: " + dates[index_max] + " ($" + str(max(revenue_change)) + ")"])
            csvwriter.writerow(["Greatest Decrease in Revenue: " + dates[index_min] + " ($" + str(min(revenue_change)) + ")"])

#generate the report for the 2 raw files
generate_report('budget_data_1.csv', 'financial_analysis_1.csv')
generate_report('budget_data_2.csv', 'financial_analysis_2.csv')
