# 数据类型
intVal = 2 ^ 128
print(type(intVal))

floatVal = 2.0
print(type(floatVal))

# 布尔类型，严格来说，只有两个值，True和False，
blVal = True
print(type(blVal))

# 复数
complexVal = 1 + 2j
print(complexVal)
print(type(complexVal))

# 字符串
singleQuotation = "hello world"
print(type(singleQuotation))
doubleQuotation = 'hello world'
print(type(doubleQuotation))
tripleQuotation = """hello world"""
print(type(tripleQuotation))
# 字符串可以用 + 合并（粘到一起），也可以用 * 重复：
print("hello " + "world")
print("hello\t" * 3)
