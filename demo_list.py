nums = [1, 2, 3]
print(nums)

nums.extend("abc")
print(nums)

nums.extend([5,7,8])
print(nums)

nums.append([5, 7, 9])
print(nums)

nums.insert(4, "me")
print(nums)

length = len(nums)
print(length)
sub_nums = nums[1:(length-1):2]
print(sub_nums)
print(nums)
