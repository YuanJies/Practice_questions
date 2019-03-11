# 求2个字符串的最长公共子串
# 方法一：矩阵算法

s1 = 'abcdefg'
s2 = 'defabcd'
s2 ='defabcdoabcdeftw'
s3 = '1234a'
s4 = "5678"
s5 = 'abcdd'

def findit(str1, str2):
    matrix = []
    # 从x轴或者y轴取都可以,选择x轴, xmax和xindex
    xmax = 0
    xindex = 0
    for i, x in enumerate(str2):
        matrix.append([])
        for j, y in enumerate(str1):
            if x != y:    # 若两个字符不相等
                matrix[i].append(0)
            else:
                if i == 0 or j == 0:    # 两个字符相等,有字符在边上的
                    matrix[i].append(1)
                else:    # 不在边上
                    matrix[i].append(matrix[i - 1][j - 1] + 1)

                if matrix[i][j] > xmax:    # 判断当前加入的值和记录的最大值比较
                    xmax = matrix[i][j]    # 记录最大值,用于下次比较
                    xindex = j    # 记录当前值的x轴偏移量,和str1[xindex+1-xmax:xindex+1]匹配
                    xindex += 1    # 只是为了计算的需求才+1,和str1[xindex-xmax:xindex]匹配

    # return str1[xindex+1-xmax:xindex+1]
    return str1[xindex - xmax: xindex]

print(findit(s1, s2))
print(findit(s1, s3))    # a
print(findit(s1, s4))    # 空串
print(findit(s1, s5))    # abcd
s1 = ' abcdefg'
s5 = '304abcdd'
print(findit(s1, s5))    # abcd


#-------------------------------------------------------------------------------------------------
# 方法二：

s1 = 'abcdefg'
s2 = 'defabcdoabcdeftw'
s3 = '1234a'

def findit(str1, str2):
    count = 0    # 看看效率,计数
    length = len(str1)

    for sublen in range(length, 0 , -1):
        for start in range(0, length - sublen + 1):
            substr = str1[start:start + sublen]
            count += 1
            if str2.find(substr) > -1:    # found
                print("count={}, substrlen={}".format(count, sublen))
                return substr

print(findit(s1, s2))
print(findit(s1, s3))
