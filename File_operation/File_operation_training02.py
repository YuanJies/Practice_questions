# 有一个文件, 对其进行单词统计, 不区分大小写, 并显示单词重复最多的10个单词
# 简单处理后, 大概的得数如下：
# the、136
# is 、60
# a、54
# path、52
# if 、42
# and 、39
# to、34
# of、33
# on、32
# return、30

# 简单处理示例：（Wayne）
d = {}
with open('sample.txt', encoding='utf8') as f:
    for line in f:
        words = line.split()
        for word in map(str.lower, words):
            d[word] = d.get(word, 0) + 1

print(sorted(d.items(), key=lambda item: item[1], reverse=True))

# 这里帮助文档中path的文档,path应该很多

# for k in d.keys():
#     if k.find('path') > -1:
#         print(k)

# 使用上面的代码, 就可以看到path非常多
# os.path.exists(path)
# 可以认为含有2个path


# 实际上有效的path很多, 作为合法的单词path统计应该有100多个。
# 对单词做进一步处理后, 统计如下：
# path、137
# the、136
# is 、60
# a、59
# os、50
# if 、43
# and 、40
# to、34
# of、33
# on、33


# 对单词做进一步处理后
# 示例：（Wayne）

def makekey(s: str):
    chars = set(r"""!'"#./\()[],*-""")
    key = s.lower()
    ret = []
    for i, c in enumerate(key):
        if c in chars:
            ret.append(' ')
        else:
            ret.append(c)
    return ''.join(ret).split()


d = {}
with open('sample.txt', encoding='utf8') as f:
    for line in f:
        words = line.split()
        for wordlist in map(makekey, words):
            for word in wordlist:
                d[word] = d.get(word, 0) + 1

for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True):
    print(k, v)
