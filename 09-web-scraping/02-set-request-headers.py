"""
python -m pip install requests
python -m pip install fake-useragent
"""

import requests
from fake_useragent import UserAgent

# 获取百度首页
url = "https://www.baidu.com/"
# 设置用户代理前
response = requests.get(url)
print(len(response.text))

# 设置用户代理后
# 设置请求头
headers = {
	# 设置用户代理
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
}
response = requests.get(url, headers=headers)
print(len(response.text))

# 使用 fake_useragent 设置 User-Agent
ua = UserAgent()
# random_ua = ua.random # 随机获取一个 User-Agent
random_ua = ua.chrome  # 使用 chrome 的 User-Agent
print(random_ua)
headers["User-Agent"] = random_ua
response = requests.get(url, headers=headers)
print(len(response.text))
