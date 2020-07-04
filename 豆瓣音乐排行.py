import requests
from bs4 import BeautifulSoup
from lxml import etree

def html_get(url):  # 网页请求

    headars = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    rest = requests.get(url, headers=headars)
    res = rest.text
    soup = BeautifulSoup(res, 'lxml')
    e=etree.HTML(rest.text)
    name=e.xpath('//td/div/a/text()')
    names = [x.strip() for x in name if x.strip() != '']  #去除空格和\n
    # 评分
    pat1 = soup.find_all('span',class_="rating_nums")
    authors = [p.text.split()[0] for p in pat1]
    # 歌手
    pat2=soup.find_all('p',class_="pl")
    cuos=[s.text.split()[0] for s in pat2]
    for i in range(len(names)):
        print(f'{names[i]}：歌手：{cuos[i]}，评分：{authors[i]}')

def main():
    for a in range(0,250,25):
        url=f'https://music.douban.com/top250?start={a}'
        print(f'——————————————————正在爬取第{a//25+1}页——————————————————————')
        html_get(url)

if __name__ == '__main__':
    # 入口
    main()
