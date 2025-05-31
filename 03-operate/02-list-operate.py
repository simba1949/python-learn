# 列表，可以存放【任意类型】的数据
datas = [1, "2", 3, "4", 5]
print(datas)

# 新增
datas.append(6)
print(datas)
# 扩展，平铺添加到列表中
datas.extend([7, 8, 9])
print(datas)
# 插入，在指定位置插入，其他元素后移
datas.insert(0, 0)
print(datas)

# 修改
datas[0] = 100
print(datas)

# 删除
# 删除指定位置的元素
del datas[0]
print(datas)
# 删除所有列表
del datas
try:
	if datas:
		print(datas)
except NameError:
	print("列表已删除")

# 清空列表
datas = [1, 2, 3, 4, 5]
datas.clear()
print("清空列表：", datas)

# 排序
datas = [1, 2, 3, 4, 5]
datas.sort()
print("排序：", datas)
datas.sort(reverse=True)
print("倒序：", datas)

# 列表推导式
# 使用列表推导式前
datas = []
for i in range(10):
	datas.append(i)
print("使用列表推导式前：", datas)
# 使用列表推导式后
datas = []
[datas.append(i) for i in range(10)]
print("使用列表推导式后：", datas)
datas = [i for i in range(10)]
print("【简洁版】使用列表推导式后：", datas)

# 列表推导式前(把奇数放进列表里面)
datas = []
for i in range(10):
	if i % 2 == 1:
		datas.append(i)
print("使用列表推导式前：", datas)
# 列表推导式后(把奇数放进列表里面)
datas = []
[datas.append(i) for i in range(10) if i % 2 == 1]
print("使用列表推导式后：", datas)
datas = [i for i in range(10) if i % 2 == 1]
print("【简洁版】使用列表推导式后：", datas)

# 多维列表
# 二维列表
datas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(datas)
