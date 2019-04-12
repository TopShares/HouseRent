import requests
import re
import js2py

url = 'http://www.mgzf.com'

cookies = {
   'acw_sc__v2': '5cb030fe507a26d05f340051113b895a936be261',
   'acw_sc__v3': '5cb0310088cacbdb5c8fd0344f1ab74e96e687ee',
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}



r = requests.get(url, headers=headers, cookies=cookies)
r.raise_for_status()
# r.encoding=r.apparent_encoding
if r.status_code == 200:  # ok
    print('write')
    with open('index.html','wb') as f:
        f.write(r.content)