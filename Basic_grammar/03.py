# 打印一个边长为n的正方形
number = int(input("Please enter the side length of the square: "))
print("*" * number)
for i in range(number-2):
    print("*" + " " * (number - 2) + "*")
print("*" * number)

#----------------------------------------------------------------------

number = int(input("Please enter the side length of the square: "))
e = -number  // 2
for i in range(e,number+e):
    if i == e or i == number + e - 1:
        print("*" * number)
    else:
        print("*" + " " * (number - 2) + "*")
       
#-----------------------------------------------------------------------

等价于上一个
number = int(input("Please enter the side length of the square: "))
for i in range(number):
    if i == 0 or i == number - 1:
        print("*" * number)
    else:
        print("*" + " " * (number - 2) + "*")
