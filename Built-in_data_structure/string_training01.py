# 用户输入一个数字
# 	判断是几位数
# 	打印每一位数字及其重复的次数
# 	依次打印每一位数字，顺序个、十、百、千、万...位

num = ''
# 数字输入的简单判断
while True:
    num = input('Input a positive number >>> ').strip().lstrip('0')
    if num.isdigit():
        break
print("The length of {} is {}.".format(num, len(num)))

# 倒序打印1
for i in range(len(num), 0, -1):
    print(num[i-1], end=' ')
print()

# 判断0-9的数字在字符串中出现的次数,每一次迭代都是用count,都是O(n)问题
counter = [0] * 10
for i in range(10):    # 10*n
    counter[i] = num.count(str(i))
    if counter[i]:
        print("The count of {} is {}".format(i, counter[i]))
print('~'*20)


#-----------------------------------------------------------------------------

num = ''
# 数字输入的简单判断
while True:
    num = input('Input a positive number >>> ').strip().lstrip('0')
    if num.isdigit():
        break
print("The length of {} is {}.".format(num, len(num)))

# 倒序打印2
for i in reversed(num):
    print(i, end=' ')
print()

# 迭代字符串本身的字符
counter = [0] * 10
for x in num:    # unique(n) * n, unique(n)取值[1,10]
    i = int(x)
    if counter[i] == 0:
        counter[i] = num.count(x)
        print("The count of {} is {}".format(x, counter[i]))
print('~'*20)


#-----------------------------------------------------------------------------

num = ''
# 数字输入的简单判断
while True:
    num = input('Input a positive number >>> ').strip().lstrip('0')
    if num.isdigit():
        break
print("The length of {} is {}.".format(num, len(num)))

# 负索引方式打印
for i in range(len(num)):
    print(num[-i-1], end=' ')
print()

# 迭代字符串本身的字符
counter = [0] * 10
for x in num:    # n
    i = int(x)
    counter[i] += 1

for i in range(len(counter)):
    if counter[i]:
        print("The count of {} is {}".format(i, counter[i]))
        
        
#-----------------------------------------------------------------------------

num = input("<<<<")
length = len(num)
print("length:{}".format(length))

lst = [0] * 10
for i in range(1, length+1):
    print(num[-i],end='')
    lst[int(num[-i])] += 1
print()
for j in range(10):
    if lst[j]:
        print("{}出现:{:3}".format(j, lst[j]))
        
        
#-----------------------------------------------------------------------------

a = str(int(input(">>>>")))
if a.startswith('-'):
    lena = len(a)-1
else:
    lena = len(a)
print("数字{}是{}位数,".format(a, lena))
for i in a:
    if i == '-':
        continue
    print("数字{}重复{}次".format(i, a.count(i)))
for x in reversed(a):
    print(x)
    
    
#-----------------------------------------------------------------------------

str1 = input(">>>please input a integer: ")
length = len(str1)
print(length)

for i in range(1, length+1):
    time = str1.count(str1[-i])
    print(str1[-i], time)
    
    
#-----------------------------------------------------------------------------

n = input(">>>")
length = len(n)
print(length)

for i in range(10):
    z = n.count(str(i)) # n * 10
    print(z)


lst = list(n)
for x in range(length):
    for y in range(length-1-x):
        if lst[y]>lst[y+1]:
            lst[y], lst[y+1] = lst[y+1], lst[y]
print(lst)
