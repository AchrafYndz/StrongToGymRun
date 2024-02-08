# StrongToGymRun

## Convert all your Strong data to GymRun.
![](images/padded_logo.png)

## Installation

Open the terminal and run:

```bash
git clone https://github.com/YAchrafY/StrongToGymRun.git
```

## Usage

On your phone, open the Strong app. Go to settings and click the "Export data" button. This will export a csv file
containing all your workout data. Put this csv file in `csv_input/`. **Make sure** you name it `myStrongData.csv`.

Now simply run `main.py` and it will output a new csv file with the name `out.csv`. Next, launch the GymRun app. Click
on "More" and then "Backup". Here you will find multiple ways to import/export data. We want to import using `CSV (Entries)`. Finally select the `out.csv` file we just generated, and all your Strong data should be imported!

## FAQ

### Help, it says it could not find a translation entry for [ExerciseName]. What now?

- Simply open the file `static.py` and add your exercise to the dictionary in following convention:
  ![name conversion dictionary](images/dictionary_screenshot.png)

  If it's a bodyweight exercise, make sure you add it to the `bodyweight_exercises` list in the same file.
  ![bodyweight exercises list](images/bodyweight_exercises.png)

### Help, my exercise does not exist in GymRun. What do I do?

- You can simply create a new exercise in the GymRun app. Just make sure you use the same name in the `name_conversion` dictionary.
