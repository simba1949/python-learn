class Person:
	name = None  # 公共属性，可以在类的内部、外部自由访问
	_age = None  # 受保护属性，单下划线开头，可以在类的内部、子类中访问
	__price = None  # 私有属性，双下划线开头，只能在类的内部访问，子类不可访问

	# 构造方法，在创建对象时调用
	def __init__(self, name, age, price):
		self.name = name
		self._age = age
		self.__price = price

	# 公共方法，类外部可以访问
	def run(self):
		print(self.name + " run")

	# 受保护方法，方法名前面加一个下划线，子类可以访问
	def _jump(self):
		print(self.name + " jump")

	# 私有方法，方法名前面加两个下划线，子类不可访问
	def __show_price(self):
		print(self.name + " show_price " + str(self.__price))


p1 = Person("张三", 18, 10000)
print(p1.name)
print(p1._age)
# 私有属性实际上是将名字修改为：_Person__price
print(p1._Person__price)
p1.run()
p1._jump()
# 私有方法实际上是将名字修改为：_Person__show_price()
p1._Person__show_price()
