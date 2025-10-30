message = input("Input: ")

if not message:
    print("Empty string")

last_character = message[-1]

if last_character == "?":
    print("question")
elif last_character == ".":
    print("statement")
else:
    print("other")