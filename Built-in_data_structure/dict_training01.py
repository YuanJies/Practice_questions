# 用户输入一个数字
#    打印每个数字及其重复的次数

# 示例：(Wayne)

num = input('>>>>')
d = {}
for c in num:
    if not d.get(c):
        d[c] = 1
        continue
    d[c] += 1
    
print(d)


#--------------------------------------

num = input('>>>')
d = {}
for c in num:
    if c not in d.keys():
        d[c] = 1
    else:
        d[c] += 1
print(d)



# 示例2：（其他）

num = input('>>>>>')
d = {}
for c in num:
    if c not in d.keys():
        d[c] = 0
    d[c] += 1
print(d)


#--------------------------------------

from collections import defaultdict
num = input('>>>>>')
d = defaultdict(int)
for c in num:
    d[c] += 1
print(d)


#--------------------------------------

num = input('>>>>>')
d = {}
for c in num:
    d[c] = d.get(c, 0) + 1
print(d)
