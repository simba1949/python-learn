"""
python -m pip install requests
"""
import requests
import os

url = ''
data = {
	'username': 'admin',
	'password': 'admin'
}

response = requests.post(url, data=data)
