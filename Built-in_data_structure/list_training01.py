# 求100内的素数
# 从2开始到自身的-1的数中找到一个能整除的,从2开始到自身开平方的数中找到一个能整除的
# 一个合数一定可以分解成几个素数的乘积,也就是说,一个数如果能被一个素数整除就是合数
# 合数：一个正整数，除了1和它本身以外，还能被其他正整数整除，这个数就叫做合数。如4、6、9、10等

# 示例：一个数能被从2开始到自己平方根的正整数整除,就是合数
import math
n = 100
for x in range(2, n):
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0:
            break
    else:
        print(x)
		
		
#--------------------------------------------------

改进1
合数一定可以分解为几个质数的乘积
import math
n = 100
primenumber = []
for x in range(2,n):
    for i in primenumber:
        if x % i == 0:
            break
    else:
        print(x)
        primenumber.append(x)
        
        
#--------------------------------------------------

改进2
进一步缩小取模的范围,使用列表存储已有的质数,同时增加范围
import math
primenumber = []
flag = False
for x in range(2,100000):
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        print(x)
        primenumber.append(x)
		
		
#--------------------------------------------------	

n = 100
lst = [2]
for i in range(3, n):
    flag = False
    for j in lst:
        if j > i**0.5:
            flag = True
            break    #是素数
        if i % j == 0:
            flag = False
            break    #合数

    if flag:
        print(i)    #找到一个质数
        lst.append(i)	


#--------------------------------------------------

计算时间比较
import datetime
upper_limit = 100000
start = datetime.datetime.now()
count = 1
for x in range(3, upper_limit, 2):    # 舍弃掉所有偶数
    if x > 10 and x % 10 == 5:    # 所有大于10的质数中，个位数只有1，3，7，9。意思就是大于5，结尾是5就能被5整除了
        continue
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            break
    else:
        count += 1
        #print(x, count)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


start = datetime.datetime.now()
x = 5
step = 2
count = 2
#print(2, 3, sep='\n')
while x < upper_limit:
    for i in range(3, int(x ** 0.5) + 1, 2):    
        if not x % i:
            break
    else:
        #print(x)
        count += 1
        
    x += step
    setp = 4 if step == 2 else 2
    
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



# 改进2
# 使用列表存储已有的质数，同时增加范围
import math

start = datetime.datetime.now()
primenumber = []
flag = False
count = 0
for x in range(2, 100000):
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        #print(x)
        count += 1
        primenumber.append(x)
        
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


增加了列表并没有大幅度提升

#--------------------------------------------------
进一步修改,去除偶数
改进2
使用列表存储已有的质数,同时增加范围
import math

start = datetime.datetime.now()
primenumber = []
flag = False
count = 1
for x in range(3, 100000, 2):    # 奇数
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        #print(x)
        count += 1
        primenumber.append(x)
        
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

但是结果并没有提高计算速度
经过分析,得到下面的代码

#--------------------------------------------------
改进2
使用列表存储已有的质数,同时增加范围
import math

start = datetime.datetime.now()
primenumber = []
flag = False
count = 1
for x in range(3, 100000, 2):
    edge = math.ceil(math.sqrt(x))
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= edge:
            flag = False
            break
    if not flag:
        #print(x)
        count += 1
        primenumber.append(x)
        
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

直接提速,计算速度第一位
本质上就是空间换时间
