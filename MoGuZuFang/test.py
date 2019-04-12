import requests

import js2py

url = 'http://www.mgzf.com'

#cookies = {
#        'acw_sc__v2':'5cad76821b90f52235f602cf3b4925597cbbca88',
#}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}


r = requests.get(url, headers=headers)

cookies = requests.cookies.RequestsCookieJar()
cookies.update(r.cookies)
print(cookies)


# call Page JS function

def get_des_psswd(data, key):
    # jsstr = get_js()
    js2py.eval_js(jsstr)
    # return (ctx.call('strEnc', data, key))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数



def get_js(html):
	js = re.compile('<script>([\s\S]*?)</scipt>')
	jsFunction = re.findall(pattern, html)
    return jsFunction


if __name__ == '__main__':
    print(get_des_psswd('123456', 'RUY2OTdCRUFFRTg0OUQ0Q0E0ODNDRDMxN0YzOEEzREQudG9tY2F0OTQ='))




exit()
res = requests.get(url, headers=headers, cookies=cookies)
print(res.cookies)
with open('r','w') as f:
	f.write(res.text)
exit()














r = s.get(url, headers=headers, cookies=r.cookies)
print(r.cookies)

exit()
session = requests.Session()
r = session.get(url, headers=headers, cookies=cookies)
r.raise_for_status()
# r.encoding=r.apparent_encoding
if r.status_code == 200:  # ok
    print('write')
    with open('detail.html','wb') as f:
        f.write(r.content)