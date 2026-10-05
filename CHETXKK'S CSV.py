import csv

# Data to be written
Chetxkk = [
    ["Hello my name is Chetxkk Navale"],
    ["My department is CSE"],
    ["I am from CSE Department"]
]

# Create and write to CSV file
with open("Chetxkk.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(Chetxkk)

print("CSV file created successfully.")

# Read data from CSV file
with open("Chetxkk.csv", "r") as file:
    lines = file.readlines()

# Display the data
for line in lines:
    print(line.strip())
