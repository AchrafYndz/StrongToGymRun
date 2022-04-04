import csv
import datetime
from exerciseNameConversion import nameConversion

strongList = []
gymRunList = []

with open("csv_input/myStrongData.csv", "r") as inputFile:
    myCsvFile = csv.reader(inputFile)
    for row in myCsvFile:
        strongList.append(row)

prevTimeObject = datetime.datetime.now()
for item in strongList:
    gymRunItem = []
    if item == strongList[0]:
        gymRunList.append(["Date", "Time", "Exercise", "Set", "Weight", "Reps", "Note"])
        continue

    ################### handling date and time ######################
    strongDateAndTime = item[0]
    dateAndTimeList = strongDateAndTime.split(" ")

    # convert date format
    date = dateAndTimeList[0]
    dateList = date.split("-")
    timeString = dateAndTimeList[1]
    timeObject = datetime.datetime(int(dateList[0]), int(dateList[1]), int(dateList[2]), int(timeString[:2]),
                                   int(timeString[3:5]), int(timeString[6:]))
    if 0 <= abs(prevTimeObject - timeObject).total_seconds() <= 86400:
        timeObject = prevTimeObject + datetime.timedelta(seconds=1)
    newDay = timeObject.strftime("%d.%m.%y")
    gymRunItem.append(newDay)
    prevTimeObject = timeObject

    newTime = timeObject.strftime("%H:%M:%S")
    gymRunItem.append(newTime)

    ################### handling exercise names #####################
    strongExerciseName = item[2]
    try:
        gymRunItem.append(nameConversion[strongExerciseName])
    except:
        print("Could not find translation entry for \"" + strongExerciseName + "\"")
        print("Please add an entry to the dictionary in exerciseNameConversion.py")

    ############### handling set orders #####################
    setOrder = item[3]
    gymRunItem.append(setOrder)

    ############## handling weight #############
    weight = item[4]
    bodyWeightExercises = ["Knee Raise (Captain's Chair)", "Plank", "Hanging Knee Raise", "Hanging Leg Raise"]
    if weight == "" and strongExerciseName not in bodyWeightExercises:
            gymRunItem.append("0")
    else:
        gymRunItem.append(weight)

    ########### handling reps #############
    reps = item[6]
    gymRunItem.append(reps)

    ########## handling notes ############
    notes = item[10]
    gymRunItem.append(notes)
    print(gymRunItem)
    gymRunList.append(gymRunItem)

with open("out.csv", "w") as outputFile:
    newCsvFile = csv.writer(outputFile, lineterminator='\n')
    for i in range(len(gymRunList)):
        newCsvFile.writerow(gymRunList[i])
