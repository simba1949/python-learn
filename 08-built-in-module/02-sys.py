"""
sys 模块负责程序跟 python 解释器的交互
"""
import sys

# 查看 python 解释器的版本信息
print(sys.version)

# 查看 python 解释器的安装路径
print(sys.path)

# 获取操作系统平台名称
print(sys.platform)

# 查看 python 解释器的默认编码
print(sys.getdefaultencoding())

# 获取系统文件系统编码
print(sys.getfilesystemencoding())
