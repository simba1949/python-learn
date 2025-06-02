# 闭包
# 闭包条件
# 1. 函数嵌套（函数里面再定义函数）
# 2. 内部函数引用外部函数的变量
# 3. 函数返回内部函数
def outer_fun():
	local_var = 10  # 仅在 outer_fun 内部可访问

	def inner_fun():
		print("调用内部函数，%d" % local_var)
		return local_var

	return inner_fun  # 返回内部函数的引用


# 第一种调用方法
# 返回内部函数的引用
print(outer_fun())
#  调用内部函数
print(outer_fun()())
# 第二种调用方法
inner_fun = outer_fun()  # 返回内部函数的引用
print(inner_fun())  # 调用内部函数
