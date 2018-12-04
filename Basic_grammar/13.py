# 给一个半径,求圆的面积和周长。圆周率3.14
# 圆周长=圆周率×直径
# 圆面积＝圆周率×半径的平方
r = int(input("Please enter a radius: "))
print("area=" + str(3.14 * r * r))
print("circumference=" + str(2 * 3.14 * r))




# 输入两个数,比较大小后,从小到大升序打印
number_1 = int(input("first"))
number_2 = int(input("second"))
if number_1 > number_2:
    print(number_2,number_1)
else:
    print(number_1,number_2)
    
#-------------------------------------------------------------------------------

number_1 = int(input("first"))
number_2 = int(input("second"))
print(number_2,number_1) if number_1 > number_2 else print(number_1,number_2)
