# 把一个字典扁平化
# 源字典 {'a':{'b':1,'c':2}, 'd':{'e':3,'f':{'g':4}}}
# 目标字典 {'ac':2,'de':3,'dfg':4,'ab':1}

source = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}
target = {}
# recursion
def flatmap(src, prefix=''):
    for k, v in src.items():
        if isinstance(v, (list, tuple, set, dict)):
            flatmap(v, prefix=prefix+k+'.')    # 递归调用
        else:
            target[prefix+k] = v

flatmap(source)
print(target)


#---------------------------------------------------------------------
# 一般这种函数都会生成一个新的字典,因此改造一下
# dest字典可以由内部创建,也可以有外部提供
source = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}

# recursion
def flatmap(src, dest=None, prefix=''):
    if dest == None:
        dest = {}
    for k, v in src.items():
        if isinstance(v, (list, tuple, set, dict)):
            flatmap(v, dest, prefix=prefix+k+'.')    # 递归调用
        else:
            dest[prefix+k] = v
    return dest

print(flatmap(source))


#---------------------------------------------------------------------
# 不暴露给外界内部的字典
source = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}

# recursion
def flatmap(src):
    def _flatmap(src, dest=None, prefix=''):
        for k, v in src.items():
            key = prefix + k
            if isinstance(v, (list, tuple, set, dict)):
                _flatmap(v, dest, key + '.')    # 递归调用
            else:
                dest[key] = v
    dest = {}
    _flatmap(src, dest)
    return dest

print(flatmap(source))
