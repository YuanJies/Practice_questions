# 编写一个函数，能够接受至少2个参数，返回最小值和最大值
# 示例：（Wayne）

import random
def double_values(*nums):
    print(nums)
    return max(nums), min(nums)

print(*double_values(*[random.randint(10, 20) for _ in range(10)]))

# double_values(*[random.randint(10, 20) for _ in range(10)])


# 示例：（其他）
def nums(x, y, *args):
    print(min(x, y, *args))
    print(max(x, y, *args))
	
nums(1, 5, 3, 0, -1)
