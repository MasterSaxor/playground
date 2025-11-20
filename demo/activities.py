def eat(food, is_healthy):
    msg = "because you only lived once"

    if is_healthy:
        msg = "because my body requires it"

    return f"I'm eating {food} {msg}"

def nap(hours):
    if hours > 1:
        return f"Oh no, I overslept, did'nt meant to sleept for {hours} hours"

    return "Feels good, I'm feeling refreshed"

def is_funny(name):
    if name == "Me":
        return False
    
    return True

