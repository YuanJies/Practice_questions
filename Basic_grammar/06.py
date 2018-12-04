# 打印九九乘法表
for i in range(1,10):
    for x in range(1,i+1):
        print(str(x) + "*" + str(i) + "=" + str(i * x),end=" ")
    print()
