# 异常
# 捕获异常
try:
	a = int(input("请输入一个整数："))
	b = int(input("请输入一个整数："))
	print("结果为：", a / b)
except Exception as e:
	print("请输入正确的整数", e)
finally:
	print("程序结束")

# 抛出异常：raise
# Exception(异常提示信息)
raise Exception("手工抛出一个异常")
