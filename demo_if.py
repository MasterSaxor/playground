def get_punctuation(message):
    if not message:
        return  "empyty string"

    last_character = message[-1]
    if last_character == "?":
        return "question"
    elif last_character == ".":
        return "statement"
    
    return "other"
    
print(get_punctuation("saxor"))

