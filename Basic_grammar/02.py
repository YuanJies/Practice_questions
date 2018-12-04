# 给定一个不超过5位的正整数,判断该数的位数,依次打印出个位、十位、百位、千位、万位的数字
number = int(input("Please enter a positive integer no more than five digits: "))
if number >= 1000:
    if number >= 10000:
        num = 5
    else:
        num = 4
else:
    if number >= 100:
        num = 3
    elif number >= 10:
        num = 2
    else:
        num = 1
a = number
for i in range(num):
    b = a % 10
    a //= 10
    print(b)
    
#----------------------------------------------------------------------------------    
 
number = int(input("Please enter a positive integer no more than five digits: "))
number *= 10
while (number // 10) != 0:
    number //= 10
    print(number % 10)   
