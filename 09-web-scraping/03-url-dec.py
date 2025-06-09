import urllib.parse

# 原始 URL
url = r"https://www.baidu.com/s?wd=将进酒"

# 解析 URL，仅对查询参数进行编码
parsed = urllib.parse.urlparse(url)
query_params = parsed.query
encoded_query = urllib.parse.quote(query_params)

# 重新构造 URL
encoded_url = parsed._replace(query=encoded_query).geturl()
print(encoded_url)  # https://www.baidu.com/s?wd%3D%E5%B0%86%E8%BF%9B%E9%85%92

# 解码 URL
decoded_url = urllib.parse.unquote(encoded_url)
print(decoded_url)  # https://www.baidu.com/s?wd=将进酒
