# 创建类
class Person:
	name = None  # 类属性
	age = None  # 类属性

	# 构造方法，实例化对象时自动调用
	def __init__(self, name, age):
		print('Person __init__')
		self.name = name
		self.age = age

	# self 参数是类中的实例方法必须具备的
	def say(self):
		print('%s say hello' % self.name)

	def __str__(self):  # __str__ 方法，打印对象时自动调用

		return 'Person __str__ ' + self.name + ' ' + str(self.age)

	def __del__(self):  # __del__ 方法（析构方法 ），删除对象时自动调用
		print('Person __del__')


# 创建对象，也叫做实例化对象
p1 = Person('anthony', 18)
print(p1)
p1.say()
p1.sex = 'male'  # 添加属性，该属性属于p1对象，不属于类
print(p1.sex)
