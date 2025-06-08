"""
random 用于实现各种分布的伪随机数生成器，可以根据不同的实数分布随机生成值
"""
import random

# 生成0-1之间的随机浮点数
random_float_0_to_1 = random.random()
print(random_float_0_to_1)
print(type(random_float_0_to_1))
print("------------- 生成0-1之间的随机浮点数 -------------")

# 生成指定范围内的随机浮点数
random_float_range = random.uniform(1, 10)
print(random_float_range)
print(type(random_float_range))
print("------------ 生成指定范围内的随机浮点数 -------------")

# 生成指定范围内的随机整数
random_int_range = random.randint(1, 10)
print(random_int_range)
print(type(random_int_range))
print("---------- 生成指定范围内的随机整数 --------------")

# 生成指定长度的随机字符串
random_string = random.randrange(0, 10, 3)
print(random_string)
print(type(random_string))
print("---------- 生成指定长度的随机字符串 ----------------")

# 随机选择一个元素
random_choice = random.choice([1, 2, 3, 4, 5])
print(random_choice)
print(type(random_choice))
print("---------- 随机选择一个元素 ----------------")
