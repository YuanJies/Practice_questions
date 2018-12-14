# 计算杨辉三角前6行
# 第n行有n项,n是正整数
# 第n行数字之和为2的n-1次方
# 只要求打印杨辉三角的数字即可

# 基础实现（方法1）
# 示例：下一行依赖上一行所有元素,是上一行所有元素的两两相加的和,再在两头各加1
# 第一行和第二行是特例
# 预先构建前两行,从而推导出后面的所有行
triangle = [[1], [1,1]]
n = 6
for i in range(2, n):    
    newline = [1]    #新行及第一个元素
    pre = triangle[i-1]
    # 1 2 1
    for j in range(i-1):
        val = pre[j] + pre[j+1]
        newline.append(val)
        
    newline.append(1)    #最后一个元素（尾巴）
    triangle.append(newline)
print(triangle)


--------------------------------------------------------
# 同上
triangle = [[1], [1,1]]
for i in range(2,6):
    cur = [1]
    pre = triangle[i-1]
    for j in range(len(pre)-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)


--------------------------------------------------------

n = 6
print([1])
pre = [1, 1]
print(pre)

for i in range(2, n):
    newline = [1]
    
    for j in range(i-1):
        val = pre[j] + pre[j+1]
        newline.append(val)
        
    newline.append(1)
    print(newline)
    pre = newline


--------------------------------------------------------

# 从第一行开始
triangle = []
n = 6
for i in range(n):
    cur = [1]
    triangle.append(cur)
    
    if i == 0:
        continue
    
    pre = triangle[i-1]
    for j in range(len(pre)-1):
        cur.append(pre[j] + pre[j+1])
    cur.append(1)
print(triangle)


--------------------------------------------------------
n = 6

for i in range(n):
    newline = [1]
    if i == 0:
        print(newline)
        continue
    for j in range(i-1):
        val = pre[j] + pre[j+1]
        newline.append(val)
        
    newline.append(1)
    print(newline)
    pre = newline
    
    
--------------------------------------------------------

# 补零（方法2）
# 除了第一行以外,每一行每一个元素(包括两头的1)都是由上一行的元素相加得到。如何得到两头的1呢？
# 通过每一行的两头加0得到两头的1
# 目标是打印指定的行,所以算出一行就打印一行,不需要用一个大空间存储所有已经算出的行

# 每一行的两头补0
n = 6
pre = [1]
print(pre)
#pre = [0, 1, 0]    #insert append , extend 0 1 0
pre.insert(0, 0)
pre.append(0)

for i in range(1, n):
    newline = []
    
    for j in range(i+1):
        val = pre[j] + pre[j+1]
        newline.append(val)
        
    print(newline)
    pre = newline
    pre.insert(0, 0)
    pre.append(0)


--------------------------------------------------------

# 只在每一行的尾部补0
n = 6
pre = [1]
print(pre)
pre.append(0)

for i in range(1, n):
    newline = []
    
    for j in range(i+1):
        val = pre[j-1] + pre[j]
        newline.append(val)
        
    print(newline)
    pre = newline
    pre.append(0)
    
    
# while循环实现
n = 6
newline = [1]    # 相当于计算好的第一行
print(newline)

for i in range(1, n):
    oldline = newline.copy()    # 浅拷贝并补0
    oldline.append(0)    # 尾部补0相当于两端补0
    newline.clear()    # 使用append，所以要清除
    
    offset = 0
    while offset <= i:
        newline.append(oldline[offset-1] + oldline[offset])
        offset += 1
    print(newline)



# for循环实现
n = 6
newline = [1]    # 相当于计算好的第一行
print(newline)

for i in range(1, n):
    oldline = newline.copy()    # 浅拷贝并补0
    oldline.append(0)    # 尾部补0相当于两端补0
    newline.clear()    # 使用append，所以要清除
    
    for j in range(i+1):
        newline.append(oldline[j - 1] + oldline[j])
    print(newline)


--------------------------------------------------------

# 对称性（方法3）
# 一次性开辟每一行空间,可以使用
#    列表解析式
#    循环迭代
#    *,乘法：效率最高,减少每一次追加元素扩展带来的性能损耗
# 少算一半的数字（对称性）

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]

# 把整个杨辉三角看成左对齐的二维矩阵
# i==2时,在第3行,中点的列表索引j==1
# i==3时,在第4行,无中点
# i==4时,在第5行,中点的列表索引j==2
# 得到以下规律,如果有i==2*j,则有中点

triangle = []
n = 6
for i in range(n):
    row = [1]    # 开始的1
    for k in range(i):    # 中间填0,尾部填1
        row.append(1) if k == i-1 else row.append(0)
    triangle.append(row)
    if i == 0:
        continue
    for j in range(1, i//2+1):    # i=2第三行才能进来
        #print(i, j)
        val = triangle[i - 1][j-1] + triangle[i - 1][j]
        row[j] = val
        # i为2，j为0 1 2，循环1次
        # i为3，j为0 1 2 3，循环1次
        # i为4，j为0 1 2 3 4，循环2次
        if i != 2*j:    # 奇数个数的中点跳过
            row[-j-1] = val
print(triangle)


# 简化上面代码
triangle = []
n = 6
for i in range(n):
    row = [1] * (i+1)    # 一次性开辟
    triangle.append(row)
    for j in range(1, i//2+1):    # i=2第三行才能进来
        #print(i, j)
        val = triangle[i - 1][j-1] + triangle[i - 1][j]
        row[j] = val
        if i != 2*j:    # 奇数个数的中点跳过
            row[-j-1] = val
print(triangle)


--------------------------------------------------------

# 单行覆盖(方法4)
# 用上对称性
# 方法3中为每一行都开辟空间,是否一次性开辟足够空间,只开辟一行重复利用
# 首先明确的知道所求最大行的元素个数,例如前6行的最大行元素个数为6个。
# 下一行等于首元素不变,覆盖中间元素

n = 6
row = [1] * n    # 一次性开辟足够的空间

for i in range(n):
    offset = n - i
    z = 1    # 因为会有覆盖影响计算，所以引用一个临时变量
    for j in range(1, i//2+1):    # 对称性
        val = z + row[j]
        row[j], z = val, row[j]
        if i != 2*j:
            row[-j-offset] = val
    print(row[:i+1])
