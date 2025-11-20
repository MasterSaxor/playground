def lowest(num_list):
    if not num_list:
        return "The list should not be empty!"

    
    min = num_list[0]
    for num in num_list:
        if num < min:
            min = num

    return min


nums = [5, 3, 1, 22, 11]
print(lowest(nums))

print(lowest([]))
