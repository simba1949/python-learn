"""
python -m pip install requests
"""
import requests
import os

url = 'https://img2.baidu.com/it/u=4188295183,762751738&fm=253&fmt=auto&app=138&f=JPEG?w=684&h=1216'
target_file_path = r'download\image.jpg'


def pre_deal():
	# 如果文件存在，则删除文件
	if os.path.exists(target_file_path):
		os.remove(target_file_path)
		print('文件已删除')


def download_image():
	response = requests.get(url)
	response.encoding = 'utf-8'

	if response.status_code == 200:
		content = response.content  # 获取图片内容
		print(type(content))  # <class 'bytes'>

		res_url = response.url  # 获取请求的url
		print(res_url)

		request_headers = response.request.headers  # 获取请求的headers
		print(request_headers)
		print("-------------")
		response_headers = response.headers  # 获取响应的headers
		print(response_headers)

		with open(target_file_path, 'wb') as f:
			f.write(content)
		print('图片已保存')


if __name__ == '__main__':
	pre_deal()
	download_image()
