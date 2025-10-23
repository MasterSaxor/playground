
def ask_dog_age():
    age = int(input("Input your dog age: "))

    return age
    

def convert_dog_age(age):
    return age * 10


def display_age(human):
    print(f"Your dog age is equivalent to {human} in hooman years!")
    

dog_age = ask_dog_age()
print(dog_age)

human_equiavalent = convert_dog_age(dog_age)

display_age(human_equiavalent)


