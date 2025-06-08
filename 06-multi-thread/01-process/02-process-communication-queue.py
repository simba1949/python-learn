# 进程间的通信
import time
from multiprocessing import Process, Queue

"""
Queue 队列
put(): 添加元素
get(): 获取元素
get_nowait(): 获取元素，如果队列为空，则抛出异常
empty(): 判断队列是否为空
full(): 判断队列是否已满
qsize(): 获取队列大小
"""


def producer(q):
	try:
		for i in range(10):
			q.put(i)
			print('[生产者] put %s' % i)
			time.sleep(1)
		# 发送结束信号
		q.put(None)  # 哨兵值，通知消费者结束
	except Exception as e:
		print(f'[生产者] 出现异常: {e}')


def consumer(q):
	try:
		while True:
			item = q.get()
			if item is None:  # 收到结束信号
				print('[消费者] 收到结束信号，准备退出')
				break
			print('[消费者] get %s' % item)
			time.sleep(1)
	except Exception as e:
		print(f'[消费者] 出现异常: {e}')


if __name__ == '__main__':
	# 创建带限长的队列
	q = Queue(maxsize=20)  # 设置最大容量，避免内存溢出

	p = Process(target=producer, args=(q,), name='生产者')
	c = Process(target=consumer, args=(q,), name='消费者')
	p.start()
	c.start()
	p.join()
	c.join()
