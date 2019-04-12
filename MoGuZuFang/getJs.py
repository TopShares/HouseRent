import re
import execjs

html =''
with open('get_sc_v2','r') as f:
	for line in f.readlines():
		html += line


def get_js(html):
    pattern = re.compile('<script>([\s\S]*?)</script>')
    jsFunction = re.findall(pattern, html)
    print(jsFunction[0])
    return jsFunction[0]

ctx = execjs.compile(html)
ctx.call("reload") 
