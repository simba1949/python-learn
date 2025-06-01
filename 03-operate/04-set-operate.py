set1 = {1, 2, 3, 4, 5}
print("set1:", set1)

set2 = {'a', 'b', 'c', 'd', 'e'}
print("set2:", set2)

# 并集
print("并集：", set1 | set2)
# 交集
print("交集：", set1 & set2)
# 差集
print("差集：", set1 - set2)

# 迭代
for i in set1:
	print(i)
print("迭代结束")

# 判断元素是否在集合中
print(1 in set1)

# 集合长度
print(len(set1))

# 集合清空
set1.clear()
print(set1)

# 集合添加元素
set1.add(1)
print(set1)

# 集合删除元素
set1.remove(1)
print(set1)
