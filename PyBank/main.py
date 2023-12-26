#Intitalize variables
MonthCount = 0
TotalProfit = 0
CurrentChange = 0
TotalChange = 0
GreatestIncrease = 0
GreatestDecrease = 0

#Open data file for reading
DataFile = open("Resources/budget_data.csv", "r")

#Read the first line and move on to the actual data
CurrentLine = DataFile.readline()

#Loop through all data
while True:

    #Read the next line of data
    CurrentLine = DataFile.readline()

    #If there are no more lines, end the loop
    if not CurrentLine:
        break
    
    #if there is another line, add one to the month count
    MonthCount += 1

    #split the data using the commas
    LineData = CurrentLine.split(",")

    #pull current profit/loss and cast as integer
    CurrentValue = int(LineData[1])

    #add CurrentValue to previous values to get total profit/loss
    TotalProfit += CurrentValue

    #calculate change from last value, starting with second line of data
    if MonthCount > 1:
        CurrentChange = CurrentValue - LastValue
       
        #add to total change (used later to calculate average change)
        TotalChange += CurrentChange

    #if this is the largest increase to date, update GreatestIncrease
    if CurrentChange > GreatestIncrease:
        GreatestIncrease = CurrentChange
        GreatestIncreaseMonth = LineData[0]

    if CurrentChange < GreatestDecrease:
        GreatestDecrease = CurrentChange
        GreatestDecreaseMonth = LineData[0]

    #Initialize for next loop
    LastValue = CurrentValue

#end loop

#close the file
DataFile.close()

#calculate average change
AverageChange = TotalChange/(MonthCount-1)

#print results to Terminal
print("Financial Analysis")
print("----------------------------------")
print("Total Months: ", MonthCount)
print("Total Profit/Loss: $", TotalProfit)
print("Average Change: $", round(AverageChange,2))
print("Greatest Increase in Profits: ", GreatestIncreaseMonth, " ($", GreatestIncrease, ")")
print("Greatest Decrease in Profits: ", GreatestDecreaseMonth, " ($", GreatestDecrease, ")")

#create results file
ResultsFile = open("Analysis/results.txt", "w")
print("Financial Analysis", file=ResultsFile)
print("----------------------------------", file=ResultsFile)
print("Total Months: ", MonthCount, file=ResultsFile)
print("Total Profit/Loss: $", TotalProfit, file=ResultsFile)
print("Average Change: $", round(AverageChange,2), file=ResultsFile)
print("Greatest Increase in Profits: ", GreatestIncreaseMonth, " ($", GreatestIncrease, ")", file=ResultsFile)
print("Greatest Decrease in Profits: ", GreatestDecreaseMonth, " ($", GreatestDecrease, ")", file=ResultsFile)

#close results file
ResultsFile.close()