import time

"""
三种时间表示
1. 时间戳
2. 格式化的时间字符串
3. 时间元组
"""

# 时间戳
# 获取当前时间戳，单位为秒，返回为浮点数
timestamp = time.time()
print(timestamp)
print(type(timestamp))  # <class 'float'>
print("---------------时间戳 end-----------------")
# 转成固定格式字符串
c_time = time.ctime()
print(c_time)  # Sun Jun  8 17:00:23 2025
print(type(c_time))  # <class 'str'>
print("---------------时间戳转换成格式化的时间字符串 end -----------------")

# 转换成时间元组
local_time = time.localtime(timestamp)
print(
	local_time)  # time.struct_time(tm_year=2025, tm_mon=6, tm_mday=8, tm_hour=17, tm_min=9, tm_sec=42, tm_wday=6, tm_yday=159, tm_isdst=0)
print(type(local_time))  # <class 'time.struct_time'>
local_time = time.gmtime()
print(
	local_time)  # time.struct_time(tm_year=2025, tm_mon=6, tm_mday=8, tm_hour=9, tm_min=9, tm_sec=42, tm_wday=6, tm_yday=159, tm_isdst=0)
print(type(local_time))  # <class 'time.struct_time'>
print("---------------时间元组转换时间元组 end -----------------")

# 时间元组
# 获取本地时间
local_time = time.localtime()
print(
	local_time)  # time.struct_time(tm_year=2025, tm_mon=6, tm_mday=8, tm_hour=17, tm_min=0, tm_sec=23, tm_wday=6, tm_yday=159, tm_isdst=0)
print(type(local_time))  # <class 'time.struct_time'>
print("---------------时间元组 end -----------------")
# 转换成时间戳
timestamp = time.mktime(local_time)
print(timestamp)
print(type(timestamp))
print("---------------时间元组转换成时间戳 end -----------------")
# 转换成固定格式字符串
asc_time = time.asctime(local_time)
print(asc_time)
print(type(asc_time))
print("---------------时间元组转换成固定格式字符串 end -----------------")

# 格式化时间字符串
format_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(format_time)
# 解析时间字符串
parse_time = time.strptime(format_time, "%Y-%m-%d %H:%M:%S")
print(parse_time)
print("---------------格式化时间字符串 end -----------------")
