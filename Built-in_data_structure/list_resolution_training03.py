# 打印九九乘法表
# 示例：(Wayne)
[print("{}*{}={:<3}{}".format(j, i, j*i,  '\n' if i==j else ' '),end="") for i in range(1,10) for j in range(1,i+1)]


# 示例2：(其他)
[print('{}*{}={:<{}} {}'.format(i, j, i*j, 1 if i == 1 else 2, '\n' if i == j else ''), end = '') for j in range(1, 10) for i in range(1, j+1)]


print("".join(['{}*{}={:<3}{}'.format(j, i, j*i, '\n' if j == i else '') for i in range(1, 10) for j in range(1, i+1)]))
