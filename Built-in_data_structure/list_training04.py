# 冒泡法
# 简单实现
numlist = [[1, 9, 8, 5, 6, 7, 4, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
nums = numlist[0]
print(nums)
length = len(nums)
count_swap = 0
count = 0
for i in range(length):
    for j in range(length-i-1):
        count += 1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            count_swap += 1
print(nums, count_swap, count)



# 优化
num_list = [[1, 9, 8, 5, 6, 7, 4, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 9, 8]]
nums = num_list[2]
print(nums)
length = len(nums)
count_swap = 0
count = 0
for i in range(length):
    flag = False
    for j in range(length-i-1):
        count += 1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            flag = True    # swapped
            count_swap += 1
    if not flag:
        break
print(nums, count_swap, count)



lst = [1, 3, 2, 0]
length = len(lst)

for i in range(length):
    for j in range(length - 1 - i):
        if lst[j] > lst[j+1]:
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp
            #lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)
