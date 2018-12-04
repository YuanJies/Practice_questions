# 输入2个数字,输出最大数
number_1 = int(input("Please enter the first number： "))
number_2 = int(input("Please enter the second number: "))
if number_1 >= number_2:
    print(number_1)
else:
    print(number_2)


    

# 给定一个不超过5位的正整数,判断其有几位
number = int(input("Please enter a number not exceeding five digits: "))
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
