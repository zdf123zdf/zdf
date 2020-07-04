from bs4 import BeautifulSoup
import requests
import re

def html_get(url):  # 网页请求

    headars = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    rest = requests.get(url, headers=headars)
    res = rest.text
    soup=BeautifulSoup(res,'lxml')
    # 名字
    pat1=soup.find_all('div',class_="title")
    names =[i.text.split() for i in pat1]
    for i in range(len(names)):
        print(' '.join(names[i]))

def main():
    for a in range(0,150,25):
        url=f'https://www.douban.com/doulist/1231366/?start={a}'
        print(f'——————————————————正在爬取第{a//25+1}页——————————————————————')
        html_get(url)

if __name__ == '__main__':
    # 入口
    main()
