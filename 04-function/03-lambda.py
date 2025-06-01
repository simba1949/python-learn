# lambda 表达式
# 基本语法：lambda 参数列表: 函数体

# 无参
hello_fun = lambda: "hello"
print(hello_fun())

# 一个参数
say_hello_fun = lambda name: "hello, %s" % name
print(say_hello_fun("anthony"))

# 默认参数，默认参数必须放在非默认参数后面
say_hello_fun = lambda name="World": "hello, %s" % name
print(say_hello_fun())

# 多个参数，多个参数用逗号隔开
add_fun = lambda a, b: a + b
print(add_fun(1, 2))

# 可变参数
add_fun = lambda *args: sum(args)
print(add_fun(1, 2, 3, 4, 5))

#  关键字参数
add_fun = lambda **kwargs: sum(kwargs.values())
print(add_fun(a=1, b=2, c=3, d=4, e=5))
