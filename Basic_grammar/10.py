# 打印100以内的斐波那契数列
print(0)
print(1)
a = 0
b = 1
while True:
    c = a + b
    if c > 100:
        break
    a = b
    b = c
    print(c)
    
#----------------------------

a = 1
b = 1
print(a)
print(b)
for i in range(2,101):
    if i == a+b:
        print(i)
        a = b
        b = i
        
#----------------------------

a = 0
b = 1
c = 0
print(a,b,sep="\n")
while c<100:
    c=a+b
    if c>100:
        break
    print(c)
    a=b
    b=c
   
#----------------------------   
   
a = 1
b = 1
while b<100:
    print(b)
    a, b = b, a+b #a=b,b=a+b
