# 内置函数
# 查看所有的内置函数，大写字母开头的一般是内置常量名， 小写字母开头的一般是内置函数名
print(dir(__builtins__))

# 返回绝对值
print(abs(-10))
print(abs(10))
# 求和
print(sum((1, 2, 3, 4, 5)))
# 返回最大值
print(max(1, 2, 3, 4, 5))
# 返回最小值
print(min(1, 2, 3, 4, 5))
# 返回绝对值最小的
print(min(-8, 5, key=abs))
# zip 函数：迭代两个序列，返回一个元组，如果迭代序列的长度不一样，则返回长度短的序列长度
for x, y in zip((1, 2, 3), (4, 5, 6)):
	print(x, y)
print("zip 函数执行结束")

# map 函数：迭代一个序列，返回一个迭代器，迭代器中的元素是函数的返回值
for x in map(abs, (-1, 2, -3, 4, -5)):
	print(x)
print("map 函数执行结束")

# reduce 函数：对参数序列中的元素进行累积计算，返回一个值
from functools import reduce

print(reduce(lambda x, y: x + y, (1, 2, 3, 4, 5)))
print("reduce 函数执行结束")
