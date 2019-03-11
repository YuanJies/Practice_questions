# 实现Base64编码
alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

teststr = "abcd"
teststr = "ManMa"

def base64(src):
    ret = bytearray()
    length = len(src)
    # r记录补0的个数
    r = 0
    for offset in range(0, length, 3):
        if offset + 3 <= length:
            triple = src[offset:offset + 3]
        else:
            triple = src[offset:]
            r = 3 - len(triple)
            triple = triple + '\x00'*r    # 补几个0

        #print(triple, r)
        # 将3个字节看成一个整体转成字节bytes,大端模式
        # abc --> 0x616263
        b = int.from_bytes(triple.encode(), 'big')    # 小端模式为'little'
        print(hex(b))

        # 0110000101100010 01100011    # abc
        # 011000 010110 001001 100011    # 每6位断开
        for i in range(18, -1, -6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F    # 0b0011 1111
            ret.append(alphabet[index])    # 得到base64编码的列表
        # 策略是不管是不是补零,都填满,只有最后一次可能出现补零的
        # 在最后替换掉就是了,代码清晰,而且替换至多2次
        # 在上一个循环中判断 r!=0,效率可能会高些
        for i in range(1, r+1):    # 1到r,补几个0替换几个=
            ret[-i] = 0x3D
    return ret
print(base64(teststr))


# base64实现
import base64
print(base64.b64encode(teststr.encode()))
