import os

# 打印操作系统名称，windows:nt, linux:posix
print(os.name)
# 获取环境变量
path = os.getenv('PATH')
print(path)

# 获取当前目录
print(os.getcwd())

file_path = r"D:\DevTool\Pycharm\workspace\python-learn\08-built-in-module\01-os.py"
# 返回文件目录
file_dir_path = os.path.dirname(file_path)
print(file_dir_path)
# 返回文件名
file_name = os.path.basename(file_path)
print(file_name)
# 判断文件是否存在，存在返回 True，不存在返回 False
is_exist = os.path.exists(file_path)
print(is_exist)
# 判断文件是否为文件，是目录返回 True，不是目录返回 False
is_file = os.path.isfile(file_path)
print(is_file)
# 判断文件是否为目录，是目录返回 True，不是目录返回 False
is_dir = os.path.isdir(file_path)
print(is_dir)
# 获取文件大小
file_size = os.path.getsize(file_path)
print(file_size)
# 获取当前路径的绝对路径
file_abs_path = os.path.abspath(file_path)
print(file_abs_path)
