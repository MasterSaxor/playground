message = input("Type something: ")

if not message:
    print("Message is empty")

last_character = message[-1]
if last_character == "?":
    print("That's a question")
elif last_character == ".":
    print("That's normal")
else:
    print("That's odder")