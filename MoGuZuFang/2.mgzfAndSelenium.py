# MGZF 蘑菇租房
import requests
from lxml import etree
import re
import csv
import pandas as pd
import time
import os


class Get_infor():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        }
        self.URL = 'http://www.mgzf.com/' 
        self.start_url = self.URL + 'list/pg1/'
        self.folder = './SH/'
    
        self.title_list=[]#标题列表
        self.address_list=[]#地址列表
        self.shape_list=[]#户型面积列表
        self.money_list=[]#价格列表
        self.href_list=[]#链接列表
        self.detail_list =[]#详细  


    def run(self, useLocal=False):
        '''
        useLoal: use local html file
        '''
        isExists = os.path.exists(self.folder)
        if not isExists:  # 目录不存在，则创建
            os.makedirs(self.folder)
        if useLocal == True:
            # use local html file
            try:
                with open(self.folder+'urlList.html', 'r', encoding='utf-8') as f:
                    html = ''
                    for line in f.readlines():
                        html += line
            except:
                pass
        else:
            html = self.getHTMLText(self.start_url)
            with open(self.folder + 'urlList.html','w',encoding='utf-8') as f:
                f.write(html)
        pattern = re.compile('<span data-v-68579cc8>共([\s\S]*?)页</span>')
        allPage = re.findall(pattern, html)
        print("allPage: " + allPage[0])
        for page in range(1, int(allPage[0])+1):
            url = re.sub(r'pg\d', 'pg'+ str(page), self.start_url)
            self.parseUrl(page, url, useLocal)
        
        #字典中的key值即为csv中列名
        dataframe=pd.DataFrame({
            '标题':self.title_list,   '详细':self.detail_list, 
            '地址':self.address_list, '房型':self.shape_list,
            '价格':self.money_list,   '链接':self.href_list})
        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        dataframe.to_csv(self.folder+"./蘑菇网.csv",index=False,sep=',', encoding='utf_8_sig') 


    def parseUrl(self, page, url, useLocal):
        print('parse url: ' + url) 
        folder = self.folder +'Detail/'
        isExists = os.path.exists(folder)
        if not isExists:  # 目录不存在，则创建
            os.makedirs(folder)   
        if useLocal == True:
            # use local html file
            with open(folder + str(page)+'.html', 'r', encoding='utf-8') as f:
                html = ''
                for line in f.readlines():
                    html += line
            html = etree.HTML(html)
        else:
            # save to local
            with open(folder + str(page)+'.html', 'w', encoding='utf-8') as f:
                f.write(self.getHTMLText(url))
            html = self.getHTMLText(url)
            html = etree.HTML(html)

        # use xpath 
        ele = html.xpath('//*[@id="__layout"]/div/div/div[1]/div[5]/div[1]/div[2]/div')
        for e in ele:
            la = e.xpath('.//a')
            print(len(la))
            for i in la:
                title = i.xpath('.//div/div[2]/h1/span//text()')
                shape = i.xpath('.//div/div[2]/h2[1]//text()')
                detail = i.xpath('.//div/div[2]/h2[2]//text()')
                address = i.xpath('.//div/div[2]/p//text()')
                money = i.xpath('.//div/div[3]/p[1]/span//text()')
                self.title_list.append(title[0])
                self.shape_list.append(shape[0])
                if len(detail) > 0:
                    self.detail_list.append(detail[0])
                else:
                    self.detail_list.append('')
                a = i.xpath('.//@href')
                self.href_list.append(a[0])
                self.address_list.append(address[0])
                self.money_list.append(money[0])
        if useLocal == False:
            time.sleep(0.5)   # 延时

def test():
    # TODO
    # use Selenium (don't need add Cookie)
    work = Get_infor()
    work.run(useLocal=True)
    print('OK')

if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("耗时： {}".format(end-start))

