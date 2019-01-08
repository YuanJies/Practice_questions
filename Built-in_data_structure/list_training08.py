# 随机产生10个数字
# 要求：
#	 每个数字取值范围[1, 20]
#  统计重复的数字有几个?分别是什么?
#  统计不重复的数字有几个?分别是什么?
	
#  举例：11, 7, 5, 11, 6, 7, 4,其中2个数字7和11重复了,3个数字4、5、6没有重复过

# 思路：
# 对于一个排序的序列,相等的数字会挨在一起。但是如果先排序,还是要花时间,能否不排序解决？
# 例如11,7,5,11,6,7,4、先拿出11,依次从第二个数字开始比较,发现11就把对应索引标记
# 这样一趟比较就知道11是否重复,哪些地方重复。
# 第二趟使用7和其后数字依次比较,发现7就标记,
# 当遇到以前比较过的11的位置的时候,其索引已经被标记为1,直接跳过。

import random

nums = []
for _ in range(10):
    nums.append(random.randrange(21))

#nums = [1,22,33,56,56,22,4,56,9,56,2,1]
print("Origin numbers = {}".format(nums))
print()

length = len(nums)
samenums = []    # 记录相同的数字
diffnums = []    # 记录不同的数字
states = [0] * length    # 记录不同的索引异同状态

for i in range(length):
    flag = False    # 假定没有重复
    if states[i] == 1:
        continue
    for j in range(i+1, length):
        if states[j] == 1:
            continue
        if nums[i] == nums[j]:
            flag = True
            states[j] = 1
    if flag:    # 有重复
        samenums.append(nums[i])
        states[i] = 1
    else:
        diffnums.append(nums[i])

print("Same numbers = {1}, Counter = {0}".format(len(samenums), samenums))
print("Different numbers = {1}, Counter = {0}".format(len(diffnums), diffnums))
print(list(zip(states, nums)))


#------------------------------------------------------------------

import random
lst = []
rep_lst = []
uniq_lst = []
for i in range(10):
    temp = random.randint(1,20)
    if temp in lst and temp not in rep_lst:
        rep_lst.append(temp)
    lst.append(temp)
    
for j in lst:
    if j not in rep_lst:
        uniq_lst.append(j)
print(lst)
print(len(rep_lst), ': ',rep_lst)
print(len(uniq_lst), ': ',uniq_lst)


#------------------------------------------------------------------

import random
lst = [0] * 21
stri = ""
strimin = ""
strimax = ""
for i in range(10):
    num = random.randint(1,20)
    lst[num] += 1
maxnum = max(lst)
for j in range(1,21):
    if lst[j] > 0:
        stri += "{},".format(j)
    if lst[j] == 1:
        strimin += "{},".format(j)
    if lst[j] == maxnum:
        strimax += "{},".format(j)
print("数字最多出现过{}次".format(maxnum))
print("数字出现有:{}其中{}出现过{}次，其中{}只是出现过1次".format(stri,strimax,maxnum,strimin))

