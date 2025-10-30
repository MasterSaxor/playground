
message = input("Type something: ")

if not message:
    print("empyty string")

last_character = message[-1]

if last_character == "?":
    print("question")
elif last_character == ".":
    print("statement")
else:
    print("other")
    