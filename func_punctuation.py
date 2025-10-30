
def get_punctuation(message):
    if not message:
        return "Message is empty"

    last_character = message[-1]

    if last_character == "?":
        return "That's a question"
    elif last_character == ".":
        return "That's normal"
    return "That's odder"
    
print(get_punctuation("This is a message"))
print(get_punctuation("This is a message."))
message = "Are we good?"
print(get_punctuation(message))
print(get_punctuation("Another one"))
print(get_punctuation(""))

