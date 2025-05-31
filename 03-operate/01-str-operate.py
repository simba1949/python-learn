# 字符串编码， 指定默认是UTF-8
str1 = "hello world"
encode_str = str1.encode('UTF-8')
print("字符串编码：%s" % encode_str)
decode_str = encode_str.decode('GBK')
print("字符串解码：%s" % decode_str)

# + 连接字符串
str1 = "hello"
str2 = "world"
print("+ 连接字符串：%s" % str1 + str2)

# * 重复字符串
str1 = "hello\t"
print("* 重复字符串：%s" % (str1 * 3))

# 通过索引获取字符串中的字符
str1 = "hello world"
print("通过获取字符串中的字符：%s" % (str1[0]))

# 字符串切片，输出结果包含切片开始，但不包含切片结束
str1 = "hello world"
print("字符串切片：%s" % (str1[0:5]))
print("字符串切片：%s" % (str1[0:5:2]))  # 步长为2

# in 成员运算符， 判断字符串中是否包含某个字符
str1 = "hello world"
print("in 运算符：%s" % ("hello" in str1))
#  not in 运算符， 判断字符串中不包含某个字符
str1 = "hello world"
print("not in 运算符：%s" % ("hello" not in str1))

# len() 函数，字符串长度
str1 = "hello world"
print("字符串长度：%s" % (len(str1)))

# r/R 原始字符串
str1 = r"hello \t world"
print("r 原始字符串：%s" % (str1))
str1 = R"hello \t world"
print("R 原始字符串：%s" % (str1))

# 字符串查找，返回字符串中子串的第一个字符的索引，否则返回-1
str1 = "hello world"
print("find 字符串查找：%s" % (str1.find("world")))
print("find 字符串查找：%s" % (str1.find("world", 5)))

# index，检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就会报错
str1 = "hello world"
print("index 字符串查找：%s" % (str1.index("world")))
print("index字符串查找：%s" % (str1.index("world", 5)))

# count，统计字符串中某个子字符串出现的次数
str1 = "hello world hello world hello world"
print("count 字符串查找：%s" % (str1.count("hello")))

# replace，替换字符串中某个子字符串为另一个子字符串
str1 = "hello world"
print("replace 字符串替换：%s" % (str1.replace("world", "python")))
str1 = "hello world world"
print("replace 字符串替换：%s" % (str1.replace("world", "python", 1)))  # 1表示替换次数

# split，字符串分割，返回一个列表
str1 = "hello world hello world"
print("split 列表：%s" % (str1.split(" ")))
