# 浅拷贝
list1 = [1, 2, 3]
list2 = list1
list1[0] = 100
print(list1, list2)
# id()函数
print(id(list1), id(list2))

# 深拷贝
# 列表的[:]操作符
list1 = [1, 2, 3]
list2 = list1[:]
list1[0] = 100
print(list1, list2)
print(id(list1), id(list2))
#  copy模块
print("使用 copy 模块")
from copy import deepcopy
list1 = [1, 2, 3]
list2 = deepcopy(list1)
list1[0] = 100
print(list1, list2)
print(id(list1), id(list2))
