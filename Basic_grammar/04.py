# 5！+ 4！+ 3！+ 2！+ 1！之和
# 求1到5的阶乘之和（153）
a = 1
sum = 0
for i in range(1,6):
    a *= i
    sum += a
print(sum)
