import csv


def fix_double():
    # Read in the input CSV file
    with open('csv_input/GymRun_23Dec22.csv', 'r') as input_file:
        reader = csv.reader(input_file, delimiter=';')
        # Skip the header row
        next(reader)
        # Create a set to store the unique {date, exercise, set} tuples
        unique_rows = set()
        # Create a list to store the modified rows
        modified_rows = []
        # Iterate through the rows in the input CSV file
        for row in reader:
            # Extract the date, exercise, and set values from the row
            date = row[0]
            exercise = row[3]
            set_num = row[4]
            # Check if the {date, exercise, set} tuple is unique
            if (date, exercise, set_num) not in unique_rows:
                # If it is unique, add it to the set and append the row to the modified rows list
                unique_rows.add((date, exercise, set_num))
                modified_rows.append(row)

    # Write the modified rows to the output CSV file
    with open('fixed.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=';')
        # Write the header row
        writer.writerow(
            ['Date', 'Time', 'Routine', 'Exercise', 'Set', 'Weight', 'Reps', 'Duration', 'Distance', 'Para6', 'Para7',
             'Para8', 'Para9', 'Para10', 'Note', 'Type', 'Book', 'Version1'])
        # Write the modified rows
        for row in modified_rows:
            writer.writerow(row)
