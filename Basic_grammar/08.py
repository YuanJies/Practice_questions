# 打印对顶三角形
#*******
# *****
#  ***
#   *
#  ***
# *****
#*******
n = 7
e = n//2
for i in range(-e,n-e):
    prespace = -i if i<0 else i
    print(" "*(e-prespace)+ "*"*(2*prespace+1))
    
#------------------------------------------------------

a = int(input("Please enter a number: "))
for i in range(-a,a+1):
    if i < 0:
        i = -i
    print(" "*(a-i)+"*"*(2*i+1)+" "*(a-i))
