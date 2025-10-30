sports = ["badminton", "cycling", "basketball", "chess", "soccer"]

my_iter = iter(sports)

print(next(my_iter))
print(next(my_iter))


for item in my_iter:
    print(item)
    

print(next(my_iter))
