# 打印闪电
#   *
#  **
# ***
#*******
#   ***
#   **
#   *
for i in range(-3,4):
    if i<0:
        print(" "*(-i) + "*"*(4+i))
    elif i>0:
        print(" "*3 + "*"*(4-i))
    else:
        print("*"*7)
