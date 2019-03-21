# 完善命令分发器
# 	要求函数可以带参数(不考虑可变参数、keyword-only参数)
# 	用户输入命令,执行相应的函数


# 即解决下面的问题
# 自定义函数
# @reg('mag')
# def foo1(x, y):
#     print('magedu', x, y)
#
# @reg('py')
# def foo2(a, b=100):
#     print('python', a, b)


# 思路：
# 可以有2种方式
# 	1、注册的时候,固定死, @reg('py', 200, 100)
# 	可以认为@reg('py', 200, 100)和@reg('py', 300, 100)是不同的函数,可以用partial函数。
# 	2、运行时,在输入cmd的时候,逗号分割,获取参数。
# 	至于函数的验证,以后实现。
# 	一般用户都喜欢使用单纯一个命令如mag,然后直接显示想要的结果,所以采用第一种方式


from functools import partial

# 自定义函数可以有任意参数,可变参数、keyword-onl除外
def command_dispatcher():
    # 构建全局字典
    cmd_tb1 = {}

    # 注册函数
    def reg(cmd, *args, **kwargs):
        def _reg(fn):
            func = partial(fn, *args, **kwargs)
            cmd_tb1[cmd] = func
            return func
        return _reg

    # 缺省函数
    def default_func():
        print('Unknown command')

    # 调度器
    def dispatcher():
        while True:
            cmd = input('Please input cmd>>')
            # 退出条件
            if cmd.strip() == '':
                return
            cmd_tb1.get(cmd, default_func)()

    return reg, dispatcher

reg, dispatcher = command_dispatcher()

# 自定义函数
@reg('mag', z=200, y=300, x=100)
def foo1(x, y, z):
    print('magedu', x, y, z)

@reg('py', 300, b=400)
def foo2(a, b=100):
    print('python', a, b)

# 调度循环
dispatcher()
