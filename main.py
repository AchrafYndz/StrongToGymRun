import csv
from exerciseNameConversion import nameConversion

strongList = []
gymRunList = []

with open("csv_input/myStrongData.csv", "r") as inputFile:
    myCsvFile = csv.reader(inputFile)
    for row in myCsvFile:
        strongList.append(row)

todo = 0
for item in strongList:
    gymrunItem = []
    if item == strongList[0]:
        continue

    ################### handling date and time ######################
    strongDateAndTime = item[0]
    dateAndTimeList = strongDateAndTime.split(" ")

    # convert date format
    date = dateAndTimeList[0]
    dateList = date.split("-")
    gymRunDate = dateList[2] + "." + dateList[1] + "." + dateList[0][2:]
    gymrunItem.append(gymRunDate)
    # append time data
    time = dateAndTimeList[1]
    gymrunItem.append(time)

    ################### handling exercise names #####################
    strongExerciseName = item[2]
    # print(strongExerciseName)
    try:
        gymrunItem.append(nameConversion[strongExerciseName])
    except:
        todo += 1
        print("Could not find translation entry for \"" + strongExerciseName + "\"")
        print("Please add an entry to the dictionary in exerciseNameConversion.py")

    # print(gymrunItem)

print(todo)
with open("out.csv", "w") as outputFile:
    newCsvFile = csv.writer(outputFile)
    for i in range(len(gymRunList)):
        newCsvFile.writerow([gymRunList])
