'''
A file named food_order.txt has the following contents:

    5 sandwiches
    4 chips
    1 pickle
    soft drinks

Find the problem provided the code below.
'''

for line in open("lines.txt"):
    space = line.index(" ")
    qty = int(line[:space])
    item = line[space+1:-1]
    print(qty, item)