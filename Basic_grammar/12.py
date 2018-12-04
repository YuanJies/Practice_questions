# 求10万内的所有素数（注意效率问题）
for i in range(2,100000):
    for x in range(2,i):
        if i % x == 0:
            break
    else:
        print(i)
        
#-------------------------------------------------------------------
# 判断N是否是质数,判断到根号N就可以了,只用看从2到根号N,是否能整除N

for i in range(2,100000):
    for x in range(2,int(i ** 0.5)+1):
        if i % x == 0:
            break
    else:
        print(i)

#-------------------------------------------------------------------

for i in range(3,100000,2):       # 舍弃掉所有偶数    
    for x in range(3,int(i ** 0.5)+1,2):     # 既然没有偶数,就不用和2取模了
        if i % x == 0:
            break
    else:
        print(i)

#-------------------------------------------------------------------
# 利用素数性质：所有大于10的质数中,个位数只有1,3,7,9

count = 1
for x in range(3,100000,2):          #舍弃掉所有偶数
    if x > 10 and x % 10 == 5:       #所有大于10的质数中,个位数只有1,3,7,9。意思就是大于5,结尾是5就能被5整除了
        continue
    for i in range(3,int(x ** 0.5)+1,2):
        if x % i == 0:
            break
    else:
        count += 1
        print(x,count)

#-------------------------------------------------------------------
# 如何计算时间：import datetime

count = 0
for i in range(2,100000):
    for x in range(2,i):
        if i % x == 0:
            break
    else:
        count += 1
print(count)




count = 0
for i in range(2,100000):
    for x in range(2,int(i ** 0.5)+1):
        if i % x == 0:
            break
    else:
        count += 1
print(count)

#-------------------------------------------------------------------
# 示例2和示例3两种算法的时间对比

import datetime

upper_limit = 100000
delta = [0,0]
counts = [0,0]

start = datetime.datetime.now()
for _ in range(10):
    counts[0] = 0
    for x in range(2,upper_limit):
        for i in range(2,int(x ** 0.5)+1):
            if x % i == 0:
                break
        else:
            counts[0] += 1
delta[0] = (datetime.datetime.now() - start).total_seconds()


start = datetime.datetime.now()
for _ in range(10):
    counts[1] = 1
    for x in range(3,upper_limit,2):
        for i in range(3,int(x ** 0.5)+1,2):
            if x % i == 0:
                break
        else:
            counts[1] += 1
delta[1] = (datetime.datetime.now() - start).total_seconds()

print(delta,sep="\t")
print(counts,sep="\t")
