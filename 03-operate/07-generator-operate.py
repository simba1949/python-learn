# 自定义一个生成器
def count_up_to(max):
	count = 1
	while count <= max:
		yield count  # 每次next()在此暂停并返回值
		count += 1


gen = count_up_to(3)
print(next(gen))  # 输出1，next(gen) 表示调用 count_up_to() 函数
print(next(gen))  # 输出2

# 生成器表达式
squares = (x ** 2 for x in range(5))  # 圆括号形式
print(list(squares))  # [0, 1, 4, 9, 16]
