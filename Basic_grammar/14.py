# 获取最大值,请输入若干个整数,打印出最大值
m=0
count=1
while True:
    num=int(input("Please input a number:"))
    if num > m:
        m=num
    count+=1
    if count>2:
        choice=input("Continue?(Y/N):")
        if choice=="N":
            print(m)
            break
            
#-------------------------------------------------------------------------------

number = int(input("number"))
n = int(input("how"))
for i in range(n):
	newnumber = int(input("number"))
	if newnumber >= number:
		number = newnumber
	else:
		print(number)
    
#-------------------------------------------------------------------------------

x = int(input("数字个数"))
z = 0
for i in range(x):
	y = int(input("数字"))
	if not z:
		z = y
	if y > z:
		z = y
print("max",z)




# 输入n个数,求每次输入后的算术平均数
n = 0    #次数
sum = 0    #和
while True:
    i = input(">>>>>")
    if i == "quit":
        break

    n += 1
    sum += int(i)
    avg = sum / n 
    print(avg)
