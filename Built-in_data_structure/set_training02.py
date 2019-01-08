# 随机产生2组各10个数字的列表,如下要求：
# 	每个数字取值范围[10,20]
# 	统计20个数字中,一共有多少个不同的数字?
# 	2组比较,不重复的数字有几个?分别是什么？
# 	2组比较,重复的数字有几个？分别是什么？
	

a = [1, 9, 7, 5, 6, 7, 8, 8, 2, 6]
b = [1, 9, 0, 5, 6, 4, 8, 3, 2, 3]
s1 = set(a)
s2 = set(b)
print(s1)
print(s2)
print(s1.union(s2))
print(s1.symmetric_difference(s2))
print(s1.intersection(s2))


#--------------------------------------------------

import random
a = []
b = []
for i in range(10):
    a.append(random.randint(10,20))
    b.append(random.randint(10,20))
print(a)
print(b)

s1 = set(a)
s2 = set(b)
print(s1)
print(s2)

print(s1 | s2)
print(s1 ^ s2)
print(s1 & s2)
