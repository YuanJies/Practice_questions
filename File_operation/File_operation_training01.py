# 指定一个源文件,实现copy到目标目录。
# 例如把/tmp/test.txt 拷贝到 /tmp/test1.txt
#
# 示例：（Wayne）
filename1 = 'test'
filename2 = 'test1'


f = open(filename1, 'w+')
lines = ['abc', '123', 'yuanjie']
f.writelines('\n'.join(lines))
f.seek(0)
print(f.read())
f.close()


def copy(src, dest):
    with open(src) as f1:
        with open(dest, 'w') as f2:
            f2.write(f1.read())


copy(filename1, filename2)
