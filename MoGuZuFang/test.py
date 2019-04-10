import requests

url = 'http://www.mgzf.com/list/qy13_0/jg0_1500/sr2/hx1/pg1/?paraName=&showMore=open'
cookies = {
        'acw_sc__v2':'5cad76821b90f52235f602cf3b4925597cbbca88',
        'acw_sc__v3':'5cad68e16c1eda1fb7b3ab86f1f94d83096ec998',
        'gr_user_id':'a9ce2390-02fb-4765-8049-c2fa5554a53f',
        'CNZZDATA1253147438':'647601619-1554852248-http%253A%252F%252Fwww.mgzf.com%252F%7C1554863065',
    }
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}

session = requests.Session()
r = session.get(url, headers=headers, cookies=cookies)
r.raise_for_status()
# r.encoding=r.apparent_encoding
if r.status_code == 200:  # ok
    print('write')
    with open('detail.html','wb') as f:
        f.write(r.content)