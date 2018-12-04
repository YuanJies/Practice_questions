# 打印九九乘法表
for i in range(1,10):
    s = " "
    for j in range(1,10):
        if j < i + 1:
            s += str(j) + '*' + str(i) + '=' + str(i * j) + ' '
    print(s)

#-------------------------------------------------------------------

for i in range(1,10):
    for x in range(1,i+1):
        print(str(x) + "*" + str(i) + "=" + str(i * x),end=" ")
    print()

#-------------------------------------------------------------------

for i in range(1,10):
    for x in range(1,i+1):
        print(x,"*",i,"=",x*i,end='\t')
    print()
    
#-------------------------------------------------------------------

for i in range(1,10):
    line = ' '
    for j in range(1,i+1):
        line += '{0}*{1}={2} '.format(j,i,i*j)
    print(line)

#-------------------------------------------------------------------

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,i*j),end=" ")
    print()

   


# 打印九九乘法表方阵上边部分（右上角）
for i in range(1,10):
    print(" "*7*(i-1),end="")
    for j in range(i,10):
        product = i*j
        if product < 10:
            end = "  "
        else:
            end = " "
        print(str(i)+"*"+str(j)+"="+str(i*j),end=end)
    print()
    
#-------------------------------------------------------------------

for i in range(1,10):
    s = " "
    for j in range(i,10):
        s += "{}*{}={:<3} ".format(i,j,i*j)
    print("{:>80}".format(s))
    
#-------------------------------------------------------------------

for i in range(1,10):
    s = " "
    for j in range(i,10):
        s += "{}*{}={:<{}} ".format(i,j,i*j, 2 if j<4 else 3)
    print("{:>80}".format(s))
    
