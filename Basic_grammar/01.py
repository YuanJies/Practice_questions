# 输入2个数字,输出最大数
number_1 = int(input("Please enter the first number： "))
number_2 = int(input("Please enter the second number: "))
if number_1 >= number_2:
    print(number_1)
else:
    print(number_2)


    

# 给定一个不超过5位的正整数,判断其有几位
number = int(input("Please enter a positive integer no more than five digits: "))
if number >= 1000:
    if number >= 10000:
        print("What you type is: five digits")
    else:
        print("What you type is: four digits")
else:
    if number >= 100:
        print("What you type is: three digits")
    elif number >= 10:
        print("What you type is: two digits")
    else:
        print("What you type is: one digits")

        
        
        
# 计算10以内的偶数（for循环）
for i in range(0,10,2):
    print(i)
    
    
    
    
# 计算10以内的奇数（for循环）
for i in range(1,10,2):
    print(i)
    
    
    
    
# 计算1000以内的被7整除的前20个数(for循环)
count = 0
for i in range(0,1000,7):
    print(i)
    count += 1
    if count >= 20:
        break
