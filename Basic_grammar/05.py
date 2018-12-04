# 给一个数，判断它是否是素数（质数）
# 质数：一个大于1的自然数,除了1和它本身外,不能被其它数整除
number = int(input("Please enter a number: "))
for i in range(2,number):
    if number % i == 0:
        print(number,"is not a prime number.")
        break
else:
    print(number,"is a prime number.")
