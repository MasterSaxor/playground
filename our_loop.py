def our_loop(iterable, func):
    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        
        func(item)


def square(x):
    print(x*x)

sports = ["badminton", "cycling", "basketball", "chess", "soccer"]
our_loop(sports, print)
our_loop([1,2,3,4,5], square)



