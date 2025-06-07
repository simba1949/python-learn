class Person:
	def __init__(self, name, age, price):
		self.__price = price
		self.name = name
		self._age = age

	# 静态方法，静态方法不需要实例化对象，类名.方法名()或者对象.方法名()
	@staticmethod
	def style(**kwargs):
		print("静态方法", kwargs)

	# 类方法，类方法需要实例化对象，类名.方法名()或者对象.方法名()
	@classmethod
	def sleep(cls, name):
		print("类方法", cls, name)


person = Person("李白", 18, 100)
person.style(name="杜甫", age=20)
Person.style(name="'白居易", age=20)

person.sleep("苏轼")
Person.sleep("苏辙")
