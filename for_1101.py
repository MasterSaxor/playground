for num in range(1, 21):
    if num % 2 == 0:
        if num == 4:
            print(f"{num} is UNLUCKY")
            continue
        print(f"{num} is EVEN")
    elif num % 2 == 1:
        print(f"{num} is ODD")

    '''
    2nd way
    if num == 4:
        print(f"{num} is UNLUCKY")
    elif num % 2 == 0:
        print(f"{num} is EVEN")
    elif num % 2 == 1:
        print(f"{num} is ODD")
    '''
    