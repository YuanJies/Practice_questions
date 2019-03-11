# 实现一个cache装饰器,实现可过期被清除的功能
# 简化设计,函数的形参定义不包含可变位置参数、可变关键字参数和keyword-only参数
# 可以不考虑缓存满了之后的换出问题

# 示例：（Wayne）
import time
import inspect
from functools import wraps
import datetime

def mag_cache(duration):
    def _cache(fn):
        local_cache = {}    # 对不同函数名是不同的cache

        @wraps(fn)
        def wrapper(*args, **kwargs):    # 接收各种参数,kwargs普通字典参数无序
            # 清除过期的key
            expire_keys = []
            for k, (_, stamp) in local_cache.items():
                now = datetime.datetime.now().timestamp()
                if now - stamp > duration:
                    expire_keys.append(k)
            for k in expire_keys:
                local_cache.pop(k)

            # 参数处理,构建key
            sig = inspect.signature(fn)
            params = sig.parameters    # 只读有序字典

            param_names = [key for key in params.keys()]
            params_dict = {}

            for i, v in enumerate(args):
                k = param_names[i]
                params_dict[k] = v

            #for k, v in kwargs.items():
                #params_dict[k] = v
            params_dict.update(kwargs)

            # 缺省值处理
            for k, v in params.items():
                if k not in params_dict.keys():
                    params_dict[k] = v.default

            key = tuple(sorted(params_dict.items()))

            # 判断是否需要缓存
            if key not in local_cache.keys():
                local_cache[key] = (fn(*args, **kwargs), datetime.datetime.now().timestamp())    # 时间戳


            return key, local_cache[key]

        return wrapper
    return _cache

def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)
        return ret
    return wrapper

@logger
@mag_cache(10)
def add(x, z, y=6):
    time.sleep(3)
    return x + y + z

result = []
result.append(add(4, 5))
result.append(add(4, z=5))
result.append(add(4, y=6, z=5))
result.append(add(y=6, z=5, x= 4))
result.append(add(4, 5, 6))
result.append(add(4, 6))

for x in result:
    print(x)

time.sleep(10)
result = []
result.append(add(4, 5))
result.append(add(4, z=5))
result.append(add(4, y=6, z=5))
result.append(add(4, 6))
