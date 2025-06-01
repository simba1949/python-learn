# 创建字典
dict = {'jack': 4098, 'sape': 4139}
print(dict)
# 查看长度
print(len(dict))

# 查看元素
# 获取元素值，如果不存在则报错
val = dict['jack']
print(val)
# get 方法获取元素值，如果不存在则返回 None
val = dict.get('guido')
print(val)

# 如果元素不存在则添加，否则修改
dict['guido'] = 4127
print(dict)

# 删除元素
del dict['sape']
print(dict)

# 循环遍历
for key in dict:
	print(key, dict[key])
print("for in 遍历结束")

for k,v in dict.items():
	print("%s = %s" % (k, v))
print("items 遍历结束")

# 清空字典，删除所有元素，但是字典本身还在
dict.clear()
print(dict)
