# -*- coding: utf-8 -*-
"""
文件读写
打开文件——>读、写文件——>关闭文件
文件对象的方法
1. open()：创建一个 file 对象，默认是以只读模式打开
2. read(n)：n 表示从文件中读取的数据的长度，没有传 n 则默认一次性读取文件的所有内容
3. write()：将指定内容写入文件
4. close()：关闭文件
5. readline()：读取文件的下一行，如果文件已经读取完毕，则返回空字符串
6. readlines()：读取文件的所有行，返回一个列表，列表的元素是文件中的每一行
文件属性
文件名.name：返回要打开的文件名，可以包含文件的具体路径
文件名.mode：返回文件的访问模式
文件名.closed：检测文件是否关闭，关闭则返回 True
"""
file_path = "./folder/file-1.txt"
file = open(file_path, encoding="utf-8")  # 打开文件
print(file.name)  # 打印文件名
print(file.mode)  # 打印文件访问模式
print(file.closed)  # 打印文件是否关闭

# print(file.read()) # 读取文件所有内容

# print(file.readline()) # 读取文件的下一行

# print(file.readlines())  # 读取文件所有行,返回一个列表

file.close()  # 关闭文件
