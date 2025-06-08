# 导入正则模块
import re

# 查看模块包含的方法
print(dir(re))

# 原始字符串‌：使用r''避免转义符冲突
pattern = re.compile(r'\d+')  # 预编译
# 如果匹配成功，返回 Match，否则返回None
m = pattern.match('123abc')
#  打印匹配对象
print(m)
# 获取匹配对象中的内容
print(m.group())
