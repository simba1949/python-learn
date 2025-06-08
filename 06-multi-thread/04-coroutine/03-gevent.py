"""
安装命令：python -m pip   install gevent
卸载命令：python -m pip uninstall gevent
gevent
1. gevent.spawn(函数名)：创建并启动新协程
2. gevent.sleep()：非阻塞式休眠
3。 gevent.join()：等待协程完成
4。 gevent.joinall()：等待所有协程完成
"""
import gevent
from gevent import monkey

# 全局补丁标准库
monkey.patch_all()


def fetch_url(url):
	print(f"GET {url}")
	# 非阻塞式休眠
	gevent.sleep(1)  # 模拟网络请求
	print(f"Done {url}")


if __name__ == '__main__':
	jobs = [
		# 创建并启动新协程
		gevent.spawn(fetch_url, "https://example.com/1"),
		gevent.spawn(fetch_url, "https://example.com/2")
	]
	# 阻塞，等待某个协程执行完毕
	gevent.joinall(jobs)
