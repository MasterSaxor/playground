f = open("file.txt", "w")
f.write("this is a simple testing")
f.close()

f = open("file.txt", "r")
data = f.read()

print(data)