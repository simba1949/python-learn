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

# 字符串切片
str1 = "hello world"
print("字符串切片：%s" % (str1[0:5]))

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
