# 给定一个3*3方阵,求其转置矩阵
# 有一个方阵,左边方阵,求其转置矩阵
# 1 2 3        1 4 7
# 4 5 6  --->  2 5 8
# 7 8 9        3 6 9

# 规律：对角线不动,a[i][j] ---> a[j][i],而且到了对角线,就停止,去做下一行,对角线上的元素不动
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
count = 0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            count += 1
print(matrix)
print(count)


#------------------------------------------------

matrix = [[1,2,3],[4,5,6],[7,8,9]]
length = len(matrix)
count = 0
for i in range(length):
    for j in range(i):    # j<i
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        count += 1
print(matrix)
print(count)


#------------------------------------------------

matrix = '1 2 3\n4 5 6\n7 8 9'
print(matrix + '\n')
length_column = len(matrix.split('\n'))
matrix = matrix.split()
length_row = len(matrix)  // length_column
print(matrix)

for i in range(length_row):
    for j in range(length_column):
        print(matrix[j * 3 + i], end=' ')
    print('\r')
    
    
#------------------------------------------------

list1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(list1)):
    for p in range(len(list1[0])):
        print(list1[i][p],end = ' ')
    print()
print('-'*10)
for i in range(len(list1[0])):
    for p in range(len(list1)):
        print(list1[p][i], end = ' ')
    print()
    
    
#------------------------------------------------

lst1 = [[1,2,3],[4,5,6],[7,8,9]]
for x in range(len(lst1)):
    for y in range(len(lst1[x])):
        if y > x:
            lst1[x][y], lst1[y][x] = lst1[y][x], lst1[x][y]
    print(lst1[x])
#print(lst1)


#------------------------------------------------

m = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    for j in range(i):
        m[i][j], m[j][i] = m[j][i], m[i][j]
print(m)


