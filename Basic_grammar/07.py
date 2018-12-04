# 打印一个菱形
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *
for i in range(-3,4):
    if i < 0:
        a = -i
    else:
        a = i
    print(" " * a + "*" * (7 - a * 2))
    
#------------------------------------------------

for i in range(7):
    i = i + 1
    if i <= 4:
        x = 4 - i
    else:
        x = i - 4
    y = 7 - 2 * x
    print(" " * x + "*" * y + " " * x)

#------------------------------------------------

line = int(input("Please enter an odd number: "))
for i in range(-line//2,line//2+1):
    if i < 0:
        print(" "*(-i)+"*"*(line+2*i))
    if i >= 0:
        print(" "*i+"*"*(line-2*i))
 
#------------------------------------------------

n = int(input("Please enter a number: "))
if not n%2:
    n += 1
e = -(n//2)
for i in range(e,n+e):
    print(" "*abs(i)+"*"*(n-2*abs(i))) 
    
#------------------------------------------------

for i in range(-3,4):
    print(" "*abs(i)+"*"*(7-2*abs(i)))
