import csv
import datetime

from static import name_conversion, bodyweight_exercises

SECONDS_IN_A_DAY = 86400


def strong_to_gymrun():
    strong_list = []
    gymrun_list = []

    unknown_exercises = []

    with open("csv_input/input.csv", "r") as inputFile:
        my_csv_file = csv.reader(inputFile, delimiter=';')
        for row in my_csv_file:
            strong_list.append(row)

    prev_time_object = datetime.datetime.now()
    for i, item in enumerate(strong_list):
        gymrun_item = []

        if i == 0:
            gymrun_list.append(["Date", "Time", "Exercise", "Set", "Weight", "Reps", "Note"])
            continue

        # handling date and time
        strong_date_and_time = item[0]
        date_and_time_list = strong_date_and_time.split(" ")

        # convert date format
        date = date_and_time_list[0]
        date_list = date.split("-")
        time_string = date_and_time_list[1]
        time_object = datetime.datetime(
            int(date_list[0]),
            int(date_list[1]),
            int(date_list[2]),
            int(time_string[:2]),
            int(time_string[3:5]),
            int(time_string[6:])
        )

        if 0 <= abs(prev_time_object - time_object).total_seconds() <= SECONDS_IN_A_DAY:
            time_object = prev_time_object + datetime.timedelta(seconds=1)

        new_day = time_object.strftime("%d.%m.%y")
        gymrun_item.append(new_day)
        prev_time_object = time_object

        new_time = time_object.strftime("%H:%M:%S")
        gymrun_item.append(new_time)

        # handling exercise names
        strong_exercise_name = item[2]
        try:
            gymrun_item.append(name_conversion[strong_exercise_name])
        except KeyError:
            if strong_exercise_name not in unknown_exercises:
                unknown_exercises.append(strong_exercise_name)
                print("Could not find translation entry for \"" + strong_exercise_name + "\"")

        # handling set orders
        set_order = item[3]
        gymrun_item.append(set_order)

        # handling weight
        weight = item[4]
        if weight == "" and strong_exercise_name not in bodyweight_exercises:
            gymrun_item.append("0")
        else:
            gymrun_item.append(weight)

        # handling reps
        reps = item[6]
        gymrun_item.append(reps)

        # handling notes
        notes = item[10]
        gymrun_item.append(notes)
        gymrun_list.append(gymrun_item)

    if unknown_exercises:
        print("---------------------------------------------------------------------------------")
        print("Please add the necessary entries to the dictionary in exercise_name_conversion.py")

    with open("out.csv", "w") as outputFile:
        new_csv_file = csv.writer(outputFile, lineterminator='\n', delimiter=';')
        for i in range(len(gymrun_list)):
            new_csv_file.writerow(gymrun_list[i])
