#for num in range(1, 10, 2):
#    print(num)

for num in range(1, 21):
    
    if num % 2 == 1:
        if num == 13:
            print(f"{num} is UNLUCKY")
            continue

        print(f"{num} is ODD")
    elif num % 2 == 0:
        if num == 4:
            print(f"{num} is UNLUCKY")
            continue

        print(f"{num} is EVEN")
    
    