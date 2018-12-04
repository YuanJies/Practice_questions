# 打印斐波那契数列第101项
a = 1 
b = 1
index = 2
print('{0},{1}'.format(0,0))
print('{0},{1}'.format(1,1))
print('{0},{1}'.format(2,1))
while True:
    c = a + b
    a = b
    b = c
    index += 1
    print('{0},{1}'.format(index,c))
    if index == 101:
        break
 
#-----------------------------------------

a=1
b=1
for count in range(99):
    a,b = b,a+b
else:
    print(b)

#-----------------------------------------

x = 1
y = 1
for i in range(2,101):
    if i == 100:
        print(x+y)
    y += x
    x = y - x

#-----------------------------------------

num = int(input("Please enter a positive integer greater than zero："))
prev = 0    # 上次结果
rst = 1     # 当前结果
tmp = 0     # 临时存放
for i in range(1,num):
    tmp = prev + rst
    prev = rst
    rst = tmp
print(rst)
