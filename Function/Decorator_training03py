# 实现Base64解码函数

alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64decode(src:bytes):
    ret = bytearray()
    length = len(src)

    step = 4    # 对齐的,每次取4个
    for offset in range(0, length, step):
        tmp = 0x00
        block = src[offset:offset + step]

        # 开始移位计算
        for i, c in enumerate(reversed(block)):
            # 替换字符为序号
            index = alphabet.find(c)
            if index == -1:
                continue # 找不到就是0,不用移位相加了
            tmp += index << i*6

        ret.extend(tmp.to_bytes(3, 'big'))
    return bytes(ret.rstrip(b'\x00'))    # 把最右边的\00去掉,不可变

# base64的decode
txt = "TWFu"
txt = "TWE="
txt = "TQ=="
txt = "TWFuTWE="
txt = "TWFuTQ=="
txt = txt.encode()

print(txt)

print(base64decode(txt).decode())


# base64实现
import base64
print(base64.b64decode(txt).decode())


#----------------------------------------------------------------------------
# 改进
# 	1、reversed可以不需要
# 	2、alphabet.find效率低


from collections import OrderedDict

base_tb1 = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
alphabet = OrderedDict(zip(base_tb1, range(64)))    # 用有序字典记录顺序和查询提升效率

def base64decode(src:bytes):
    ret = bytearray()
    length =len(src)

    step = 4    # 对齐的,每次取4个
    for offset in range(0, length, step):
        tmp = 0x00
        block = src[offset:offset + step]

        # 开始移位计算
        for i in range(4):
            index = alphabet.get(block[-i-1])
            if index is not None:
                tmp += index << i*6
            # 找不到,不用移位相加了

        ret.extend(tmp.to_bytes(3, 'big'))
    return bytes(ret.rstrip(b'\x00'))    # 把最右边的\x00去掉,不可变

# base64的decode
txt = "TWFu"
#txt = "TWE="
#txt = "TQ=="
#txt = "TWFuTWE="
#txt = "TWFuTQ=="
txt = txt.encode()
print(txt)

print(base64decode(txt).decode())


# base64实现
import base64
print(base64.b64decode(txt).decode())
