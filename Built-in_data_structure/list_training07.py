# 给定一个矩阵,求其转置矩阵
# 1 2 3        1 4
# 4 5 6  --->  2 5
#              3 6

# 这样一个矩阵,但不是方阵

# 算法1
# 过程就是,扫描matrix第一行,在tm的第一列从上至下附加,然后再第二列附加
# 举例：扫描第一行1,2,3、加入到tm的第一列,然后扫描第二行4,5,6、追加到tm的第二列

matrix = [[1,2,3], [4,5,6]]
#matrix = [[1,4],[2,5],[3,6]]

tm = []
count = 0
for row in matrix:
    for i, col in enumerate(row):
        if len(tm) < i + 1:    # matrix有i列就要为tm创建i行
            tm.append([])

        tm[i].append(col)
        count += 1

print(matrix)
print(tm)
print(count)


#------------------------------------------------------------------
# 算法2
# 思考：
#	 能否一次性开辟目标矩阵的内存空间？
#	 如果一次性开辟好目标矩阵内存空间,那么原矩阵的元素直接移动到转置矩阵的对称坐标就行了
#  在原有的矩阵上改动,牵制到增加元素和减少元素,麻烦,所以,定义一个新的矩阵输出

matrix = [[1,2,3], [4,5,6]]
#matrix = [[1,4],[2,5],[3,6]]

tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]
count = 0

for i, row in enumerate(tm):
    for j, col in enumerate(row):
        tm[i][j] = matrix[j][i]    # 将matrix的所有元素搬到tm中
        count += 1

print(matrix)
print(tm)
print(count)


