# 需要导入线程模块
import threading
import time

# time.sleep(5) 表示休眠5秒
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Hello World!")
time.sleep(5)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Hello World!")

#  判断是否是主线程
if __name__ == "__main__":
	# 创建线程对象（子线程）
	t1 = threading.Thread(target=print, args=("Hello World!",), daemon=True)  # daemon=True 表示子线程随主线程退出而退出
	t2 = threading.Thread(target=print, args=("Hello World!",))
	t2.daemon = True  # daemon=True 表示子线程随主线程退出而退出
	# 给线程设置名称
	t1.name = "t1"
	t2.name = "t2"
	# 启动线程
	t1.start()
	t2.start()
	# 等待线程结束
	t1.join()
	t2.join()
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "子线程都执行结束了")

