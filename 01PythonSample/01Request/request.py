import requests

response = requests.get('http://www.junpin168.cn')     # Get the request from a normal page
print response.status_code  # >> 200 | 404
print response.encoding    # >> ISO-8859-1
print response.content     # >> <!DOCTYPE html PUBLIC "...
print response.headers     # >> {'content-length': '4152', 'content-encoding'...
print response.headers['content-type']  # >> text/html
print response.url  # >> http://www.junpin168.cn/
print response.ok   # >> True

# Custom Headers
url = 'http://www.junpin168.cn'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
response = requests.get(url,headers=headers)
print response.request.headers  # {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*'...
print response.request.headers['user-agent']    # >> Mozilla/5.0 ...