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

    
    
    
# 给定一个不超过5位的正整数，判断该数的位数，依次从万位打印到个位的数字
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
a = 0
for i in range(num,0,-1):
    b = number // (10 ** (i - 1))
    print(b - a * 10)
    a = b
    
#------------------------------------------------------------------------------------
number = int(input("Please enter a positive integer no more than five digits: "))
if number >= 1000:
    if number >= 10000:
        num = 10000
    else:
        num = 1000
else:
    if number >= 100:
        num = 100
    elif number >= 10:
        num = 10
    else:
        num = 1
while num != 0:
    print(number // num)
    number %= num
    num //= 10
    
#------------------------------------------------------------------------------------
number = int(input("Please enter a positive integer no more than five digits: "))
w = 10000
length = 5
flag = False
while w:
    t = number // w
    if flag:
        print(t)
    else:
        if t:
            print(t)
            flag = True
        else:
            length -= 1
    number %= w
    w //= 10
print("The length of number if",length)
