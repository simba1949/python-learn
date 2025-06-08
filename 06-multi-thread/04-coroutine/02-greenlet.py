"""
安装命令：python -m pip   install greenlet
卸载命令：python -m pip uninstall greenlet
注意：greenlet 属于手动切换，当遇到IO操作，程序会阻塞，而不能进行自动切换
"""
import greenlet

print(greenlet.__version__)  # 应输出安装版本号


def task1():
	print("任务1开始")
	gr2.switch()  # 切换到任务2
	print("任务1结束")
	gr2.switch()  # 再次切换


def task2():
	print("任务2开始")
	gr1.switch()  # 切换回任务1
	print("任务2结束")


if __name__ == '__main__':
	# 创建 greenlet 对象
	gr1 = greenlet.greenlet(task1)
	gr2 = greenlet.greenlet(task2)
	# 启动第一个任务
	gr1.switch()
