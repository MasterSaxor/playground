import csv

with open("testing.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Municipality"])
    writer.writerow(["Melvinn", "Calatagan"])
    writer.writerow(["Albert", "Nasugbu"])
    writer.writerow(["Meo", "Lian"])


