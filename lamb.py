squared = lambda x: x ** 2
print(squared(4))

greater = lambda x, y: x if x > y else y
result = greater(3, 5)
print(result)

def my_func(n):
    return lambda x: x * n

doubler = my_func(2)
print(doubler(5))

tripler = my_func(3)
print(tripler(5))

l = [1, 2, 3, 4]

doubles = list(map(lambda x: x * 2, l))

print(doubles)

def convert_deg(C):
    return (9/5) * C + 32

temps = [12.5, 15.5, 18, 20]
converted_temp = map(convert_deg, temps)
print(converted_temp)

list_converted_temp = list(converted_temp)
print(list_converted_temp)


fahrenheit = list(map(lambda C: (9/5) * C + 32, temps))
print(fahrenheit)

def filter_temps(C):
    converted =  (9/5) * C + 32
    return True if converted > 55 else False

temps = [12.5, 15.5, 18, 20]
filtered_temps = filter(filter_temps, temps)
print(filtered_temps)

list_filtered_temps = list(filtered_temps)
print(list_filtered_temps)


filtered_temperature = list(filter(lambda C: True if (9/5) * C + 32 > 55 else False, temps))
print(filtered_temperature)

names = ["Saxor", "Meo", "Yno", "Jason"]
instructors = list(map(lambda name: f"Your instructor is {name}",
                    filter(lambda value: len(value) < 5, names)))

print(instructors)

# ['Your instructor is Saxor']​
l = [1, 2, 3, 4]

total = 1
for num in l:
    total = total * num

print(total)

def fib(n):
    if n <= 1: # base case
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(6))