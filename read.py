import csv

with open("testing.csv", "r") as f:
   reader = csv.reader(f, delimiter=",")
   for row in reader:
     print(row)

