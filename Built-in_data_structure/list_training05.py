# 求杨辉三角的第m行第k个元素
# 第m行有m项,m是正整数,因此k一定不会大于m
# 第n行的m个数可表示为C(n-1, m-1),即为从n-1个不同元素中取m-1个元素的组合数

# 算法1
# 计算到m行,打印出k项

# 求m行k个元素
# m行元素有m个,所以k不能大于m
# 这个需求需要保存m行的数据,那么可以使用一个嵌套机构[[],[],[]]

m = 5
k = 4
triangle = []
for i in range(m):
    # 所有行都需要1开头
    row = [1]
    triangle.append(row)
    if i == 0:
        continue
    for j in range(1, i):
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)
print(triangle)
print("---------")
print(triangle[m-1][k-1])
print("---------")


#-------------------------------------------------------------------------------

# 算法2
# 根据杨辉三角的定理：第n行的m个数(m>0且n>0)可表示为C(n-1, m-1),
# 即为从n-1个不同元素中取m-1个元素的组合数
# 组合数公式：有m个不同元素,任意取n(n≤m)个元素,记作C(m,n),组合数公式为：
# 	C(m,n)=m!/(n!(m - n)!)

# m行k列的值,C(m-1,k-1)组合数
m = 9
k = 5
# c(n,r) = c(m-1,k-1) = (m-1)!/((k-1)!(m-r)!)
# m 最大
n = m - 1
r = k - 1
d = n - r 
targets = []    # r, n-r, n
factorial = 1
# 可以加入k为1或者m的判断,返回1
for i in range(1, n+1):
    factorial *= i
    if i == r:
        targets.append(factorial)
    if i == d:
        targets.append(factorial)
    if i == n:
        targets.append(factorial)
#print(targets)
print(targets[2]//(targets[0]*targets[1]))


# i==r、i==n、i==d 这三个条件不要写在一起,因为它们有可能两两相等
# 算法说明：一趟到n的阶乘算出所有阶乘值


