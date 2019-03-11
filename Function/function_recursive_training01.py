# 求n的阶乘

def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

n = 5
print(fac(n))


#---------------------------------------------------

def fac1(n, p=1):
    if n == 1:
        return p
    p *= n
    print(p)
    fac1(n-1, p)
    return p

n = 5
print(fac1(n))


#---------------------------------------------------

def fac2(n, p=None):
    if p is None:
        p = [1]
    if n == 1:
        return p[0]
    p[0] *= n
    print(p[0])
    fac2(n-1, p)
    return p

n = 5
print(fac2(n))


# fac函数性能最好,因为时间复杂度是相同的,fac最简单
#---------------------------------------------------

def fac(n, m=1):
    m *= n
    if n == 1:
        return m
    return fac(n-1, m)

print(fac(5))
