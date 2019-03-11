# 编写一个函数，接受一个参数n，n为正整数，左右两种打印方式。要求数字必须对齐
# 上三角

示例：（Wayne）
def show(n):
    tail = " ".join([str(i) for i in range(n, 0, -1)])
    width = len(tail)
    for i in range(1, n):
        print("{:>{}}".format(" ".join([str(j) for j in range(i, 0, -1)]), width))
    print(tail)

show(12)


示例：（其他）
def show(n):
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if i < j:
                print(' '*len(str(j)), end=' ')
            else:
                print(j, end=' ')
        print()

show(12)


# 下三角

# 示例：（Wayne）
def showtail(n):
    tail = " ".join([str(i) for i in range(n, 0, -1)])
    print(tail)
    # 无需再次生成列表
    for i in range(len(tail)):
        if tail[i] == ' ':
            print(' '*i, tail[i+1:])

showtail(12)
