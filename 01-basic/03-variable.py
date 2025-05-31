# 变量
# 定义变量
name = "anthony"
print(name)


#  局部变量
def func():
    local_var = 10  # 仅在func内部可访问
    print("局部变量", local_var)
    func()


# 全局变量
global_var = 10
print("全局变量", global_var)


def outer():
    x = 10
    print("outer,x=", x)

    def inner():
        nonlocal x
        x = 20  # 修改外层变量x
        print("inner,x=", x)
        inner()

    outer()
