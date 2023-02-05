import csv

with open('details.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("Entry " + row["Id"])
        print("    - Name: " + row["Name"])
        print("    - Age: " + row["Age"])
        print("    - Favourite Food: " + row["Favourite Food"])