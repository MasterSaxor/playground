'''
def fib_list(max):
    nums = []
    a, b = 0, 1

    while len(nums) < max:
        nums.append(b)
        a, b, = b, a+b

    return nums

print(fib_list(1000000))
'''

def fib_gen(max):
    a = 0
    b = 1
    count = 0

    while count < max:
        a, b = b, a+b
        yield a
        count += 1

for n in fib_gen(1000000):
    print(n)
