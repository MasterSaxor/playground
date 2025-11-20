def eat(food, is_healthy):
    ending = "because you only lived once"

    if is_healthy:
        ending = "because I'm a vegetarian"


    return f"I'm eating {food}, {ending}"

def nap(hours):
    if hours > 2:
        return f"Uhg I overslept, I did'nt meant to sleep for {hours} hours"

    return  "I'm feeling refreshed"

def is_funny(name):
    if name == "me":
        return False
    return True


