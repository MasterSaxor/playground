nums = [3, 5, 2, 1, 7, 8, 5]


print(len(nums))
print()

# Accessing values by item/name
for num in nums:
    print(num)

print()

# Accessing values by index
print(nums[0])
print(nums[3])
print()

odd_no_index = []
for index in range(len(nums)):
    print(f"At the index {index}, the value is {nums[index]}")

    if index % 2 == 1:
        odd_no_index.append(nums[index])

print()
print(odd_no_index)
print()

for i, value in enumerate(nums):
    print(f"Item No.{i+1}, the value is {value}")
