import csv
data = {
    'name': ["Dave", "Dennis", "Peter", "Jess"],
    'language': ["Python", "C", "Java", "Python"]
}


with open("data.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(data.keys())

    for i in range(len(data["name"])):
        writer.writerow([data["name"][i], data["language"][i]])

with open("data.csv", mode="r") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)



        
        
            
            

