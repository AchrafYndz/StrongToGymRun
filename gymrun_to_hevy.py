import csv
from datetime import datetime
from static import conversion_name, bodyweight_exercises

# Constants for the input and output CSV file names
INPUT_FILE = 'fixed.csv'
OUTPUT_FILE = 'output.csv'

# Constants for the input CSV file columns
DATE_COLUMN = 0
TIME_COLUMN = 1
ROUTINE_COLUMN = 2
EXERCISE_COLUMN = 3
SET_COLUMN = 4
WEIGHT_COLUMN = 5
REPS_COLUMN = 6
DURATION_COLUMN = 7
DISTANCE_COLUMN = 8
NOTE_COLUMN = 14
TYPE_COLUMN = 15

date_time_set = set()


def gymrun_to_hevy():
    # Open the input and output files
    with open(INPUT_FILE, 'r') as input_file, open(OUTPUT_FILE, 'w', newline='') as output_file:
        # Create the CSV reader and writer
        reader = csv.reader(input_file, delimiter=';')
        writer = csv.writer(output_file, delimiter=',', quotechar="'")
        unknown_exercises = set()

        # Write the header row for the output CSV file
        writer.writerow(
            ['Date', 'Workout Name', 'Exercise Name', 'Set Order', 'Weight', 'Weight Unit', 'Reps', 'Distance',
             'Distance Unit', 'Seconds', 'Notes', 'Workout Notes'])

        # Iterate over each row in the input CSV file
        for row in reader:
            # Skip the first row, which is the header row
            if reader.line_num == 1:
                continue

            # Extract the data from the row
            date = row[DATE_COLUMN]
            time = row[TIME_COLUMN]
            routine = row[ROUTINE_COLUMN]
            exercise = row[EXERCISE_COLUMN]
            set_order = row[SET_COLUMN]
            weight = row[WEIGHT_COLUMN]
            reps = row[REPS_COLUMN]
            duration = row[DURATION_COLUMN]
            distance = row[DISTANCE_COLUMN]
            note = row[NOTE_COLUMN]
            weight_unit = 'kg'
            distance_unit = ''

            # Format the date and time into a single datetime string
            date_time = ''

            date_obj = datetime.strptime(date, '%d.%m.%Y')

            for item in date_time_set:
                if item.date() == date_obj.date():
                    date_time = item

            if not date_time:
                date_time = datetime.strptime(f'{date} {time}', '%d.%m.%Y %H:%M:%S')
                date_time_set.add(date_time)

            # Convert the exercise name
            # converted_exercise = next((k for k, v in name_conversion.items() if v == exercise), None)

            try:
                converted_exercise = conversion_name[exercise]
            except:
                unknown_exercises.add(exercise)

            if not converted_exercise:
                unknown_exercises.add(exercise)

            # Add a default routine name
            if not routine:
                routine = 'default'

            # Handle zero weight
            if not weight and converted_exercise in bodyweight_exercises:
                weight = ''
                weight_unit = ''

            if converted_exercise == 'Plank':
                distance_unit = 'km'
                weight_unit = ''

            if note:
                note = '"' + note + '"'

            # Write the row
            writer.writerow(
                [date_time, '"'+routine+'"', '"'+converted_exercise+'"', set_order, weight, weight_unit, reps, '',
                 distance_unit, 0, note, ''])

    if unknown_exercises:
        for unknown_exercise in unknown_exercises:
            print(unknown_exercise)
        print("Please fill the " + str(len(unknown_exercises)) + " exercises first")
    else:
        print("Successfully generated csv.")
