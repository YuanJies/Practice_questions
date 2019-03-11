# 写一个命令分发器
# 程序员可以方便的注册函数到某一个命令,用户输入命令时,路由到注册的函数
# 如果此命令没有对应的注册函数,执行默认函数
# 用户输入用 input(">>")

# 分析
# 输入一个命令映射到一个函数,并执行这个函数。应该是cmd_tbl[cmd] = fn的形式,字典正好合适。
# 如果输入了某一个cmd命令后,没有找到函数,就要调用缺省的函数执行,这正好是字典缺省参数。

def command_dispatcher():
    # 构建全局字典
    cmd_tbl = {}

    # 注册函数
    def reg(cmd):
        def _reg(fn):
            cmd_tbl[cmd] = fn
            return fn
        return _reg

    # 缺省函数
    def default_func():
        print("Unknown command")

    # 调度器
    def dispatcher():
        while True:
            cmd = input(">>>>")
            if cmd.strip() == '':
                return
            cmd_tbl.get(cmd, default_func)()

    return reg, dispatcher

reg, dispatcher = command_dispatcher()


# 自定义函数
@reg('yj')
def foo1():
    print('yuanjie')

@reg('py')
def foo2():
    print('python')

# 调度循环
dispatcher()
