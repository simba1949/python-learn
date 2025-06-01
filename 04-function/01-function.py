# 定义函数
def my_function():
	print("这是函数")


# 调用函数之前必须保证函数已经存在
my_function()


# 函数的返回值
# 返回值的三种情况总结
# 1.函数没有返回值，返回值为None
# 2.函数只有一个返回值， 返回值就是函数的返回值
# 3.函数有多个返回值， 返回值是一个元组
# 无返回值
def hello_fun():
	print("hello world")


print("hello_fun() 执行结果：", hello_fun(), "结果类型", type(hello_fun()))


# 仅有一个返回值
def add_fun(a, b):
	return a + b


print("add_fun(a, b) 执行结果：", add_fun(1, 2), "结果类型", type(hello_fun()))


# 多个返回值
def add_sub_fun2(a, b):
	return a + b, a - b


print("add_sub_fun2(a, b) 执行结果：", add_sub_fun2(1, 2), "结果类型", type(add_sub_fun2(1, 2)))


# 参数
# 必备参数，函数调用时必须提供
def add_fun1(a, b):
	print("add_fun1(a, b) 函数被调用，形参：", a, b, "形参类型：", type(a), type(b))
	return a + b


print("add_fun1(a, b) 执行结果：%d" % add_fun1(1, 2))


# 可选参数，设置默认值的参数，函数调用时可以不提供
def add_fun2(a, b=0):
	print("add_fun2(a, b=0) 函数被调用，形参：", a, b, "形参类型：", type(a), type(b))
	return a + b


print("add_fun2(a, b=0) 执行结果：%d" % add_fun2(1, 2))


# 可变参数，*args 以元组的形式接收
def add_fun3(*args):
	print("add_fun3(*args) 函数被调用，形参：", args, "形参类型：", type(args))
	return sum(args)


print("add_fun3(*args) 执行结果：%d" % add_fun3(1, 2, 3))


# 关键字参数，**kwargs 以字典的形式接收
def add_fun4(**kwargs):
	print("add_fun4(**kwargs) 函数被调用，形参：", kwargs, "形参类型：", type(kwargs))
	return kwargs


print("add_fun4(**kwargs) 执行结果：%s" % add_fun4(a=1, b=2))


# 函数的嵌套，函数可以嵌套定义，函数也可以嵌套调用，注意不要在内层函数调用外层函数的参数
def add_fun5(a, b):
	def add_fun6(c, d):
		return c + d  # 两个数相加

	return add_fun6(a, b)


print("add_fun5 执行结果：%d" % add_fun5(1, 2))
