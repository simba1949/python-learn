# 类的继承
# 动物类
class Animal:
	name = None

	def __init__(self, name):
		self.name = name
		print('Animal:', name)


# 食肉的动物类
class Carnivora(Animal):
	def __init__(self, name):
		super().__init__(name)
		print('Carnivora:', name)


# 狗类
class Dog(Carnivora, Animal):
	def __init__(self, name):
		super().__init__(name)
		print('Dog:', self.name)


dog = Dog('wangcai')
print(dog.name)
