import requests
import re
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
with open('get_sc_v2','w')as f:
    f.write(r.text)
exit()


# call Page JS function

def get_des_psswd(data, key):
    # jsstr = get_js()
    js2py.eval_js(jsstr)
    # return (ctx.call('strEnc', data, key))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数



def get_js(html):
    js = re.compile("arg1='([\s\S]*?)';'")
    jsFunction = re.findall(pattern, html)
    return jsFunction[0]

get_js(html)


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