# 数字重复统计
#    随机产生100个整数
#    数字的范围[-1000, 1000]
#    升序输出所有不同的数字及其重复的次数
	
# 示例：(Wayne)

import random
n = 100
nums = [0] * n
for i in range(n):
    nums[i] = random.randint(-1000, 1000)
print(nums)
t = nums.copy()
t.sort()
print(t)

d = {}
for x in nums:
    if x not in d.keys():
        d[x] = 1
    else:
        d[x] += 1
print(d)
d1 = sorted(d.items())
print(d1)



# 示例2：（其他）

import random
numlist = []
for i in range(100):
    numlist.append(random.randint(-1000,1000))
    
numdict = {}
for i in numlist:
    if i not in numdict:
        numdict[i] = 1
    else:
        numdict[i] += 1
print(sorted(numdict.items()))


#-----------------------------------------------

import random
lst = [random.randint(-1000, 1000) for i in range(100)]
dic = {}
for i in lst:
    if not dic.get(i):
        dic[i] = 1
    else:
        dic[i] += 1
lstkey = sorted(dic)
for k in lstkey:
    print(k,':',dic[k],sep='',end='  ')
