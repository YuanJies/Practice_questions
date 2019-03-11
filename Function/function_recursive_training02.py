# 将一个数逆序放入列表中,例如1234 ---> [4, 3, 2, 1]
# 示例：（Wayne）

data = str(1234)

def revert(x):
    if x == -1:
        return ''
    return data[x] + revert(x-1)

print(revert(len(data)-1))


#-----------------------------------------------------------------
def revert(n, lst=None):
    if lst is None:
        lst = []

    x, y = divmod(n ,10)
    lst.append(y)
    if x == 0:
        return lst
    return revert(x, lst)

print(revert(12345))


#-----------------------------------------------------------------
num = 1234

def revert(num, target=[]):
    if num:
        target.append(num[len(num)-1])    # target.append(num[-1:])
        revert(num[:len(num)-1])
    return target

print(revert(str(num)))


#-----------------------------------------------------------------
示例：（其他）

def reverse(n, lst=None):
    if lst is None:
        lst = []

    lst.append(n%10)
    if n // 10 == 0:
        return lst
    return reverse(n//10, lst)

print(reverse(1234))
