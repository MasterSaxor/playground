weather = "unpleasant"

temperature = int(input("What is the temperature in Fahrenheit? "))
rainfall = 0

if temperature > 50:
    if temperature < 80:
        if rainfall == 0:
            weather = "nice"

print(weather)