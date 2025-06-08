# 基础并发模式
"""
关键要点：
1. 所有并发协程必须在同一个事件循环中运行
2. 使用 await 关键字标记可能阻塞的I/O操作
3. 通过 asyncio.run() 启动顶级协程
4. 协程并发是协作式的，需要主动 await 让出控制权
"""
import asyncio


async def task1():
	await asyncio.sleep(1)
	print("任务1完成")


async def task2():
	await asyncio.sleep(2)
	print("任务2完成")


async def main():
	# 通过 asyncio.gather() 同时运行多个协程
	await asyncio.gather(task1(), task2())


if __name__ == "__main__":
	asyncio.run(main())
