'''
nums = [1, 2, 3, 2, 5, 3, 5, 7]

for num in nums:
    print(num)

print()

new_list = []
for index in range(len(nums)):
    print(f"Index: {index}\t Value: {nums[index]}")

    if index % 2 == 1:
        new_list.append(nums[index])

print(new_list)


for index, value in enumerate(nums):
    print(index, value)
'''

targets = [2, 3, 5, 4, -1, 1]
index = 0
count = 0

while targets[index] != -1:
    index = targets[index]
    print(index)
    count += 1

print(f"No. of loops: {count}")







