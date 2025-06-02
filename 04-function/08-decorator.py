# 装饰器
# 函数作为参数传递给另一个函数
# 定义被装饰的函数
def print_fun():
	print('start')
	print('end')


# 定义装饰器
def new_print_fun(fn):
	print('new_print_fun start')
	fn()  # 调用被装饰的函数
	print('new_print_fun end')


# 调用装饰器
new_print_fun(print_fun)
print('------------------------------------------------------')


# 标准版装饰器
# 定义被装饰的函数
def send_message(*args, **kwargs):
	print('send_message start', args, kwargs)


# 定义装饰器
def wrapper_fun(fn):
	def inner_fun(*args, **kwargs):
		# 执行被装饰函数之前的操作
		print('wrapper start')
		result = fn(*args, **kwargs)
		# 执行被装饰函数之后的操作
		print('wrapper end')
		return result

	return inner_fun


# 调用装饰器
wrapper_fun(send_message)(*(1, 2), **{'a': 3, 'b': 4})
print('------------------------------------------------------')


#  语法糖版装饰器
def grammar_candy_wrapper_fun(fn):
	def inner_fun(*args, **kwargs):
		# 执行被装饰函数之前的操作
		print('语法糖装饰器 start')
		result = fn(*args, **kwargs)
		# 执行被装饰函数之后的操作
		print('语法糖装饰器 end')
		return result

	return inner_fun


# @装饰器函数名
@grammar_candy_wrapper_fun
def send_message(*args, **kwargs):
	print('send_message start', args, kwargs)


send_message(*(1, 2), **{'a': 3, 'b': 4})
