import csv

with open("people.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)


    for row in reader:
        name = row["name"]
        role = row["role"]

        sentence = f"{name} works as a {role.upper()}."
        print(sentence)