"""
python -m pip install requests
python -m pip install fake-useragent

session 自动携带 cookie
1.对访问登录后才能访问的页面进行抓包
2.确定登录请求的URL地址，请求方法和所需参数
3.确定登录才能访问的页面的URL和请求方法
4.利用 requests.session() 完成代码
"""
import requests

# 登录
login_url = ""
login_data = {
	"username": "admin",
	"password": "123456"
}
# 访问
url = ""
data = {
	"username": "admin",
	"password": "123456"
}

if __name__ == '__main__':
	session = requests.session()  # 创建 session 对象
	login_response = session.post(url=login_url, data=login_data)

	# 使用 session 访问需要登录后的页面
	response = session.post(url=url, data=data, cookies=login_response.cookies)
