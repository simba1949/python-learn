# range 函数：https://docs.python.org/zh-cn/3.13/library/stdtypes.html#range
# range 函数格式：range(start, stop[, step])
# start 表示起始值（不指定默认为0）
# stop 表示结束值（不包含）
# step 步长（不指定默认为1）

#  for
for i in range(10):
	print(i)
print("for i in range(10) is end \n")

# range
for i in range(5, 10, 2):
	print(i)
print("for i in range(5, 10, 2) is end \n")

# 遍历字符串
for ele in "hello world":
	print(ele)
print("for c in  \"hello world\" is end \n")
