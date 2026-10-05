import csv
# Data to be written
students = [
    [101, "Rahul", 85],
    [102, "Priya", 92],
    [103, "Amit", 78]
]

# Create and write to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["RollNo", "Name", "Marks"])

    # Write student data
    writer.writerows(students)

# Read CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
