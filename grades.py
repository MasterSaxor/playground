import csv

total = 0

with open("grades.csv") as file:
    grades = csv.DictReader(file)
       
    for row in grades:
        grade = row["grade"].strip()
        total += float(grade)

    print(total/len(row))




        


