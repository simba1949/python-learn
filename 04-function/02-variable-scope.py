# 变量作用域是指变量的可访问范围
# 1.全局变量： 在函数外定义的变量
# 2.局部变量： 在函数内定义的变量
#  局部变量
def fun():
	local_var = 10  # 仅在 fun 内部可访问
	print("局部变量", local_var)
	fun()


# 全局变量
global_val = 10
print("全局变量", global_val)

# 重新赋值全局变量
global_val = 0


def outer_fun():
	local_val = 10

	def inner_fun():
		nonlocal local_val  # 修改外层变量
		print("修改前 inner_fun, local_val=", local_val)
		local_val = 20  # 修改外层变量 local_val
		print("修改后 inner_fun, local_val=", local_val)

	print("调用前 inner_fun, local_val=", local_val)
	inner_fun()
	print("调用后 inner_fun, local_val=", local_val)

	# 重新赋值全局变量
	global global_val
	print("修改前 outer_fun, global_val=", global_val)
	global_val = 20
	print("修改后 outer_fun, global_val=", global_val)


print("调用前 outer_fun, global_val=", global_val)
outer_fun()
print("调用后 outer_fun, global_val=", global_val)
