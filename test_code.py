
def avg_line_length(file_name):
    try:
        file = open(file_name)

        lines = file.read().splitlines()
        total = sum(len(line) for line in lines)

        return total / len(lines)

    except ZeroDivisionError:
        return "not defined"
        file.close()
    
    except FileNotFoundError:
        return "File does not exists!"

    finally:
        print("Closing time...")
        #file.close()


print(avg_line_length("lines.txt"))
print(avg_line_length("empty.txt"))
print(avg_line_length("secret.txt"))