# 简单选择排序实现

lst = [1,9,8,5,6,7,4,3,2]
length = len(lst)

for i in range(length):
    x = lst[i]    # 1 和其他数比较,找出maxindex
    maxindex = i
    for j in range(i+1, length):    # j 1,2,.....
        if lst[j] > lst[maxindex]:
            maxindex = j
    if i != maxindex:
        lst[i], lst[maxindex] = lst[maxindex], lst[i]
print(lst)

#---------------------------------------------------------

m_list = [[1, 9, 8, 5, 6, 7, 4, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1]]

nums = m_list[1]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0

for i in range(length):
    maxindex = i
    for j in range(i + 1, length):
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
            
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1
        
print(nums, count_swap, count_iter)

#---------------------------------------------------------

# 优化实现
#    二元选择排序
#    同时固定左边最大值和右边最小值
	
# 优点：
#    减少迭代元素次数
		
# 1、length//2整除,通过几次运算就可以发现规律
# 2、由于使用了负索引,所以条件中要增加 i == length + minindex
	
m_list = [[1, 9, 8, 5, 6, 7, 4, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1]]

nums = m_list[1]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0
# 二元选择排序
for i in range(length // 2):
    maxindex = i
    minindex = -i - 1
    minorigin = minindex
    for j in range(i + 1, length - i):    # 每次左右都要少比较一个
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
        if nums[minindex] > nums[-j - 1]:
            minindex = -j - 1
            #print(maxindex,minindex)
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1
        # 如果最小值被交换过,要更新索引
        if i == minindex or i == length + minindex:
            minindex = maxindex
    if minorigin != minindex:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap += 1
    
print(nums, count_swap, count_iter)


# 改进优化实现
#    如果一轮比较后,极大值、极小值的值相等,说明比较的序列元素全部相等
	
m_list = [
    [1, 9, 8, 5, 6, 7, 4, 3, 2], 
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]
nums = m_list[3]
length = len(nums)
print(nums)
count_swap = 0 
count_iter = 0
# 二元选择排序
for i in range(length // 2):
    maxindex = i
    minindex = -i - 1
    minorigin = minindex
    for j in range(i + 1, length - i):    # 每次左右都要少比较一个
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
        if nums[minindex] > nums[-j - 1]:
            minindex = -j - 1
    #print(maxindex,minindex)
    if nums[maxindex] == nums[minindex]:    # 元素全相同
        break
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1
        # 如果最小值被交换过，要更新索引
        if i == minindex or i == length + minindex:
            minindex = maxindex
    if minorigin != minindex:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap += 1

print(nums, count_swap, count_iter)



# 改进实现
#    [1, 1, 1, 1, 1, 1, 1, 1, 2]这种情况,找到的最小值索引是-2,
#    最大值索引8,上面的代码会交换2次,最小值两个1交换是无用功,所以,增加一个判断


m_list = [
    [1, 9, 8, 5, 6, 7, 4, 3, 2], 
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2]
]
nums = m_list[4]
length = len(nums)
print(nums)
count_swap = 0 
count_iter = 0
# 二元选择排序
for i in range(length // 2):
    maxindex = i
    minindex = -i - 1
    minorigin = minindex
    for j in range(i + 1, length - i):    # 每次左右都要少比较一个
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
        if nums[minindex] > nums[-j - 1]:
            minindex = -j - 1
    print(maxindex,minindex)
    if nums[maxindex] == nums[minindex]:    # 元素全相同
        break
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1
        # 如果最小值被交换过，要更新索引
        if i == minindex or i == length + minindex:
            minindex = maxindex
    # 最小值索引不同，但值相同就没有必要交换了
    if minorigin != minindex and nums[minorigin] != nums[minindex]:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap +=1
        
print(nums, count_swap, count_iter)
