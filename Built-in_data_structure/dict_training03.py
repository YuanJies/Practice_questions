# 字符串重复统计
#  字符表'abcdefghijklmnopqrstuvwxyz'
#  随机挑选2个字母组成字符串,共挑选100个
#  降序输出所有不同的字符串及重复的次数
	
# 示例：(Wayne)

import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = []
for _ in range(100):
    #words.append(random.choice(alphabet)+random.choice(alphabet))
    #words.append(''.join(random.sample(alphabet, 2)))    # 随机采样
    words.append(''.join(random.choice(alphabet) for _ in range(2)))    # 生成器
    
d = {}
for x in words:
    d[x] = d.get(x,0) + 1
print(d)

d1 = sorted(d.items(), reverse=True)
print(d1)



# 示例2：（其他）

strs = 'abcdefghijklmnopqrstuvwxyz'
import random
dict1 = {}
for i in range(100):
    str1 = ''.join(random.sample(strs,2))
    if str1 not in dict1:
        dict1[str1] = 1
    else:
        dict1[str1] += 1
for j in reversed(sorted(dict1.keys())):
    print(j,end='  ')
    print("Repeat {} times".format(dict1[j]))


#----------------------------------------------------	

import random
from collections import OrderedDict
s = 'abcdefghijklmnopqrstuvwxyz'
lst = []
dic = OrderedDict()

for j in range(100):
    val1 = random.randint(0,25)
    val2 = random.randint(0,25)
    new_s = s[val1]+s[val2]
    lst.append(new_s)
    
length = len(lst)
for i in range(length):
    maxindex = i
    for s in range(i+1,length):
        if lst[s] > lst[maxindex]:
            maxindex = s
        if i != maxindex:
            tmp = lst[i]
            lst[i] = lst[maxindex]
            lst[maxindex] = tmp
print(lst)

for k in lst:
    val = lst.count(k)
    dic.setdefault(k,val)
print(dic)
	
	
#----------------------------------------------------	

import random
from collections import OrderedDict
s = 'abcdefghijklmnopqrstuvwxyz'
lst = []
dic = OrderedDict()

for j in range(100):
    lst.append(s[random.randint(0,25)]+s[random.randint(0,25)])
    
length = len(lst)
for i in range(length):
    maxindex = i
    for s in range(i+1, length):
        if lst[s] > lst[maxindex]:
            maxindex = s
        if i != maxindex:
            lst[i], lst[maxindex] = lst[maxindex], lst[i]
print(lst)

for k in lst:
    if k not in dic.keys():
        dic[k] = 1
    else:
        dic[k] += 1
print(dic)
