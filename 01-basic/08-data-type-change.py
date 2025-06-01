# 类型转换
str_val = "123"
int_val = int(str_val)
print("字符串转数字，类型：", type(int_val), "值：", int_val)

str_val = "123.456"
float_val = float(str_val)
print("字符串转浮点数，类型：", type(float_val), "值：", float_val)

str_val = "True"
bool_val = bool(str_val)
print("字符串转布尔值，类型：", type(bool_val), "值：", bool_val)

eval_result = eval("1+1")
print("计算 Python 有效表达式，类型：", type(eval_result), "值：", eval_result)

set_val = {1, 2, 3}
tuple_val = tuple(set_val)
print("集合转元组，类型：", type(tuple_val), "值：", tuple_val)

set_val = {1, 2, 3}
list_val = list(set_val)
print("集合转列表，类型：", type(list_val), "值：", list_val)

int_val = 123
str_val = str(int_val)
print("数字转字符串，类型：", type(str_val), "值：", str_val)
