'''
password = input("What's the magic password? ").strip()

while password != "eyy":
    password = input("Password: ").strip()


finished = False

while not finished:
    password = input("Password: ").strip()
    finished = password == "saxor"

    
password = ""
while password != "saxor":
    password = input("Password: ").strip()
'''

targets = [2, 3, 5, 4, -1, 1]
index = 0

count = 0
while targets[index] != -1:
    count += 1
    index = targets[index]
    print(f"Loop No.{count}   Index:{index}")


    



