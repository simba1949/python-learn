# 导入进程模块
from multiprocessing import Process


# 通过Process类创建子进程
def task(name):
	print(f"子进程{name}执行")


# 需将主代码放在 if __name__ == '__main__': 中，避免递归创建进程
if __name__ == "__main__":
	# target 参数指定进程执行的函数，args参数指定函数的参数，name参数指定进程名，daemon参数指定进程是否是守护进程
	p = Process(target=task, args=("A",))
	# 开启子进程
	p.start()
	# is_alive() 方法判断进程是否还活着，如果子进程还活着，则返回True，否则返回False
	print(f"子进程{p.name}是否还活着：{p.is_alive()}")
	# 获取子进程的name和ID
	print(f"子进程{p.name}的ID：{p.pid}")
	# 主进程等待子进程结束
	p.join()
