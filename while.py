'''
password = input("Password: ").strip()
while password != "ey":
    password = input("Password: ").strip()

    
finished = False
while not finished:
    password = input("Password: ").strip()
    finished = password == "ey"
'''

targets = [2, 3, 5, 4, -1, 1]
index = 0
count = 0
while targets[index] != -1:
    index = targets[index]
    count += 1
    print(f"Loopn No.{count}  Index: {index}")
