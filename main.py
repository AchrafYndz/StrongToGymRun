import csv
import datetime
from exercise_name_conversion import name_conversion


def main():
    strong_list = []
    gym_run_list = []

    with open("csv_input/my_strong_data.csv", "r") as inputFile:
        my_csv_file = csv.reader(inputFile, delimiter=';')
        for row in my_csv_file:
            print(row)
            strong_list.append(row)

    prev_time_object = datetime.datetime.now()
    for item in strong_list:
        gym_run_item = []
        if item == strong_list[0]:
            gym_run_list.append(["Date", "Time", "Exercise", "Set", "Weight", "Reps", "Note"])
            continue

        # handling date and time
        strong_date_and_time = item[0]
        date_and_time_list = strong_date_and_time.split(" ")

        # convert date format
        date = date_and_time_list[0]
        date_list = date.split("-")
        time_string = date_and_time_list[1]
        time_object = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), int(time_string[:2]),
                                        int(time_string[3:5]), int(time_string[6:]))
        if 0 <= abs(prev_time_object - time_object).total_seconds() <= 86400:
            time_object = prev_time_object + datetime.timedelta(seconds=1)
        new_day = time_object.strftime("%d.%m.%y")
        gym_run_item.append(new_day)
        prev_time_object = time_object

        new_time = time_object.strftime("%H:%M:%S")
        gym_run_item.append(new_time)

        # handling exercise names
        strong_exercise_name = item[2]
        try:
            gym_run_item.append(name_conversion[strong_exercise_name])
        except KeyError:
            print("Could not find translation entry for \"" + strong_exercise_name + "\"")
            print("Please add an entry to the dictionary in exercise_name_conversion.py")

        # handling set orders
        set_order = item[3]
        gym_run_item.append(set_order)

        # handling weight
        weight = item[4]
        body_weight_exercises = ["Knee Raise (Captain's Chair)", "Plank", "Hanging Knee Raise", "Hanging Leg Raise"]
        if weight == "" and strong_exercise_name not in body_weight_exercises:
            gym_run_item.append("0")
        else:
            gym_run_item.append(weight)

        # handling reps
        reps = item[6]
        gym_run_item.append(reps)

        # handling notes
        notes = item[10]
        gym_run_item.append(notes)
        gym_run_list.append(gym_run_item)

    with open("out.csv", "w") as outputFile:
        new_csv_file = csv.writer(outputFile, lineterminator='\n', delimiter=';')
        for i in range(len(gym_run_list)):
            new_csv_file.writerow(gym_run_list[i])


if __name__ == "__main__":
    main()
